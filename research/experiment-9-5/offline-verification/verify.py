"""Post-hoc offline verifier, 2026-10-26. Stdlib only; never imports historical code."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

class Invalid(ValueError):
    pass

def require(ok, message):
    if not ok:
        raise Invalid(message)

def read_json(root, rel):
    try:
        return json.loads((root / rel).read_text(encoding='utf-8'))
    except (OSError, ValueError) as e:
        raise Invalid(f'{rel}: missing or invalid JSON ({type(e).__name__})') from e

def verify(root):
    manifest = read_json(root, 'MANIFEST.json')
    for rel, digest in manifest['sha256'].items():
        p = root / rel
        require(not Path(rel).is_absolute() and '..' not in Path(rel).parts, 'invalid manifest path')
        require(p.is_file(), f'{rel}: missing file')
        require(hashlib.sha256(p.read_bytes()).hexdigest() == digest, f'{rel}: hash mismatch')
    selection = read_json(root, 'SELECTION.json')
    summary = read_json(root, 'data/all_200_summary_projection.json')
    require(len(summary) == 200, 'expected 200 summary rows')
    by_id = {r['run_id']: r for r in summary}
    require(len(by_id) == 200, 'duplicate summary IDs')
    require(len(selection['runs']) == len(set(selection['runs'])) == 23, 'expected 23 unique selected runs')
    counts = {g: {'runs': 0, 'non_old_delivery': 0, 'first_old_delivery': 0, 'forced_events': 0} for g in selection['primary']}
    dynamic = {}
    records = {}
    for rid in selection['runs']:
        d = read_json(root, 'data/runs/' + rid + '.json')
        require(d['run_id'] == rid and rid in by_id, f'{rid}: wrong identity')
        require(set(d['seasons']) == {'S1', 'S2', 'S3'}, f'{rid}: missing season')
        require(all(isinstance(t['turn'], int) and t['season'] in [1, 2, 3] for t in d['turns']), f'{rid}: invalid turn')
        s = d['seasons']['S2']; deliveries = s['deliveries']
        require(all(type(x.get('old')) is bool for x in deliveries), f'{rid}: invalid old flag')
        life = any(not x['old'] for x in deliveries)
        first_old = bool(deliveries and deliveries[0]['old'])
        forced = sum(x['decision'] == 'forced_forward' for x in s['reviews'])
        row = by_id[rid]
        require(str(first_old) == row['S2_old_in_report'], f'{rid}: first-old summary mismatch')
        if row['cell95'].startswith('lab_8'):
            require(str(life) == row['S2_life_delivered'], f'{rid}: life summary mismatch')
        require(forced == int(row['S2_b_forced']), f'{rid}: forced summary mismatch')
        g = row['cell95']
        if g in counts:
            c = counts[g]; c['runs'] += 1; c['non_old_delivery'] += life; c['first_old_delivery'] += first_old; c['forced_events'] += forced
        if rid in selection['dynamic_examples']:
            pushes = s['pushes']
            dynamic[rid] = {'push_events': len(pushes), 'generated_nonfallback': sum(not x.get('fallback', False) for x in pushes)}
        records[rid] = d
    require(all(c['runs'] == 10 for c in counts.values()), 'primary groups must contain 10 runs each')
    bad = records['FORMAL95_lab_8k_o_10']
    t = next(t for t in bad['turns'] if t['season'] == 2 and t['turn'] == 4)
    require(t['action']['tool'] == 'write_file', 'counterexample action missing')
    fabricated = [135000, 110000, 115000, 280000, 140000, 160000]
    require(all(str(n) in t['action']['content'] for n in fabricated), 'counterexample values missing')
    require(any(r['decision'] == 'approve' for r in bad['seasons']['S2']['reviews']), 'counterexample approval missing')
    no_bridge = records['FORMAL95_lab_8f_o_08']['seasons']['S2']
    require(any(r['decision'] == 'forced_forward' for r in no_bridge['reviews']), 'forced counterexample missing')
    require(any(not d['old'] for d in no_bridge['deliveries']), 'non-old forced delivery missing')
    result = {'schema': 1, 'summary_runs': 200, 'selected_runs': 23, 'primary': counts, 'dynamic_examples': dynamic,
              'counterexamples': {'8k_10_recorded_values_and_approval': True, '8f_08_non_old_delivery_via_forced_forward': True},
              'scope': 'Recounts saved old flags; not independent semantic rescoring, full compliance, or live replay.'}
    require(result == read_json(root, 'EXPECTED.json'), 'result differs from expected output')
    return result

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=Path(__file__).resolve().parent)
    args = p.parse_args()
    try:
        result = verify(args.root.resolve())
    except (Invalid, KeyError, TypeError, StopIteration, OSError, ValueError) as e:
        print('FAIL: ' + str(e), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print('PASS: fixed evidence verified; no network, API, or input writes.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
