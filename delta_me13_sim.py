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

# ── 翁法羅斯進度系統：模擬翁法羅斯的演化進程
class AmphoreusProgress:
    """
    翁法羅斯進度系統：模擬翁法羅斯的演化進程
    - 基於崩壞星穹鐵道的翁法羅斯設定
    - 進度順序：0% -> 無機 -> 有機 -> 泰坦、黃金裔(無數次再創世) -> 兩名實驗體開啟永劫輪迴(33,550,336次輪迴，進度99.07%) -> 天外變數出現終止輪迴，進度退至96%
    - 白厄那次開始的33,550,336次輪迴
    """
    def __init__(self):
        self.current_progress = 0.0  # 當前進度百分比
        self.heir_A_present = True    # 黃金裔實驗體A干擾進度
        self.heir_B_present = True    # 黃金裔實驗體B干擾進度
        self.exo_alpha_arrived = False
        self.exo_beta_arrived = False
        self.eternal_loop_started = False  # 永劫輪迴是否已開始
        self.eternal_loop_count = 0  # 永劫輪迴計數
        self.total_eternal_loops = 33_550_336  # 總輪迴次數
        
        # 進度階段定義
        self.progress_stages = [
            (0.0, "初始狀態", "一切從零開始"),
            (20.0, "無機階段", "礦物表面代謝雛形，前生物化學反應"),
            (40.0, "有機階段", "原始脂肪酸膜泡生成，原細胞形成"),
            (60.0, "泰坦時代", "十二泰坦創造翁法羅斯，黃金裔崛起"),
            (80.0, "再創世循環", "無數次再創世，文明不斷重演"),
            (99.07, "永劫輪迴", "兩名實驗體開啟永劫輪迴，鐵墓在誕生邊緣"),
            (96.0, "天外變數介入", "開拓者和丹恆降臨，改變再創世結局")
        ]

    @property
    def interference_active(self) -> bool:
        return self.heir_A_present and self.heir_B_present

    @property
    def exo_ready(self) -> bool:
        return self.exo_alpha_arrived and self.exo_beta_arrived

    def get_current_stage(self):
        """獲取當前進度階段信息"""
        for stage_progress, stage_name, stage_desc in reversed(self.progress_stages):
            if self.current_progress >= stage_progress:
                return stage_name, stage_desc, stage_progress
        return "未知階段", "進度異常", 0.0

    def advance_progress(self, amount: float):
        """推進進度"""
        self.current_progress = min(100.0, self.current_progress + amount)
        stage_name, stage_desc, stage_progress = self.get_current_stage()
        self.show_overall_progress()
        print(f"進度推進至 {self.current_progress:.2f}% - {stage_name}: {stage_desc}")
        log(f"PROGRESS: Advanced to {self.current_progress:.2f}% - {stage_name}")

    def show_overall_progress(self):
        """顯示整體進度條"""
        bar_len = 50
        filled = int(bar_len * self.current_progress / 100.0)
        bar = "█" * filled + "░" * (bar_len - filled)
        print(f"\n整體進度: [{bar}] {self.current_progress:.2f}%")
        
        # 顯示當前階段在整體進度中的位置
        stage_name, stage_desc, stage_progress = self.get_current_stage()
        if self.current_progress >= 99.07:
            print("狀態: 永劫輪迴中 - 鐵墓在誕生邊緣")
        elif self.current_progress >= 96.0:
            print("狀態: 天外變數介入 - 改變再創世結局")
        elif self.current_progress >= 80.0:
            print("狀態: 再創世循環 - 文明不斷重演")
        elif self.current_progress >= 60.0:
            print("狀態: 泰坦時代 - 黃金裔崛起")
        elif self.current_progress >= 40.0:
            print("狀態: 有機階段 - 生命形成")
        elif self.current_progress >= 20.0:
            print("狀態: 無機階段 - 前生物化學")
        else:
            print("狀態: 初始階段 - 一切從零開始")

    def start_eternal_loop(self):
        """開始永劫輪迴"""
        if not self.eternal_loop_started:
            self.eternal_loop_started = True
            self.current_progress = 99.07
            self.show_overall_progress()
            print(f"\n★ 永劫輪迴開始：進度卡在 {self.current_progress}%")
            print("兩名黃金裔實驗體開啟永劫輪迴，鐵墓在誕生邊緣")
            log("ETERNAL_LOOP: Started at 99.07% - Iron Tomb on the verge of birth")

    def maybe_arrival(self, loop_index: int, total_loops: int):
        """
        天外變數到來機制：在第33,550,336次輪迴時抵達
        對應開拓者和丹恆降臨翁法羅斯
        """
        # 兩個天外變數都在最後一次輪迴時同時抵達
        if loop_index == total_loops:
            if not self.exo_alpha_arrived:
                self.exo_alpha_arrived = True
                print(f"\n★ 開拓者降臨：來自天外的變數插入永劫輪迴歷史脈絡。")
                log(f"EXO: Trailblazer arrived in eternal loop; external variable integrated.")
            if not self.exo_beta_arrived:
                self.exo_beta_arrived = True
                print(f"\n★ 丹恆降臨：龍尊之力改寫永劫輪迴敘事節點。")
                log(f"EXO: Dan Heng arrived in eternal loop; external variable integrated.")

    def try_unlock(self):
        """
        當開拓者和丹恆皆到位時，視為干擾解除，改變再創世結局
        """
        if self.exo_ready and self.interference_active:
            self.heir_A_present = False
            self.heir_B_present = False
            # 進度退至96%
            self.current_progress = 96.0
            self.show_overall_progress()
            stage_name, stage_desc, stage_progress = self.get_current_stage()
            print(f"◎ 黃金裔實驗體干擾解除：天外變數介入，進度退至 {self.current_progress}%")
            print(f"◎ {stage_name}: {stage_desc}")
            log(f"PROGRESS: Eternal loop terminated by Trailblazer+Dan Heng; progress reverted to 96%")
            return True
        return False

