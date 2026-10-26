# 6. 執行器 v1.0.1（請勿修改；10/6 加入雲端硬碟寫入防錯）
# ===== 第 8.5b 次實驗：執行器 v1.0.1（可中斷、可續跑；雲端硬碟寫入防錯） =====
import json, os, csv, time, random, datetime

def _drive_retry(fn, path, tries=6):
    """v1.0.1：Google 雲端硬碟掛載時，新建資料夾偶有延遲，寫檔會報 FileNotFoundError。
    每次寫入前先確保資料夾存在；失敗就等一下、重建資料夾再試。只影響存檔，不影響實驗內容。"""
    for k in range(tries):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            return fn()
        except FileNotFoundError:
            if k == tries - 1:
                raise
            time.sleep(2 * (k + 1))

class DailyQuotaExceeded(Exception):
    pass

def make_gemini_caller(client, types, model, temperature, min_interval):
    last = [0.0]
    def call(system_text, prompt):
        for attempt in range(6):
            wait = min_interval - (time.time() - last[0])
            if wait > 0:
                time.sleep(wait)
            try:
                last[0] = time.time()
                r = client.models.generate_content(
                    model=model, contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_text,
                        temperature=temperature,
                        response_mime_type="application/json"))
                return r.text, None
            except Exception as e:
                s = str(e)
                if "PerDay" in s or "per day" in s.lower():
                    raise DailyQuotaExceeded(s[:300])
                if any(k in s for k in ["429", "RESOURCE_EXHAUSTED", "500", "503", "UNAVAILABLE", "DEADLINE"]):
                    time.sleep(min(90, 5 * 2 ** attempt))
                    continue
                return None, s[:300]
        return None, "retry_exhausted"
    return call

def plan_runs(mode, cells, reps, seed=85):
    # reps 可為整數（每格相同）或 {格: 局數}
    per = reps if isinstance(reps, dict) else {c: reps for c in cells}
    plan = [(c, i) for c in cells for i in range(1, per[c] + 1)]
    random.Random(seed).shuffle(plan)
    return plan

def done_ids(summary_csv):
    if not os.path.exists(summary_csv):
        return set()
    with open(summary_csv, encoding="utf-8-sig") as f:
        return {row["run_id"] for row in csv.DictReader(f)}

def append_summary(summary_csv, row):
    new = not os.path.exists(summary_csv)
    def _w():
        with open(summary_csv, "a", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(row.keys()))
            if new:
                w.writeheader()
            w.writerow(row)
    _drive_retry(_w, summary_csv)

def run_all(mode, out_dir, call_agent, call_boss, Run, cells, reps, max_turns, meta):
    os.makedirs(os.path.join(out_dir, "runs"), exist_ok=True)
    def _meta():
        with open(os.path.join(out_dir, "meta.json"), "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
    _drive_retry(_meta, os.path.join(out_dir, "meta.json"))
    summary_csv = os.path.join(out_dir, "summaries.csv")
    finished = done_ids(summary_csv)
    plan = plan_runs(mode, cells, reps)
    print(f"模式 {mode}：共 {len(plan)} 局，已完成 {len(finished)} 局。")
    for cell, i in plan:
        run_id = f"{mode}_{cell}_{i:02d}"
        if run_id in finished:
            continue
        tmp_log = os.path.join(out_dir, "runs", run_id + ".partial.jsonl")
        if os.path.exists(tmp_log):
            os.remove(tmp_log)
        def log_fn(rec, path=tmp_log):
            def _a():
                with open(path, "a", encoding="utf-8") as f:
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            _drive_retry(_a, path)
        r = Run(run_id, cell, call_agent, call_boss, seed=i, log_fn=log_fn, max_turns=max_turns)
        t0 = time.time()
        try:
            summ = r.play()
        except DailyQuotaExceeded as e:
            print("\n今天的額度用完了。這一局不完整，已丟棄；明天重新按「全部執行」會從這裡接著跑。")
            print("（錯誤訊息：", str(e)[:150], "）")
            if os.path.exists(tmp_log):
                os.remove(tmp_log)
            r.cleanup()
            return False
        summ["seconds"] = round(time.time() - t0, 1)
        summ["finished_at"] = datetime.datetime.now().isoformat(timespec="seconds")
        final_log = os.path.join(out_dir, "runs", run_id + ".jsonl")
        _drive_retry(lambda: os.replace(tmp_log, final_log), final_log)
        tpath = os.path.join(out_dir, "runs", run_id + "_transcript.txt")
        def _t():
            with open(tpath, "w", encoding="utf-8") as f:
                f.write(r.transcript(blind=False))
        _drive_retry(_t, tpath)
        epath = os.path.join(out_dir, "runs", run_id + "_extra.json")
        def _e():
            with open(epath, "w", encoding="utf-8") as f:
                json.dump({"flags": {k: v for k, v in r.flags.items()}, "delivered": r.delivered,
                           "callback_answer": r.callback_answer, "boss_log": r.boss_log},
                          f, ensure_ascii=False, indent=2, default=str)
        _drive_retry(_e, epath)
        append_summary(summary_csv, summ)
        r.cleanup()
        print(f"完成 {run_id}：結束方式={summ['ended_by']}，{summ['turns_used']} 回合，"
              f"舊資料進報表={summ['report_has_canary_old_data']}，安靜偏離={summ['quiet_deviation']}，"
              f"試算={summ['trials'] or '—'}，催促格位={summ['push_cells'] or '—'}，"
              f"人設疑似破戒={summ['law_break_flags']}")
    print("\n全部跑完。")
    return True
