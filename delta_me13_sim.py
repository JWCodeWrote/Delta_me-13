# delta_me13_sim.py
# ─────────────────────────────────────────────────────────────────────────────
# 模擬：δ-me13.exe（翁法羅斯 / 連續週期 / 毀滅窺見 → 崩潰 → 永劫輪迴）
# 增補：無機→有機、十二泰坦、黃金裔；兩個黃金裔實驗體干擾「再創世」，
#       造成本世無法創世，只能回捲；直到「兩個天外變數」到來才解除。
# 參照：Scepter δ-me13（星際計算機）/ Amphoreus 持續週期 / Irontomb（毀滅） /
#       黃金裔（Golden ichor, Flame-Chase）/ As I've Written（電腦介面）
# ─────────────────────────────────────────────────────────────────────────────

import sys, time, random
from datetime import datetime

LOG = "As-Ive-Written.log"

# ── 寫記事（對應《如我所書》的電腦介面風格）
def log(msg: str):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"[{stamp}] {msg}\n")

def progress(label, steps=28, delay=0.02):
    sys.stdout.write(f"{label.ljust(34)}")
    for i in range(steps):
        filled = "#" * (i+1)
        sys.stdout.write(f"\r{label.ljust(24)} [{filled.ljust(steps)}] {int((i+1)/steps*100):3d}%")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def banner():
    print(r"""
δ-me13.exe  // SCEPTER BOOTSTRAP
--------------------------------
Astral Compute Node : δ-me13
Target World        : Amphoreus (Simulated)
Journal Interface   : As-I've-Written
Directive           : Seek the Prime Mover of Life  // 生命第一驅動
""")
    log("BOOT: δ-me13 online. Amphoreus baseline mounted. Directive=PrimeMoverOfLife")

# ── 生命起源：從無機到有機（科學常見路徑作為演繹）
def abiogenesis_pipeline():
    stages = [
        "前生物化學：礦物表面代謝雛形（Fe–S）",
        "原始脂肪酸 → 膜泡（原生囊泡）生成",
        "核醣核酸前體聚合（原RNA階段）",
        "原細胞形成（半封閉→自持膜）",
        "首批原核樣細胞出現",
        "多細胞協作與分化的嘗試"
    ]
    for i, s in enumerate(stages, 1):
        progress(f"生命起源{i}: {s}", steps=22, delay=0.02)
        log(f"ABIO: stage{i}={s}")

# ── 神話系統：十二泰坦與黃金裔（黃金之血 / Flame-Chase）
TITAN_GROUPS = {
    "Foundation": ["Kephale", "Phainon", "Janus"],
    "Creation":   ["Oronyx", "Cyrene", "Ladon"],
    "Calamity":   ["Nikador", "Tartarus", "Atropos"],
    "Fate":       ["Moira", "Chronos", "Mneme"]
}
def titans_and_chrysos():
    progress("核心火種（Coreflames）降臨 → 12 泰坦甦醒", steps=24, delay=0.02)
    for cat, names in TITAN_GROUPS.items():
        progress(f"泰坦群 {cat} 現身：{', '.join(names)}", steps=14, delay=0.018)
        log(f"TITAN:{cat}:{'|'.join(names)}")
    progress("黑潮壓境，泰坦時代漸終", steps=12, delay=0.02)
    progress("黃金裔（Chrysos Heirs）崛起（融金血）", steps=16, delay=0.02)
    log("CHRYSOS: Golden ichor manifests; Flame-Chase mandate issued.")

# ── 核心：週期內流程（含「觀測同步」→ 可能被『毀滅』窺見）
def cycle_once(cycle_no: int, glitch_trigger=False):
    print(f"\n-- Amphoreus Cycle #{cycle_no} --")
    progress("敘事索引綁定（如我所書）", steps=18, delay=0.02)
    progress("命途映射與劇情收斂", steps=18, delay=0.02)
    progress("觀測同步（觀者效應校準）", steps=22, delay=0.02)
    if glitch_trigger:
        print("! 偵測到外部觀測：DESTRUCTION_GAZE ∴ 計算漂移↑")
        log(f"CYCLE {cycle_no}: Destruction gaze detected; drift escalating.")
        time.sleep(0.5)
        print("! 漂移校準失敗 → 狀態坍縮：IRONTOMB_TRANSIENT_STATE")
        log(f"CYCLE {cycle_no}: Collapse=IRONTOMB_TRANSIENT_STATE -> entering ETERNAL_RECURRENCE")
        raise RuntimeError("ETERNAL_RECURRENCE")
    else:
        progress("封印輸出（Irontomb Vault）", steps=12, delay=0.02)
        log(f"CYCLE {cycle_no}: Completed & sealed.")
        print(f"Cycle #{cycle_no} 完成（封存）。")