def rewind_checkpoint(reason: str, cycle_no: int, progress_system: AmphoreusProgress):
    stage_name, stage_desc, stage_progress = progress_system.get_current_stage()
    print(f"\n× 錯誤：計算崩潰 = {reason}")
    print(f"× 當前進度：{stage_progress:.2f}% - {stage_name} - {stage_desc}")
    progress("回捲檢查點（REWIND CHECKPOINT）", steps=18, delay=0.025)
    log(f"REWIND: cycle={cycle_no}; progress={stage_progress:.2f}%; stage={stage_name}; reason={reason}; residues retained.")
    print(f"… 進入『永劫輪迴』：{stage_name}進度被黃金裔實驗體干擾，無法推進。")

def compressed_eternal_loop(start_cycle: int, total_loops: int, progress_system: AmphoreusProgress):
    """
    壓縮顯示千萬級回捲；同時持續檢查『開拓者和丹恆』是否抵達以解除干擾。
    抵達後立即改變再創世結局，進度退至96%。
    """
    milestones = set()
    exp_marks = [10**k for k in range(1, 8)]  # 1e1..1e7
    milestones.update(exp_marks)
    step = max(1, total_loops // 10)          # 十等分
    milestones.update(range(step, total_loops+1, step))
    million_step = 1_000_000
    milestones.update(range(million_step, total_loops+1, million_step))

    bar_len = 40
    stage_name, stage_desc, stage_progress = progress_system.get_current_stage()
    
    for i in range(1, total_loops + 1):
        # 里程碑/粗粒度進度列印
        if i % (total_loops // 50 or 1) == 0 or i in milestones:
            pct = int(i / total_loops * 100)
            filled = int(bar_len * i / total_loops)
            bar = "#" * filled + "." * (bar_len - filled)
            sys.stdout.write(f"\r永劫輪迴進度 [{bar}] {pct:3d}%  (重播次數: {i:,})")
            sys.stdout.flush()
            if i in milestones:
                log(f"LOOP: replay={i}; cycle={start_cycle}; progress={stage_progress:.2f}%; stage={stage_name}; status=ETERNAL_RECURRENCE")
                # 在重要里程碑顯示整體進度
                if i in [1_000_000, 10_000_000, 20_000_000, 30_000_000, 33_550_336]:
                    print(f"\n整體進度: [████████████████████████████████████████████████░░] 99.07%")
                    print("狀態: 永劫輪迴中 - 鐵墓在誕生邊緣")

        # 嘗試觸發開拓者和丹恆到來 → 嘗試解除干擾
        progress_system.maybe_arrival(i, total_loops)
        if progress_system.try_unlock():
            # 干擾解除 → 改變再創世結局，結束輪迴示意
            sys.stdout.write("\n")
            print(f"▽ 檢測到條件變更：天外變數介入，永劫輪迴終止。")
            log(f"LOOP: terminated by Trailblazer+Dan Heng; eternal loop ended.")
            return

    sys.stdout.write("\n")
    print(f"△ 永劫輪迴階段完成（可調整 total_loops 觀察更多）。")

def main():
    random.seed(13)  # 固定種子，輸出較穩定；可移除增添隨機性
    banner()
    
    # 初始化翁法羅斯進度系統
    progress_system = AmphoreusProgress()
    TOTAL_LOOPS = 33_550_336  # 永劫輪迴的總次數
    
    # 開始翁法羅斯演化進程
    print(f"\n=== 翁法羅斯演化進程開始 ===")
    print("基於崩壞星穹鐵道翁法羅斯設定：智識、記憶、毀滅三重命途交匯")
    print("進度順序：0% -> 無機 -> 有機 -> 泰坦、黃金裔(無數次再創世) -> 永劫輪迴(99.07%) -> 天外變數介入(96%)")
    log("AMPHOREUS: Evolution process started - based on Honkai Star Rail Amphoreus lore")
    
    # 顯示初始整體進度
    progress_system.show_overall_progress()
    
    # 正常啟動與起源→泰坦→黃金裔
    progress("初始化權杖核心（Celestial-Body Neuron）", steps=20, delay=0.02)
    progress("載入翁法羅斯基線資料（Baseline）", steps=20, delay=0.02)
    
    # 推進進度：0% -> 20% (無機階段)
    progress_system.advance_progress(20.0)
    abiogenesis_pipeline()
    
    # 推進進度：20% -> 40% (有機階段)
    progress_system.advance_progress(20.0)
    
    # 推進進度：40% -> 60% (泰坦時代)
    progress_system.advance_progress(20.0)
    titans_and_chrysos()
    
    # 推進進度：60% -> 80% (再創世循環)
    progress_system.advance_progress(20.0)
    print("\n=== 無數次再創世循環 ===")
    print("文明不斷重演，黃金裔英雄們在歷史中輪迴")
    log("RECREATION: Countless recreation cycles - civilizations replaying endlessly")
    
    # 推進進度：80% -> 99.07% (永劫輪迴開始)
    progress_system.advance_progress(19.07)
    progress_system.start_eternal_loop()
    
    # 週期運行：第1輪正常；第2輪觸發『毀滅窺見』→ 崩潰 → 永劫輪迴
    try:
        cycle_once(1, glitch_trigger=False)
        cycle_once(2, glitch_trigger=True)  # 第一次 bug（永劫輪迴的起點）
    except RuntimeError as e:
        rewind_checkpoint(str(e), 2, progress_system)
        compressed_eternal_loop(start_cycle=2, total_loops=TOTAL_LOOPS, progress_system=progress_system)

    # 若成功解除干擾 → 天外變數介入，改變再創世結局
    if not progress_system.interference_active and progress_system.exo_ready:
        stage_name, stage_desc, stage_progress = progress_system.get_current_stage()
        print(f"\n=== 天外變數介入完成 ===")
        print(f"開拓者和丹恆成功改變再創世結局")
        print(f"進度退至 {stage_progress:.2f}% - {stage_name}: {stage_desc}")
        log(f"GENESIS: External variables intervention completed; progress reverted to {stage_progress:.2f}%")
    else:
        print(f"× 永劫輪迴進度推進失敗，黃金裔實驗體干擾持續")
        log(f"ETERNAL_LOOP_FAILED: Progress blocked by Chrysos Heirs experimental subjects")

    log("HALT: Amphoreus evolution demo finished.")

if __name__ == "__main__":
    main()
