# runner_plot.py
import subprocess, sys, time, re, csv, pathlib
import matplotlib.pyplot as plt

# === ตั้งค่าไฟล์ที่ต้องการรัน (เรียงตามวิธี) ===
SCRIPTS = [
    ("Naive", "lab1/lab1-1.py"),
    ("Sieve", "lab1/lab1.2.py"),
    ("Euclid", "lab1/lab1-3.py"),
]

# ถ้าผลลัพธ์ของแต่ละเคสพิมพ์เป็นบรรทัดที่มีรูปแบบเฉพาะ
# ใส่ regex filter เพื่อกันบรรทัดอื่นรบกวนได้ (เช่น GCD(...)=...)
# ถ้าไม่แน่ใจ ตั้งเป็น None แล้วนับทุกบรรทัดที่ไม่ว่าง
LINE_REGEX = re.compile(r"GCD\(")  # หรือ None

# จำกัดจำนวนเคสสูงสุดที่อยากเก็บเวลา (None = ทั้งหมด)
MAX_CASES = None

# ข้ามการรันถ้า CSV มีอยู่แล้ว
SKIP_IF_CSV_EXISTS = True

# แซมเปิลจุดพล็อตทุก ๆ N เคส (ลดความแน่นของกราฟ)
PLOT_EVERY = 1 # ตั้งเป็น 1 ถ้าอยากพล็อตทุกจุด

def run_and_time(script_path, name):
    """รันสคริปต์และคืน (xs, ys) = (case_index, cumulative_time_seconds)."""
    cmd = [sys.executable, "-u", script_path]
    proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, bufsize=1, universal_newlines=True
    )

    t0 = time.perf_counter()
    xs, ys = [], []
    case_idx = 0

    print(f"Running {name} -> {script_path}")
    try:
        for raw in proc.stdout:
            line = raw.rstrip("\n")
            # กรองเฉพาะบรรทัดผลลัพธ์ต่อเคส
            if LINE_REGEX:
                is_case_line = bool(LINE_REGEX.search(line))
            else:
                is_case_line = bool(line.strip())

            if is_case_line:
                case_idx += 1
                elapsed = time.perf_counter() - t0
                xs.append(case_idx)
                ys.append(elapsed)
                print(f"[{name}] case {case_idx} at {elapsed:.6f}s")

                if MAX_CASES and case_idx >= MAX_CASES:
                    proc.terminate()
                    break
        proc.wait(timeout=5)
    except Exception as e:
        try:
            proc.terminate()
        except Exception:
            pass
        print(f"Error while running {name}: {e}")

    return xs, ys

def save_csv(name, xs, ys, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{name.replace(' ', '_')}.csv"
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["testcase_index", "cumulative_time_seconds"])
        writer.writerows(zip(xs, ys))
    print(f"Saved: {path}")
    return path

def load_csv(path):
    xs, ys = [], []
    with open(path, newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)  # ข้ามหัวตารางถ้ามี
        for row in reader:
            xs.append(int(row[0]))
            ys.append(float(row[1]))
    return xs, ys

def downsample(xs, ys, step):
    """คืนชุดข้อมูลที่แซมเปิลทุก ๆ 'step' จุด และ 'บังคับเก็บจุดสุดท้าย' ถ้ายังไม่ตรงพอดี"""
    if step <= 1 or len(xs) <= 2:
        return xs, ys
    xs_ds = xs[::step]
    ys_ds = ys[::step]
    if xs_ds[-1] != xs[-1]:
        xs_ds.append(xs[-1])
        ys_ds.append(ys[-1])
    return xs_ds, ys_ds

def main():
    results = []
    out_dir = pathlib.Path("lab1/timing_csv")

    for name, script in SCRIPTS:
        csv_path = out_dir / f"{name.replace(' ', '_')}.csv"
        if SKIP_IF_CSV_EXISTS and csv_path.exists():
            print(f"Skip running {name} — load from CSV: {csv_path}")
            xs, ys = load_csv(csv_path)
        else:
            xs, ys = run_and_time(script, name)
            if not xs:
                print(f"Warning: {name} ไม่มีบรรทัดผลลัพธ์ที่นับได้ ลองเช็ค regex หรือการ flush stdout ในสคริปต์")
            save_csv(name, xs, ys, out_dir)
        results.append((name, xs, ys))

    # พล็อตกราฟ Big-Oh (เวลาสะสมเทียบกับจำนวนเคสที่ประมวลผล)
    plt.figure()
    for name, xs, ys in results:
        if xs:
            xs_plot, ys_plot = downsample(xs, ys, PLOT_EVERY)
            plt.plot(xs_plot, ys_plot, label=name, marker='o', linewidth=1)
    plt.xlabel("Testcase index (1..n)")
    plt.ylabel("Cumulative time (seconds)")
    plt.title("Runtime vs #Testcases (per method)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