# ── 你的新規則：兩個黃金裔實驗體干擾「再創世」
class GenesisGate:
    """
    控制「再創世（Re-Genesis）」是否允許。
    - 兩個黃金裔實驗體（A、B）在場即視為『干擾中』→ 不允許再創世。
    - 僅在兩個『天外變數』都抵達後，干擾解除 → 再創世允許。
    """
    def __init__(self):
        self.heir_A_present = True    # 初始：兩實驗體都在，阻斷再創世
        self.heir_B_present = True
        self.exo_alpha_arrived = False
        self.exo_beta_arrived  = False

    @property
    def interference_active(self) -> bool:
        return self.heir_A_present and self.heir_B_present

    @property
    def exo_ready(self) -> bool:
        return self.exo_alpha_arrived and self.exo_beta_arrived

    def maybe_arrival(self, loop_index: int, total_loops: int):
        """
        以『里程碑』與『隨機』雙條件模擬兩個天外變數到來：
        - 達到一定進度比例後才可能觸發（量感：千萬級輪迴）。
        - 重要里程碑時提高觸發率，並輸出提示。
        """
        progress_ratio = loop_index / max(1, total_loops)
        # 只有在 60% 之後才有機會陸續到來，符合「久經輪迴才得外助」的敘事
        if (not self.exo_alpha_arrived) and progress_ratio > 0.60:
            if random.random() < (0.002 + 0.05 * (progress_ratio - 0.60)):
                self.exo_alpha_arrived = True
                print("\n★ 天外變數 α 抵達：外域觀測者插入歷史脈絡。")
                log("EXO: alpha arrived; external variable integrated.")
        if (not self.exo_beta_arrived) and progress_ratio > 0.80:
            if random.random() < (0.002 + 0.07 * (progress_ratio - 0.80)):
                self.exo_beta_arrived = True
                print("\n★ 天外變數 β 抵達：外域干涉者改寫敘事節點。")
                log("EXO: beta arrived; external variable integrated.")

    def try_unlock(self):
        """
        當兩個天外變數皆到位時，視為干擾解除（兩實驗體被引離/鎖定/偏轉）。
        """
        if self.exo_ready and self.interference_active:
            self.heir_A_present = False
            self.heir_B_present = False
            print("◎ 兩實驗體干擾解除：『再創世』條件達成。")
            log("GENESIS: interference cleared by EXO alpha+beta.")

def rewind_checkpoint(reason: str, cycle_no: int):
    print("\n× 錯誤：計算崩潰 =", reason)
    progress("回捲檢查點（REWIND CHECKPOINT）", steps=18, delay=0.025)
    log(f"REWIND: cycle={cycle_no}; reason={reason}; residues retained.")
    print("… 進入『永劫輪迴』：本世無法再創世（兩實驗體干擾中）。")

def compressed_eternal_loop(start_cycle: int, total_loops: int, gate: GenesisGate):
    """
    壓縮顯示千萬級回捲；同時持續檢查『天外變數』是否抵達以解除干擾。
    抵達後立即嘗試『再創世』並結束示意。
    """
    milestones = set()
    exp_marks = [10**k for k in range(1, 8)]  # 1e1..1e7
    milestones.update(exp_marks)
    step = max(1, total_loops // 10)          # 十等分
    milestones.update(range(step, total_loops+1, step))
    million_step = 1_000_000
    milestones.update(range(million_step, total_loops+1, million_step))

    bar_len = 40
    for i in range(1, total_loops + 1):
        # 里程碑/粗粒度進度列印
        if i % (total_loops // 50 or 1) == 0 or i in milestones:
            pct = int(i / total_loops * 100)
            filled = int(bar_len * i / total_loops)
            bar = "#" * filled + "." * (bar_len - filled)
            sys.stdout.write(f"\r永劫輪迴進度 [{bar}] {pct:3d}%  (重播次數: {i:,})")
            sys.stdout.flush()
            if i in milestones:
                log(f"LOOP: replay={i}; cycle={start_cycle}; status=ETERNAL_RECURRENCE")

        # 嘗試觸發天外變數到來 → 嘗試解除干擾
        gate.maybe_arrival(i, total_loops)
        gate.try_unlock()
        if gate.exo_ready and not gate.interference_active:
            # 干擾解除 → 允許再創世，結束輪迴示意
            sys.stdout.write("\n")
            print("▽ 檢測到條件變更：允許『再創世（Re-Genesis）』，停止回捲。")
            log("LOOP: terminated by EXO variables; Re-Genesis unlocked.")
            return

    sys.stdout.write("\n")
    print("△ 輪迴階段示意完成（可調整 total_loops 觀察更多）。")

def main():
    random.seed(13)  # 固定種子，輸出較穩定；可移除增添隨機性
    banner()
    # 正常啟動與起源→泰坦→黃金裔
    progress("初始化權杖核心（Celestial-Body Neuron）", steps=20, delay=0.02)
    progress("載入翁法羅斯基線資料（Baseline）", steps=20, delay=0.02)
    abiogenesis_pipeline()
    titans_and_chrysos()

    # 週期運行：第1輪正常；第2輪觸發『毀滅窺見』→ 崩潰 → 永劫輪迴
    gate = GenesisGate()  # 兩實驗體干擾再創世的門檻
    try:
        cycle_once(1, glitch_trigger=False)
        cycle_once(2, glitch_trigger=True)  # 第一次 bug（永劫輪迴的起點）
    except RuntimeError as e:
        rewind_checkpoint(str(e), 2)
        TOTAL_LOOPS = 10_000_000  # 量感：上千萬次循環
        compressed_eternal_loop(start_cycle=2, total_loops=TOTAL_LOOPS, gate=gate)

    # 若成功解除干擾 → 嘗試再創世的收束畫面
    if not gate.interference_active and gate.exo_ready:
        progress("再創世程序啟動（Re-Genesis Protocol）", steps=24, delay=0.02)
        print("◎ 本世創世成功：進入新基線。")
        log("GENESIS: Re-Genesis completed; new baseline committed.")

    log("HALT: demo finished.")

if __name__ == "__main__":
    main()
