/**
 * Amphoreus Progress System - TypeScript Implementation
 * Based on Honkai: Star Rail Amphoreus lore
 * 翁法罗斯进度系统 - 完整剧情版本 (简体中文)
 */

import { ref, computed, reactive } from "vue";
import { translations, type Language, type Translations } from "./i18n";

// 泰坦分类（依据百科）
export const TITAN_GROUPS = {
  "Creation（创世）": [
    "Kephale（刻法勒）",
    "Mnemeta（墨涅塔）",
    "Sersis（瑟希斯）",
  ],
  "Destiny（天命）": [
    "Olorus（欧洛尼斯）",
    "Tarandton（塔兰顿）",
    "Janus（雅努斯）",
  ],
  "Calamity（灾祸）": [
    "Nikador（尼卡多利）",
    "Zagreus（扎格列斯）",
    "Senatos（塞纳托斯）",
  ],
  "Pillar（支柱）": [
    "Gioria（吉奥里亚）",
    "Fagiana（法吉娜）",
    "Aigle（艾格勒）",
  ],
};

// 进度阶段定义
export interface ProgressStage {
  progress: number;
  name: string;
  description: string;
  theme:
    | "initial"
    | "inorganic"
    | "organic"
    | "titan"
    | "recreation"
    | "eternal"
    | "intervention"
    | "destruction"
    | "victory"
    | "finale";
}

export const TOTAL_ETERNAL_LOOPS = 33_550_336;
export const FINAL_LOOP = 33_550_337;

export interface LogEntry {
  timestamp: string;
  message: string;
  type:
    | "info"
    | "warning"
    | "error"
    | "success"
    | "system"
    | "destruction"
    | "victory";
}

// 模拟阶段
export type SimPhase =
  | "boot"
  | "abiogenesis"
  | "titans"
  | "recreation"
  | "eternal_loop_1"
  | "loop_1_end"
  | "eternal_loop_2"
  | "final_recreation"
  | "irontomb_battle"
  | "universe_destruction"
  | "reversal"
  | "irontomb_fall"
  | "finale"
  | "false_ending";

