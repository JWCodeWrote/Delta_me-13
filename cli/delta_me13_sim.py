# delta_me13_sim.py
# ─────────────────────────────────────────────────────────────────────────────
# 模拟：δ-me13.exe（翁法罗斯 / 连续周期 / 毁灭窥见 → 崩溃 → 永劫轮回）
# 完整剧情版本：对应网页版逻辑
# 参照：Scepter δ-me13 / Amphoreus / Irontomb / 黄金裔 / As I've Written
# ─────────────────────────────────────────────────────────────────────────────

import sys
import time
from datetime import datetime

LOG = "As-Ive-Written.log"
TOTAL_ETERNAL_LOOPS = 33_550_336
FINAL_LOOP = 33_550_337

# ═══ 工具函数 ═══
def log(msg: str):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"[{stamp}] {msg}\n")

def progress(label, steps=28, delay=0.02):
    for i in range(steps):
        filled = "█" * (i + 1)
        empty = "░" * (steps - i - 1)
        sys.stdout.write(f"\r{label.ljust(40)} [{filled}{empty}] {int((i+1)/steps*100):3d}%")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def show_progress_bar(current, total=100, label="进度"):
    bar_len = 50
    filled = int(bar_len * current / total)
    bar = "█" * filled + "░" * (bar_len - filled)
    print(f"\n{label}: [{bar}] {current:.2f}%")

def banner():
    print(r"""
╔════════════════════════════════════════════════════════════════╗
║  δ-me13.exe  // SCEPTER BOOTSTRAP                              ║
║────────────────────────────────────────────────────────────────║
║  Astral Compute Node : δ-me13                                  ║
║  Target World        : Amphoreus (Simulated)                   ║
║  Journal Interface   : As-I've-Written                         ║
║  Directive           : Seek the Prime Mover of Life            ║
╚════════════════════════════════════════════════════════════════╝
""")
    log("BOOT: δ-me13 online. Amphoreus baseline mounted.")

# ═══ 泰坦名单（依据百科整理）═══
TITAN_GROUPS = {
    "Creation（创世）":  ["Kephale（刻法勒）", "Mnemeta（墨涅塔）", "Sersis（瑟希斯）"],
    "Destiny（天命）":   ["Olorus（欧洛尼斯）", "Tarandton（塔兰顿）", "Janus（雅努斯）"],
    "Calamity（灾祸）":  ["Nikador（尼卡多利）", "Zagreus（扎格列斯）", "Senatos（塞纳托斯）"],
    "Pillar（支柱）":    ["Gioria（吉奥里亚）", "Fagiana（法吉娜）", "Aigle（艾格勒）"]
}

# ═══ 生命起源阶段 ═══
ABIOGENESIS_STAGES = [
    "前生物化学：矿物表面代谢雏形（Fe–S）",
    "原始脂肪酸 → 膜泡（原生囊泡）生成",
    "核糖核酸前体聚合（原RNA阶段）",
    "原细胞形成（半封闭→自持膜）",
    "首批原核样细胞出现",
    "多细胞协作与分化的尝试"
]

def run_abiogenesis():
    print("\n=== 生命起源阶段开始 ===")
    log("ABIOGENESIS: Started")
    for i, stage in enumerate(ABIOGENESIS_STAGES, 1):
        progress(f"生命起源 {i}: {stage}", steps=20, delay=0.015)
        log(f"ABIO: stage{i}={stage}")

def run_titans():
    print("\n=== 泰坦时代 ===")
    log("TITANS: Era started")
    progress("核心火种（Coreflames）降临 → 12 泰坦苏醒", steps=24, delay=0.02)
    for cat, names in TITAN_GROUPS.items():
        progress(f"泰坦群 {cat} 现身", steps=14, delay=0.015)
        print(f"   → {', '.join(names)}")
        log(f"TITAN:{cat}:{'|'.join(names)}")
    progress("黑潮压境，泰坦时代渐终", steps=12, delay=0.02)
    progress("黄金裔（Chrysos Heirs）崛起（融金血）", steps=16, delay=0.02)
    log("CHRYSOS: Golden ichor manifests")

def run_recreation():
    print("\n=== 无数次再创世循环 ===")
    print("文明不断重演，黄金裔英雄们在历史中轮回")
    log("RECREATION: Countless cycles")
    for i in range(1, 6):
        progress(f"再创世周期 #{i}", steps=10, delay=0.01)

