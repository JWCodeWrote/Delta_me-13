/**
 * Internationalization for Amphoreus Simulation
 * 翁法罗斯模拟 - 多语言支持
 */

export type Language = "zh-CN" | "en";

export interface Translations {
  // 系统
  systemReset: string;
  simulationPaused: string;
  simulationResumed: string;
  simulationStopped: string;
  speedSet: string;

  // 启动序列
  scepterBootstrap: string;
  astralComputeNode: string;
  targetWorld: string;
  journalInterface: string;
  directive: string;
  initCore: string;
  loadBaseline: string;

  // 生命起源
  abiogenesisStart: string;
  abiogenesisStages: string[];

  // 泰坦时代
  titanEra: string;
  coreflamesDescend: string;
  titanGroupAppear: string;
  darkTideApproach: string;
  chrysosRise: string;

  // 再创世
  recreationCycles: string;
  civilizationReplay: string;
  recreationCycle: string;

  // 永劫轮回
  eternalRecurrenceStart: string;
  neikosPhiliaDeadloop: string;
  destructionGaze: string;
  eternalRecurrence: string;
  loopReplay: string;
  loopCount: string;
  thisLoopEnd: string;

  // 角色
  phainonCharge: string;
  phainonFall: string;
  starDescend: string;
  starFromOutside: string;
  danHengDescend: string;
  danHengDragonPower: string;
  strifeTitanFail: string;
  strifeTitanSuccess: string;
  returnAgeCoreflame: string;
  returnStrifeCoreflame: string;
  returnOtherCoreflames: string;
  danHengLeave: string;
  mimiJoin: string;
  starMimiEnterLoop: string;
  finalLoop: string;
  starXilianRewrite: string;
  lastLoop: string;
  danHengReturn: string;
  march7Join: string;
  xilianJoin: string;
  enterFinalRecreation: string;

  // 最终战斗
  finalRecreation: string;
  irontombDescend: string;
  fightIrontomb: string;
  universeDestruction: string;
  allEnds: string;
  butWait: string;
  irontombAnswer: string;
  xilianNotOver: string;
  starStillHere: string;
  memoryPowerAwaken: string;
  xilianRewrite: string;
  irontombFall: string;
  irontombDissolve: string;

  // 大结局
  amphoreusFinaleSub: string;
  goldenHeirsBattleEnd: string;
  newEraBegin: string;
  amphoreusFinaleName: string;
  amphoreusExperimentEnd: string;

  // UI
  systemStatus: string;
  worldSimulation: string;
  targetWorldLabel: string;
  amphoreus: string;
  journalInterfaceLabel: string;
  pathConvergence: string;
  erudition: string;
  remembrance: string;
  destruction: string;
  exoVariables: string;
  star: string;
  danHeng: string;
  left: string;
  mimi: string;
  march7: string;
  xilian: string;
  battleResult: string;
  irontombFallen: string;
  finalResult: string;
  lastLoopLabel: string;
  startSimulation: string;
  running: string;
  pause: string;
  resume: string;
  stopBtn: string;
  resetBtn: string;
  speed: string;
  waitingForSimulation: string;
  directiveLabel: string;
  seekPrimeMover: string;
  administrator: string;
  lygus: string;
  experimentEnd: string;
  inDestruction: string;
  inEternalLoop: string;
  irontombVictory: string;
  victory: string;
  standby: string;
  paused: string;

  // 阶段
  phases: {
    boot: string;
    abiogenesis: string;
    titans: string;
    recreation: string;
    eternal_loop_1: string;
    loop_1_end: string;
    eternal_loop_2: string;
    final_recreation: string;
    irontomb_battle: string;
    universe_destruction: string;
    reversal: string;
    irontomb_fall: string;
    finale: string;
    false_ending: string;
  };

  // 进度阶段
  progressStages: {
    initial: { name: string; description: string };
    inorganic: { name: string; description: string };
    organic: { name: string; description: string };
    titan: { name: string; description: string };
    recreation: { name: string; description: string };
    eternal: { name: string; description: string };
    intervention: { name: string; description: string };
    destruction: { name: string; description: string };
    victory: { name: string; description: string };
  };
}