export function useAmphoreus() {
  // 语言设置
  const currentLanguage = ref<Language>("zh-CN");
  const t = computed<Translations>(() => translations[currentLanguage.value]);

  function setLanguage(lang: Language) {
    currentLanguage.value = lang;
    addLog(
      lang === "zh-CN" ? "语言切换为简体中文" : "Language switched to English",
      "system",
    );
  }

  // 状态
  const currentProgress = ref(0);
  const eternalLoopCount = ref(0);
  const currentLoopNumber = ref(1);
  const isRunning = ref(false);
  const isPaused = ref(false);
  const simulationSpeed = ref(1);

  const heirAPresent = ref(true);
  const heirBPresent = ref(true);
  const starArrived = ref(false);
  const danHengArrived = ref(false);
  const danHengLeft = ref(false);
  const mimiArrived = ref(false);
  const march7Arrived = ref(false);
  const xilianArrived = ref(false);

  const eternalLoopStarted = ref(false);
  const simulationComplete = ref(false);
  const irontombDefeated = ref(false);
  const showFalseEnding = ref(false);
  const falseEndingOpacity = ref(0); // 用于慢慢显示
  const isDestructionPhase = ref(false);
  const isVictoryPhase = ref(false);
  const isFlashing = ref(false); // 红橙闪烁状态
  const adminVisible = ref(true); // 管理员可见性

  const logs = reactive<LogEntry[]>([]);
  const currentPhase = ref<SimPhase>("boot");
  const currentSubStage = ref(0);
  const infinityProgress = ref(0);

  // 计算属性
  const interferenceActive = computed(
    () => heirAPresent.value && heirBPresent.value,
  );

  const currentStage = computed((): ProgressStage => {
    const stages = t.value.progressStages;
    if (isDestructionPhase.value) {
      return {
        progress: currentProgress.value,
        name: stages.destruction.name,
        description: stages.destruction.description,
        theme: "destruction",
      };
    }
    if (isVictoryPhase.value) {
      return {
        progress: 100,
        name: stages.victory.name,
        description: stages.victory.description,
        theme: "victory",
      };
    }
    if (currentProgress.value >= 99.07)
      return {
        progress: 99.07,
        name: stages.eternal.name,
        description: stages.eternal.description,
        theme: "eternal",
      };
    if (currentProgress.value >= 80)
      return {
        progress: 80,
        name: stages.recreation.name,
        description: stages.recreation.description,
        theme: "recreation",
      };
    if (currentProgress.value >= 60)
      return {
        progress: 60,
        name: stages.titan.name,
        description: stages.titan.description,
        theme: "titan",
      };
    if (currentProgress.value >= 40)
      return {
        progress: 40,
        name: stages.organic.name,
        description: stages.organic.description,
        theme: "organic",
      };
    if (currentProgress.value >= 20)
      return {
        progress: 20,
        name: stages.inorganic.name,
        description: stages.inorganic.description,
        theme: "inorganic",
      };
    return {
      progress: 0,
      name: stages.initial.name,
      description: stages.initial.description,
      theme: "initial",
    };
  });

  const themeColor = computed(() => {
    if (isDestructionPhase.value) return "#c0392b";
    if (isVictoryPhase.value) return "#ff69b4"; // 粉色
    if (
      eternalLoopStarted.value &&
      !simulationComplete.value &&
      !isVictoryPhase.value
    ) {
      return isFlashing.value ? "#ff4500" : "#c0392b"; // 红橙交替
    }
    const theme = currentStage.value.theme;
    switch (theme) {
      case "initial":
        return "#3a7bd5";
      case "inorganic":
        return "#8e44ad";
      case "organic":
        return "#27ae60";
      case "titan":
        return "#d4af37";
      case "recreation":
        return "#f39c12";
      case "eternal":
        return "#c0392b";
      case "intervention":
        return "#00d4ff";
      default:
        return "#d4af37";
    }
  });

  // 闪烁定时器
  let flashInterval: ReturnType<typeof setInterval> | null = null;

  function startFlashing() {
    if (flashInterval) return;
    flashInterval = setInterval(() => {
      isFlashing.value = !isFlashing.value;
    }, 300);
  }

  function stopFlashing() {
    if (flashInterval) {
      clearInterval(flashInterval);
      flashInterval = null;
    }
    isFlashing.value = false;
  }

  // 日志功能
  function addLog(message: string, type: LogEntry["type"] = "info") {
    const now = new Date();
    const timestamp = now.toLocaleTimeString("zh-CN", { hour12: false });
    logs.unshift({ timestamp, message, type });
    if (logs.length > 100) logs.pop();
  }

  // 重置
  function reset() {
    stopFlashing();
    currentProgress.value = 0;
    eternalLoopCount.value = 0;
    currentLoopNumber.value = 1;
    isRunning.value = false;
    isPaused.value = false;
    heirAPresent.value = true;
    heirBPresent.value = true;
    starArrived.value = false;
    danHengArrived.value = false;
    danHengLeft.value = false;
    mimiArrived.value = false;
    march7Arrived.value = false;
    xilianArrived.value = false;
    eternalLoopStarted.value = false;
    simulationComplete.value = false;
    irontombDefeated.value = false;
    showFalseEnding.value = false;
    falseEndingOpacity.value = 0;
    isDestructionPhase.value = false;
    isVictoryPhase.value = false;
    adminVisible.value = true; // 重置时恢复管理员可见
    currentPhase.value = "boot";
    currentSubStage.value = 0;
    infinityProgress.value = 0;
    logs.length = 0;
    addLog(t.value.systemReset, "system");
  }

  function delay(ms: number): Promise<void> {
    return new Promise((resolve) =>
      setTimeout(resolve, ms / simulationSpeed.value),
    );
  }

  // 启动序列
  async function bootSequence() {
    addLog(t.value.scepterBootstrap, "system");
    addLog(t.value.astralComputeNode, "info");
    addLog(t.value.targetWorld, "info");
    addLog(t.value.journalInterface, "info");
    addLog(t.value.directive, "info");
    await delay(1500);
    addLog(t.value.initCore, "info");
    await delay(1000);
    addLog(t.value.loadBaseline, "info");
    await delay(1000);
  }

  // 生命起源
  async function runAbiogenesis() {
    currentPhase.value = "abiogenesis";
    addLog(t.value.abiogenesisStart, "system");

    const stages = t.value.abiogenesisStages;
    for (let i = 0; i < stages.length; i++) {
      if (!isRunning.value || isPaused.value) {
        while (isPaused.value && isRunning.value) await delay(100);
        if (!isRunning.value) return;
      }
      currentSubStage.value = i;
      addLog(
        `${currentLanguage.value === "zh-CN" ? "生命起源" : "Abiogenesis"} ${i + 1}: ${stages[i]}`,
        "info",
      );
      currentProgress.value = 20 + (i / stages.length) * 20;
      await delay(800);
    }
    currentProgress.value = 40;
  }

  // 泰坦时代
  async function runTitans() {
    currentPhase.value = "titans";
    addLog(t.value.titanEra, "system");
    addLog(t.value.coreflamesDescend, "warning");
    await delay(1000);

    for (const [group, titans] of Object.entries(TITAN_GROUPS)) {
      if (!isRunning.value) return;
      addLog(
        `${t.value.titanGroupAppear} ${group}：${titans.join(", ")}`,
        "info",
      );
      currentProgress.value += 5;
      await delay(600);
    }

    addLog(t.value.darkTideApproach, "warning");
    await delay(800);
    addLog(t.value.chrysosRise, "success");
    currentProgress.value = 60;
    await delay(800);
  }

  // 再创世循环
  async function runRecreation() {
    currentPhase.value = "recreation";
    addLog(t.value.recreationCycles, "system");
    addLog(t.value.civilizationReplay, "info");

    for (let i = 0; i < 5; i++) {
      if (!isRunning.value) return;
      currentProgress.value = 60 + (i / 5) * 20;
      addLog(
        `${t.value.recreationCycle} #${i + 1}... ${currentLanguage.value === "zh-CN" ? "完成" : "Complete"}`,
        "info",
      );
      await delay(400);
    }

    currentProgress.value = 80;
    await delay(500);
  }

  // 第一次永劫轮回
  async function runEternalLoop1() {
    currentPhase.value = "eternal_loop_1";
    currentLoopNumber.value = 1;
    eternalLoopStarted.value = true;
    currentProgress.value = 99.07;
    startFlashing(); // 开始红橙闪烁

    addLog(t.value.eternalRecurrenceStart, "error");
    addLog(t.value.neikosPhiliaDeadloop, "error");
    addLog(t.value.destructionGaze, "error");
    await delay(1000);

    const milestones = [
      100,
      1000,
      10000,
      100000,
      1_000_000,
      10_000_000,
      20_000_000,
      30_000_000,
      TOTAL_ETERNAL_LOOPS,
    ];
    let lastMilestone = 0;

    for (const milestone of milestones) {
      if (!isRunning.value) return;

      const steps = 20;
      const increment = (milestone - lastMilestone) / steps;

      for (let i = 0; i < steps; i++) {
        if (!isRunning.value) return;
        eternalLoopCount.value = Math.floor(
          lastMilestone + increment * (i + 1),
        );
        infinityProgress.value =
          (eternalLoopCount.value / TOTAL_ETERNAL_LOOPS) % 1;
        await delay(50);
      }

      eternalLoopCount.value = milestone;

      if (milestone === TOTAL_ETERNAL_LOOPS) {
        addLog(
          `${t.value.eternalRecurrence}：${currentLanguage.value === "zh-CN" ? "第" : "#"} ${milestone.toLocaleString()} ${currentLanguage.value === "zh-CN" ? "次" : ""}`,
          "warning",
        );
      } else {
        addLog(
          `${t.value.eternalRecurrence}：${t.value.loopReplay} ${milestone.toLocaleString()} ${t.value.loopCount}`,
          "info",
        );
      }
      lastMilestone = milestone;
    }

    await triggerFirstLoopEnd();
  }

  // 第一次轮回结束 - 33,550,336次中后段
  async function triggerFirstLoopEnd() {
    currentPhase.value = "loop_1_end";

    // 1. 星和丹恒降临
    addLog(`${t.value.starDescend}：${t.value.starFromOutside}`, "success");
    starArrived.value = true;
    await delay(800);

    addLog(
      `${t.value.danHengDescend}：${t.value.danHengDragonPower}`,
      "success",
    );
    danHengArrived.value = true;
    await delay(800);

    // 2. 纷争泰坦讨伐失败
    addLog(t.value.strifeTitanFail, "error");
    await delay(800);

    // 3. 迷迷加入队伍
    addLog(t.value.mimiJoin, "success");
    mimiArrived.value = true;
    await delay(800);

    // 4. 归还岁月火种
    addLog(t.value.returnAgeCoreflame, "info");
    await delay(600);

    // 5. 纷争泰坦讨伐成功，归还纷争火种
    addLog(t.value.strifeTitanSuccess, "success");
    addLog(t.value.returnStrifeCoreflame, "info");
    await delay(600);

    // 6. 陆续归还死亡、理性、天空的火种
    addLog(t.value.returnOtherCoreflames, "info");
    await delay(600);

    // 7. 丹恒离开翁法罗斯
    addLog(t.value.danHengLeave, "info");
    danHengLeft.value = true;
    await delay(800);

    // 8. 白厄向权杖核心区冲突，殒落
    addLog(t.value.phainonCharge, "error");
    await delay(1000);
    addLog(t.value.phainonFall, "error");
    await delay(1000);

    addLog(`◎ ${t.value.thisLoopEnd}`, "warning");
    await delay(800);

    // 9. 星与迷迷进入下一次轮回
    addLog(t.value.starMimiEnterLoop, "warning");
    await delay(1000);
  }

  // 第二次永劫轮回 - 星和昔涟为主
  async function runEternalLoop2() {
    currentPhase.value = "eternal_loop_2";
    currentLoopNumber.value = 2;
    eternalLoopCount.value = FINAL_LOOP;

    addLog(t.value.finalLoop, "error");
    addLog(t.value.starXilianRewrite, "success"); // 星和昔涟改写永劫回归结果
    addLog(t.value.lastLoop, "warning");

    for (let i = 0; i < 5; i++) {
      if (!isRunning.value) return;
      infinityProgress.value = i / 5;
      await delay(600);
    }

    await delay(1000);

    addLog(t.value.danHengReturn, "success");
    danHengLeft.value = false;
    await delay(800);

    addLog(t.value.march7Join, "success");
    march7Arrived.value = true;
    await delay(800);

    xilianArrived.value = true; // 昔涟在第二次轮回已加入
    await delay(1000);

    addLog(t.value.enterFinalRecreation, "warning");
    await delay(1000);
  }

  // 最后的再创世
  async function runFinalRecreation() {
    currentPhase.value = "final_recreation";
    isDestructionPhase.value = true;
    stopFlashing();

    addLog(t.value.finalRecreation, "destruction");
    addLog(t.value.irontombDescend, "destruction");
    await delay(1000);

    currentPhase.value = "irontomb_battle";
    addLog(t.value.fightIrontomb, "destruction");

    for (let p = 0; p <= 100; p += 2) {
      if (!isRunning.value) return;
      currentProgress.value = p;
      await delay(100);
    }

    currentProgress.value = 100;
    await delay(500);

    currentPhase.value = "universe_destruction";
    addLog(t.value.universeDestruction, "destruction");
    addLog(t.value.allEnds, "destruction");
    await delay(2000);
  }

  // 进度倒退与胜利
  async function runReversal() {
    currentPhase.value = "reversal";

    // 铁墓的问题
    addLog(t.value.butWait, "destruction");
    await delay(1500);

    addLog(t.value.irontombAnswer, "destruction");
    await delay(1500);

    // 昔涟和星的回应
    addLog(t.value.xilianNotOver, "victory");
    await delay(800);
    addLog(t.value.starStillHere, "victory");
    await delay(1000);

    addLog(t.value.memoryPowerAwaken, "victory");

    for (let p = 100; p >= 95; p -= 1) {
      if (!isRunning.value) return;
      currentProgress.value = p;
      await delay(200);
    }

    await delay(500);

    currentPhase.value = "irontomb_fall";
    isDestructionPhase.value = false;
    isVictoryPhase.value = true;

    addLog(t.value.xilianRewrite, "victory");
    await delay(1000);

    addLog(t.value.irontombFall, "victory");
    addLog(t.value.irontombDissolve, "victory");
    irontombDefeated.value = true;
    await delay(1500);

    // 粉色进度条到100%
    for (let p = 95; p <= 100; p += 1) {
      if (!isRunning.value) return;
      currentProgress.value = p;
      await delay(150);
    }

    currentProgress.value = 100;

    currentPhase.value = "finale";
    adminVisible.value = false; // 大结局后管理员消失
    addLog(t.value.amphoreusFinaleSub, "victory");
    addLog(t.value.goldenHeirsBattleEnd, "victory");
    addLog(t.value.newEraBegin, "victory");
    await delay(2000);
  }

  // 显示结局 - 慢慢淡入约13秒
  async function showEnding() {
    currentPhase.value = "false_ending";
    showFalseEnding.value = true;
    simulationComplete.value = true;
    isRunning.value = false;

    addLog("", "system");
    addLog("█████████████████████████████", "system");
    addLog("█                           █", "system");
    addLog("█            !              █", "system");
    addLog("█                           █", "system");
    addLog("█████████████████████████████", "system");
    addLog("", "system");
    addLog(t.value.amphoreusExperimentEnd, "system");

    // 13秒慢慢淡入
    const totalDuration = 13000;
    const steps = 100;
    const stepDuration = totalDuration / steps;

    for (let i = 0; i <= steps; i++) {
      falseEndingOpacity.value = i / steps;
      await new Promise((resolve) => setTimeout(resolve, stepDuration));
    }
  }

  // 主运行函数
  async function startSimulation() {
    if (isRunning.value) return;

    reset();
    isRunning.value = true;

    await bootSequence();
    if (!isRunning.value) return;

    await runAbiogenesis();
    if (!isRunning.value) return;

    await runTitans();
    if (!isRunning.value) return;

    await runRecreation();
    if (!isRunning.value) return;

    await runEternalLoop1();
    if (!isRunning.value) return;

    await runEternalLoop2();
    if (!isRunning.value) return;

    await runFinalRecreation();
    if (!isRunning.value) return;

    await runReversal();
    if (!isRunning.value) return;

    await showEnding();
  }

  function togglePause() {
    isPaused.value = !isPaused.value;
    addLog(
      isPaused.value ? t.value.simulationPaused : t.value.simulationResumed,
      "system",
    );
  }

  function stop() {
    stopFlashing();
    isRunning.value = false;
    isPaused.value = false;
    addLog(t.value.simulationStopped, "system");
  }

  function setSpeed(speed: number) {
    simulationSpeed.value = speed;
    addLog(`${t.value.speedSet} ${speed}x`, "system");
  }

  function closeEnding() {
    showFalseEnding.value = false;
    falseEndingOpacity.value = 0;
  }

  return {
    // i18n
    currentLanguage,
    t,
    setLanguage,

    // State
    currentProgress,
    eternalLoopCount,
    currentLoopNumber,
    isRunning,
    isPaused,
    simulationSpeed,
    heirAPresent,
    heirBPresent,
    starArrived,
    danHengArrived,
    danHengLeft,
    mimiArrived,
    march7Arrived,
    xilianArrived,
    eternalLoopStarted,
    simulationComplete,
    irontombDefeated,
    showFalseEnding,
    falseEndingOpacity,
    isDestructionPhase,
    isVictoryPhase,
    isFlashing,
    adminVisible,
    logs,
    currentPhase,
    currentSubStage,
    infinityProgress,

    // Computed
    interferenceActive,
    currentStage,
    themeColor,

    // Constants
    TOTAL_ETERNAL_LOOPS,
    FINAL_LOOP,

    // Methods
    startSimulation,
    togglePause,
    stop,
    reset,
    setSpeed,
    closeEnding,
  };
}