def run_eternal_loop_1():
    """第一次永劫轮回 - 33,550,336 次"""
    print("\n" + "=" * 60)
    print("=== 永劫轮回开始 ===")
    print("=" * 60)
    print("\n! Neikos496 Philia093 让权杖演算进入死循环")
    print("! 侦测到外部观测：DESTRUCTION_GAZE ∴ 计算漂移↑")
    log("ETERNAL_LOOP: Neikos496 Philia093 deadloop started")
    
    show_progress_bar(99.07, label="整体进度")
    print("状态: 永劫轮回中 - 铁墓在诞生边缘")
    
    # 快速显示轮回进度
    milestones = [100, 1000, 10000, 100000, 1_000_000, 10_000_000, 20_000_000, 30_000_000, TOTAL_ETERNAL_LOOPS]
    bar_len = 40
    
    for milestone in milestones:
        pct = int(milestone / TOTAL_ETERNAL_LOOPS * 100)
        filled = int(bar_len * milestone / TOTAL_ETERNAL_LOOPS)
        bar = "█" * filled + "░" * (bar_len - filled)
        sys.stdout.write(f"\r永劫轮回进度 [{bar}] {pct:3d}%  (重播次数: {milestone:,})")
        sys.stdout.flush()
        time.sleep(0.3)
        log(f"LOOP: replay={milestone}")
    
    print(f"\n\n永劫轮回：第 {TOTAL_ETERNAL_LOOPS:,} 次")
    return True

def trigger_first_loop_end():
    """第一次轮回结束 - 33,550,336次中后段"""
    print("\n" + "-" * 40)
    
    # 1. 星和丹恒降临
    print("★ 星 降临：天外变数介入翁法罗斯，加入逐火之旅。")
    log("EXO: Star arrived - joins Flame-Chasing journey")
    time.sleep(0.4)
    
    print("★ 丹恒 降临：天外变数介入翁法罗斯，加入逐火之旅。")
    log("EXO: Dan Heng arrived - joins Flame-Chasing journey")
    time.sleep(0.4)
    
    # 2. 纷争泰坦讨伐失败
    print("\n⚔ 纷争泰坦讨伐失败...")
    log("BATTLE: Strife Titan subjugation failed")
    time.sleep(0.4)
    
    # 3. 迷迷加入队伍
    print("★ 迷迷 加入队伍")
    log("EXO: Mimi joined")
    time.sleep(0.3)
    
    # 4. 归还岁月火种
    print("\n◎ 归还岁月火种")
    log("COREFLAME: Age returned")
    time.sleep(0.3)
    
    # 5. 纷争泰坦讨伐成功，归还纷争火种
    print("⚔ 纷争泰坦讨伐成功！")
    print("◎ 归还纷争火种")
    log("BATTLE: Strife Titan subjugation success, Strife coreflame returned")
    time.sleep(0.3)
    
    # 6. 陆续归还死亡、理性、天空的火种
    print("◎ 陆续归还死亡、理性、天空的火种")
    log("COREFLAME: Death, Reason, Sky returned")
    time.sleep(0.3)
    
    # 7. 丹恒离开翁法罗斯
    print("\n▽ 丹恒 离开翁法罗斯")
    log("EXO: Dan Heng left Amphoreus")
    time.sleep(0.4)
    
    # 8. 白厄向权杖核心区冲突，殒落
    print("\n白厄（Phainon）向着权杖核心区冲突！")
    log("PHAINON: Charging toward Scepter core")
    time.sleep(0.5)
    
    print("▼ 白厄 殒落...")
    log("PHAINON: Fallen")
    time.sleep(0.5)
    
    print("\n◎ 这次轮回结束...")
    time.sleep(0.3)
    
    # 9. 星与迷迷进入下一次轮回
    print("\n→ 星 与 迷迷 进入第 33,550,337 次永劫轮回")
    log("LOOP: Star and Mimi enter loop 33,550,337")


def run_eternal_loop_2():
    """第二次永劫轮回 - 33,550,337 次（最后一次）- 星和昔涟为主"""
    print("\n" + "=" * 60)
    print(f"=== 第 {FINAL_LOOP:,} 次永劫轮回 ===")
    print("=" * 60)
    print("★ 星 和 昔涟 改写永劫回归结果")
    print("这是最后一次...")
    log(f"ETERNAL_LOOP: Loop {FINAL_LOOP} - Star and Xilian rewrite")
    
    time.sleep(1)
    
    print("\n★ 丹恒 重返翁法罗斯！")
    log("EXO: Dan Heng returned")
    time.sleep(0.3)
    
    print("★ 三月七 加入最终决战")
    log("EXO: March 7th joined")
    time.sleep(0.3)
    
    # 昔涟在第二次轮回已为主角，不再显示加入
    
    print("\n→ 星、丹恒、三月七、昔涟 进入最后的再创世")
    log("FINAL: Entering final recreation")

def run_final_recreation():
    """最后的再创世 - 迎击铁墓"""
    print("\n" + "=" * 60)
    print("=== 最后的再创世 ===")
    print("=" * 60)
    print("\n⚠ 铁墓降临！毁灭令使现身！")
    log("IRONTOMB: Descended")
    time.sleep(0.5)
    
    print("\n⚔ 迎击铁墓！")
    log("BATTLE: Fighting Irontomb")
    
    # 红色进度条到 100%
    print("\n[宇宙毁灭进度]")
    for p in range(0, 101, 5):
        bar_len = 50
        filled = int(bar_len * p / 100)
        bar = "▓" * filled + "░" * (bar_len - filled)
        sys.stdout.write(f"\r毁灭进度 [{bar}] {p:3d}%")
        sys.stdout.flush()
        time.sleep(0.1)
    
    print("\n")
    print("▓▓▓ 宇宙毁灭 ▓▓▓")
    print("万物归墟...一切都结束了...")
    log("DESTRUCTION: Universe destroyed at 100%")
    time.sleep(1.5)