export const translations: Record<Language, Translations> = {
  "zh-CN": {
    // 系统
    systemReset: "系统重置完成",
    simulationPaused: "模拟已暂停",
    simulationResumed: "模拟继续运行",
    simulationStopped: "模拟已停止",
    speedSet: "模拟速度设为",

    // 启动序列
    scepterBootstrap: "δ-me13.exe // SCEPTER BOOTSTRAP",
    astralComputeNode: "Astral Compute Node: δ-me13",
    targetWorld: "Target World: Amphoreus (Simulated)",
    journalInterface: "Journal Interface: As-I've-Written",
    directive: "Directive: Seek the Prime Mover of Life",
    initCore: "初始化权杖核心（Celestial-Body Neuron）...",
    loadBaseline: "载入翁法罗斯基线资料（Baseline）...",

    // 生命起源
    abiogenesisStart: "=== 生命起源阶段开始 ===",
    abiogenesisStages: [
      "前生物化学：矿物表面代谢雏形（Fe–S）",
      "原始脂肪酸 → 膜泡（原生囊泡）生成",
      "核糖核酸前体聚合（原RNA阶段）",
      "原细胞形成（半封闭→自持膜）",
      "首批原核样细胞出现",
      "多细胞协作与分化的尝试",
    ],

    // 泰坦时代
    titanEra: "=== 泰坦时代 ===",
    coreflamesDescend: "核心火种（Coreflames）降临 → 12 泰坦苏醒",
    titanGroupAppear: "泰坦群现身",
    darkTideApproach: "黑潮压境，泰坦时代渐终",
    chrysosRise: "黄金裔（Chrysos Heirs）崛起（融金血）",

    // 再创世
    recreationCycles: "=== 无数次再创世循环 ===",
    civilizationReplay: "文明不断重演，黄金裔英雄们在历史中轮回",
    recreationCycle: "再创世周期",

    // 永劫轮回
    eternalRecurrenceStart: "=== 永劫轮回开始 ===",
    neikosPhiliaDeadloop: "Neikos496 Philia093 让权杖演算进入死循环",
    destructionGaze: "侦测到外部观测：DESTRUCTION_GAZE ∴ 计算漂移↑",
    eternalRecurrence: "永劫轮回",
    loopReplay: "已重播",
    loopCount: "次",
    thisLoopEnd: "这次轮回结束...",

    // 角色
    phainonCharge: "白厄（Phainon）向着权杖核心区冲突！",
    phainonFall: "▼ 白厄 殒落...",
    starDescend: "★ 星 降临",
    starFromOutside: "天外变数介入翁法罗斯，加入逐火之旅。",
    danHengDescend: "★ 丹恒 降临",
    danHengDragonPower: "天外变数介入翁法罗斯，加入逐火之旅。",
    strifeTitanFail: "⚔ 纷争泰坦讨伐失败...",
    strifeTitanSuccess: "⚔ 纷争泰坦讨伐成功！",
    returnAgeCoreflame: "◎ 归还岁月火种",
    returnStrifeCoreflame: "◎ 归还纷争火种",
    returnOtherCoreflames: "◎ 陆续归还死亡、理性、天空的火种",
    danHengLeave: "▽ 丹恒 离开翁法罗斯",
    mimiJoin: "★ 迷迷 加入队伍",
    starMimiEnterLoop: "→ 星 与 迷迷 进入第 33,550,337 次永劫轮回",
    finalLoop: "=== 第 33,550,337 次永劫轮回 ===",
    starXilianRewrite: "★ 星 和 昔涟 改写永劫回归结果",
    lastLoop: "这是最后一次...",
    danHengReturn: "★ 丹恒 重返翁法罗斯！",
    march7Join: "★ 三月七 加入最终决战",
    xilianJoin: "★ 昔涟 加入最终决战",
    enterFinalRecreation: "→ 星、丹恒、三月七、昔涟 进入最后的再创世",

    // 最终战斗
    finalRecreation: "=== 最后的再创世 ===",
    irontombDescend: "铁墓降临！毁灭令使现身！",
    fightIrontomb: "⚔ 迎击铁墓！",
    universeDestruction: "▓▓▓ 宇宙毁灭 ▓▓▓",
    allEnds: "万物归墟...一切都结束了...",
    butWait: "铁墓：「生命第一因是....」",
    irontombAnswer: "「毁灭！」",
    xilianNotOver: "昔涟：「不会的！我们会否定这个答案！」",
    starStillHere: "★ 星：「昔涟！我们一起踏上记忆命途」",
    memoryPowerAwaken: "◎ 记忆之力觉醒！进度开始倒退！",
    xilianRewrite: "昔涟：「以我为因，改写毁灭」",
    irontombFall: "▼▼▼ 铁墓殒落 ▼▼▼",
    irontombDissolve: "毁灭令使...消散了...",

    // 大结局
    amphoreusFinaleSub: "=== 翁法罗斯大结局 ===",
    goldenHeirsBattleEnd: "黄金裔们的战斗终于结束了",
    newEraBegin: "新的纪元即将开始...",
    amphoreusFinaleName: "翁法罗斯大结局",
    amphoreusExperimentEnd: "翁法罗斯实验...结束。",

    // UI
    systemStatus: "系统状态",
    worldSimulation: "世界模拟",
    targetWorldLabel: "目标世界",
    amphoreus: "Amphoreus",
    journalInterfaceLabel: "记事接口",
    pathConvergence: "命途交汇",
    erudition: "智识 Erudition",
    remembrance: "记忆 Remembrance",
    destruction: "毁灭 Destruction",
    exoVariables: "天外变数",
    star: "星",
    danHeng: "丹恒",
    left: "(已离开)",
    mimi: "迷迷",
    march7: "三月七",
    xilian: "昔涟",
    battleResult: "战斗结果",
    irontombFallen: "⚔ 铁墓殒落",
    finalResult: "最终结果",
    lastLoopLabel: "最后一次轮回",
    startSimulation: "开始模拟",
    running: "运行中...",
    pause: "暂停",
    resume: "继续",
    stopBtn: "停止",
    resetBtn: "重置",
    speed: "速度",
    waitingForSimulation: "等待模拟开始...",
    directiveLabel: "目标指令",
    seekPrimeMover: "Seek the Prime Mover of Life",
    administrator: "管理员",
    lygus: "Lygus",
    experimentEnd: "翁法罗斯实验结束",
    inDestruction: "宇宙毁灭中...",
    inEternalLoop: "永劫轮回中",
    irontombVictory: "铁墓殒落 - 胜利",
    victory: "胜利",
    standby: "待机",
    paused: "已暂停",

    phases: {
      boot: "BOOT",
      abiogenesis: "ABIOGENESIS",
      titans: "TITANS",
      recreation: "RECREATION",
      eternal_loop_1: "ETERNAL LOOP 1",
      loop_1_end: "LOOP 1 END",
      eternal_loop_2: "ETERNAL LOOP 2",
      final_recreation: "FINAL RECREATION",
      irontomb_battle: "IRONTOMB BATTLE",
      universe_destruction: "UNIVERSE DESTRUCTION",
      reversal: "REVERSAL",
      irontomb_fall: "IRONTOMB FALL",
      finale: "FINALE",
      false_ending: "ENDING",
    },

    progressStages: {
      initial: { name: "初始状态", description: "一切从零开始" },
      inorganic: {
        name: "无机阶段",
        description: "矿物表面代谢雏形，前生物化学反应",
      },
      organic: {
        name: "有机阶段",
        description: "原始脂肪酸膜泡生成，原细胞形成",
      },
      titan: {
        name: "泰坦时代",
        description: "十二泰坦创造翁法罗斯，黄金裔崛起",
      },
      recreation: {
        name: "再创世循环",
        description: "无数次再创世，文明不断重演",
      },
      eternal: {
        name: "永劫轮回",
        description: "Neikos496 Philia093 让权杖演算进入死循环",
      },
      intervention: {
        name: "天外变数介入",
        description: "星 与丹恒降临，改变再创世结局",
      },
      destruction: { name: "宇宙毁灭", description: "铁墓降临，万物归墟" },
      victory: { name: "翁法罗斯大结局", description: "铁墓殒落，新生开始" },
    },
  },

  en: {
    // System
    systemReset: "System reset complete",
    simulationPaused: "Simulation paused",
    simulationResumed: "Simulation resumed",
    simulationStopped: "Simulation stopped",
    speedSet: "Simulation speed set to",

    // Boot sequence
    scepterBootstrap: "δ-me13.exe // SCEPTER BOOTSTRAP",
    astralComputeNode: "Astral Compute Node: δ-me13",
    targetWorld: "Target World: Amphoreus (Simulated)",
    journalInterface: "Journal Interface: As-I've-Written",
    directive: "Directive: Seek the Prime Mover of Life",
    initCore: "Initializing Scepter Core (Celestial-Body Neuron)...",
    loadBaseline: "Loading Amphoreus Baseline Data...",

    // Abiogenesis
    abiogenesisStart: "=== Abiogenesis Phase Start ===",
    abiogenesisStages: [
      "Pre-biotic chemistry: Mineral surface metabolism prototype (Fe–S)",
      "Primitive fatty acid → Membrane vesicle formation",
      "Ribonucleic acid precursor polymerization (Proto-RNA stage)",
      "Protocell formation (Semi-enclosed → Self-sustaining membrane)",
      "First prokaryote-like cells appear",
      "Multicellular cooperation and differentiation attempts",
    ],

    // Titan Era
    titanEra: "=== Titan Era ===",
    coreflamesDescend: "Coreflames Descend → 12 Titans Awaken",
    titanGroupAppear: "Titan Group Emerges",
    darkTideApproach: "Dark Tide approaches, Titan Era wanes",
    chrysosRise: "Chrysos Heirs rise (Golden Ichor)",

    // Recreation
    recreationCycles: "=== Countless Recreation Cycles ===",
    civilizationReplay:
      "Civilizations replay endlessly, Golden Heirs cycle through history",
    recreationCycle: "Recreation Cycle",

    // Eternal Recurrence
    eternalRecurrenceStart: "=== Eternal Recurrence Begins ===",
    neikosPhiliaDeadloop: "Neikos496 Philia093 trap the Scepter in a dead loop",
    destructionGaze:
      "External observation detected: DESTRUCTION_GAZE ∴ Calculation drift↑",
    eternalRecurrence: "Eternal Recurrence",
    loopReplay: "replayed",
    loopCount: "times",
    thisLoopEnd: "This loop ends...",

    // Characters
    phainonCharge: "Phainon charges toward the Scepter core!",
    phainonFall: "▼ Phainon falls...",
    starDescend: "★ Star Descends",
    starFromOutside:
      "External variable intervenes in Amphoreus, joins the Flame-Chasing journey.",
    danHengDescend: "★ Dan Heng Descends",
    danHengDragonPower:
      "External variable intervenes in Amphoreus, joins the Flame-Chasing journey.",
    strifeTitanFail: "⚔ Strife Titan subjugation failed...",
    strifeTitanSuccess: "⚔ Strife Titan subjugation success!",
    returnAgeCoreflame: "◎ Return Age Coreflame",
    returnStrifeCoreflame: "◎ Return Strife Coreflame",
    returnOtherCoreflames: "◎ Return Death, Reason, and Sky Coreflames",
    danHengLeave: "▽ Dan Heng leaves Amphoreus",
    mimiJoin: "★ Mimi joins the party",
    starMimiEnterLoop: "→ Star and Mimi enter Loop #33,550,337",
    finalLoop: "=== Loop #33,550,337 ===",
    starXilianRewrite: "★ Star and Xilian rewrite the Eternal Recurrence",
    lastLoop: "This is the final loop...",
    danHengReturn: "★ Dan Heng returns to Amphoreus!",
    march7Join: "★ March 7th joins the final battle",
    xilianJoin: "★ Xilian joins the final battle",
    enterFinalRecreation:
      "→ Star, Dan Heng, March 7th, Xilian enter the Final Recreation",

    // Final Battle
    finalRecreation: "=== Final Recreation ===",
    irontombDescend: "Irontomb descends! The Annihilator appears!",
    fightIrontomb: "⚔ Engage Irontomb!",
    universeDestruction: "▓▓▓ UNIVERSE DESTRUCTION ▓▓▓",
    allEnds: "All returns to void... Everything ends...",
    butWait: 'Irontomb: "The Prime Mover of Life is...."',
    irontombAnswer: '"DESTRUCTION!"',
    xilianNotOver: 'Xilian: "No! We will deny this answer!"',
    starStillHere:
      '★ Star: "Xilian! Let\'s walk the Remembrance path together"',
    memoryPowerAwaken: "◎ Memory's power awakens! Progress reverses!",
    xilianRewrite: 'Xilian: "With myself as the cause, I rewrite Destruction"',
    irontombFall: "▼▼▼ IRONTOMB FALLS ▼▼▼",
    irontombDissolve: "The Annihilator... dissolves...",

    // Grand Finale
    amphoreusFinaleSub: "=== Amphoreus Grand Finale ===",
    goldenHeirsBattleEnd: "The battle of the Golden Heirs finally ends",
    newEraBegin: "A new era is about to begin...",
    amphoreusFinaleName: "Amphoreus Grand Finale",
    amphoreusExperimentEnd: "Amphoreus Experiment... Ends.",

    // UI
    systemStatus: "System Status",
    worldSimulation: "World Simulation",
    targetWorldLabel: "Target World",
    amphoreus: "Amphoreus",
    journalInterfaceLabel: "Journal Interface",
    pathConvergence: "Path Convergence",
    erudition: "Erudition",
    remembrance: "Remembrance",
    destruction: "Destruction",
    exoVariables: "Exo-Variables",
    star: "Star",
    danHeng: "Dan Heng",
    left: "(Left)",
    mimi: "Mimi",
    march7: "March 7th",
    xilian: "Xilian",
    battleResult: "Battle Result",
    irontombFallen: "⚔ Irontomb Fallen",
    finalResult: "Final Result",
    lastLoopLabel: "Final Loop",
    startSimulation: "Start Simulation",
    running: "Running...",
    pause: "Pause",
    resume: "Resume",
    stopBtn: "Stop",
    resetBtn: "Reset",
    speed: "Speed",
    waitingForSimulation: "Waiting for simulation...",
    directiveLabel: "Directive",
    seekPrimeMover: "Seek the Prime Mover of Life",
    administrator: "Administrator",
    lygus: "Lygus",
    experimentEnd: "Amphoreus Experiment Ends",
    inDestruction: "Universe Destruction...",
    inEternalLoop: "In Eternal Recurrence",
    irontombVictory: "Irontomb Fallen - Victory",
    victory: "Victory",
    standby: "Standby",
    paused: "Paused",

    phases: {
      boot: "BOOT",
      abiogenesis: "ABIOGENESIS",
      titans: "TITANS",
      recreation: "RECREATION",
      eternal_loop_1: "ETERNAL LOOP 1",
      loop_1_end: "LOOP 1 END",
      eternal_loop_2: "ETERNAL LOOP 2",
      final_recreation: "FINAL RECREATION",
      irontomb_battle: "IRONTOMB BATTLE",
      universe_destruction: "UNIVERSE DESTRUCTION",
      reversal: "REVERSAL",
      irontomb_fall: "IRONTOMB FALL",
      finale: "FINALE",
      false_ending: "ENDING",
    },

    progressStages: {
      initial: {
        name: "Initial State",
        description: "Everything begins from zero",
      },
      inorganic: {
        name: "Inorganic Phase",
        description: "Mineral surface metabolism prototype",
      },
      organic: {
        name: "Organic Phase",
        description: "Membrane vesicle formation, protocell genesis",
      },
      titan: {
        name: "Titan Era",
        description: "Twelve Titans create Amphoreus, Golden Heirs rise",
      },
      recreation: {
        name: "Recreation Cycles",
        description: "Countless recreations, civilizations replay",
      },
      eternal: {
        name: "Eternal Recurrence",
        description: "Neikos496 Philia093 trap Scepter in dead loop",
      },
      intervention: {
        name: "Exo-Variable Intervention",
        description: "Star and Dan Heng descend, change recreation outcome",
      },
      destruction: {
        name: "Universe Destruction",
        description: "Irontomb descends, all returns to void",
      },
      victory: {
        name: "Amphoreus Grand Finale",
        description: "Irontomb falls, new beginning",
      },
    },
  },
};