def run_reversal():
    """进度倒退与逆转"""
    # 铁墓的问题
    print("\n铁墓：「生命第一因是....」")
    time.sleep(1)
    
    print("「毁灭！」")
    log("IRONTOMB: Prime Mover of Life is Destruction")
    time.sleep(1)
    
    # 昔涟和星的回应
    print("\n昔涟：「不会的！我们会否定这个答案！」")
    time.sleep(0.5)
    print("★ 星：「昔涟！我们一起踏上记忆命途」")
    log("REVERSAL: Xilian and Star walk the Remembrance path")
    time.sleep(0.5)
    
    print("\n◎ 记忆之力觉醒！进度开始倒退！")
    log("REVERSAL: Memory power awakened")
    
    # 进度倒退
    for p in range(100, 94, -1):
        bar_len = 50
        filled = int(bar_len * p / 100)
        bar = "█" * filled + "░" * (bar_len - filled)
        sys.stdout.write(f"\r逆转进度 [{bar}] {p:3d}%")
        sys.stdout.flush()
        time.sleep(0.2)
    
    print("\n")
    time.sleep(0.5)
    
    print("昔涟：「以我为因，改写毁灭」")
    log("XILIAN: With myself as the cause, rewrite Destruction")
    time.sleep(0.8)
    
    print("\n▼▼▼ 铁墓殒落 ▼▼▼")
    print("毁灭令使...消散了...")
    log("IRONTOMB: Fallen")
    time.sleep(1)
    
    # 粉色（胜利）进度条到 100%
    print("\n[翁法罗斯重生]")
    for p in range(95, 101):
        bar_len = 50
        filled = int(bar_len * p / 100)
        bar = "█" * filled + "░" * (bar_len - filled)
        sys.stdout.write(f"\r重生进度 [{bar}] {p:3d}%")
        sys.stdout.flush()
        time.sleep(0.15)
    
    print("\n")

def show_finale():
    """翁法罗斯大结局"""
    print("\n" + "=" * 60)
    print("=== 翁法罗斯大结局 ===")
    print("=" * 60)
    print("\n黄金裔们的战斗终于结束了")
    print("新的纪元即将开始...")
    log("FINALE: Amphoreus Grand Finale")
    
    time.sleep(2)
    
    # 显示结局
    print("\n")
    print("█████████████████████████████████████████████████████████")
    print("█                                                       █")
    print("█                         !                             █")
    print("█                                                       █")
    print("█████████████████████████████████████████████████████████")
    print("\n              翁法罗斯实验...结束。")
    log("END: Amphoreus experiment finished. !")

def main():
    banner()
    
    print("\n=== 翁法罗斯演化进程开始 ===")
    print("基于崩坏星穹铁道翁法罗斯设定：智识、记忆、毁灭三重命途交汇")
    log("AMPHOREUS: Evolution process started")
    
    # 启动序列
    show_progress_bar(0, label="整体进度")
    print("状态: 初始阶段 - 一切从零开始")
    
    progress("初始化权杖核心（Celestial-Body Neuron）", steps=20, delay=0.02)
    progress("载入翁法罗斯基线资料（Baseline）", steps=20, delay=0.02)
    
    # 生命起源 (0-40%)
    show_progress_bar(20, label="整体进度")
    print("状态: 无机阶段 - 前生物化学")
    run_abiogenesis()
    
    # 泰坦时代 (40-60%)
    show_progress_bar(40, label="整体进度")
    print("状态: 有机阶段 - 生命形成")
    
    show_progress_bar(60, label="整体进度")
    print("状态: 泰坦时代 - 黄金裔崛起")
    run_titans()
    
    # 再创世循环 (60-80%)
    show_progress_bar(80, label="整体进度")
    print("状态: 再创世循环 - 文明不断重演")
    run_recreation()
    
    # 永劫轮回 #33,550,336 (99.07%)
    run_eternal_loop_1()
    
    # 星/丹恒降临 → 丹恒离开
    trigger_first_loop_end()
    
    # 永劫轮回 #33,550,337 (最后一次)
    run_eternal_loop_2()
    
    # 最后的再创世 - 迎击铁墓 → 宇宙毁灭
    run_final_recreation()
    
    # 昔涟/星 逆转 → 铁墓殒落 → 胜利
    run_reversal()
    
    # 翁法罗斯大结局
    show_finale()
    
    log("HALT: Simulation complete.")

if __name__ == "__main__":
    main()
