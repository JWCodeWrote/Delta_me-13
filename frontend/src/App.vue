<script setup lang="ts">
import { useAmphoreus } from "./composables/useAmphoreus";
import { computed } from "vue";

const {
  currentLanguage,
  t,
  setLanguage,
  currentProgress,
  eternalLoopCount,
  currentLoopNumber,
  isRunning,
  isPaused,
  simulationSpeed,
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
  currentStage,
  themeColor,
  infinityProgress,
  TOTAL_ETERNAL_LOOPS,
  FINAL_LOOP,
  startSimulation,
  togglePause,
  stop,
  reset,
  setSpeed,
  closeEnding,
} = useAmphoreus();

// 格式化数字
const formatNumber = (n: number) => n.toLocaleString("zh-CN");

// 无限符号路径
const infinityPath =
  "M 50,100 C 50,50 100,50 150,100 C 200,150 250,150 250,100 C 250,50 200,50 150,100 C 100,150 50,150 50,100";

// 计算无限符号上的点位置
const infinityPoint = computed(() => {
  const t = infinityProgress.value * Math.PI * 2;
  const scale = 1;
  const x = 150 + 100 * Math.sin(t) * scale;
  const y = 100 + 50 * Math.sin(2 * t) * scale;
  return { x, y };
});

// 日志颜色
const getLogColor = (type: string) => {
  switch (type) {
    case "error":
      return "var(--color-red-destruction)";
    case "warning":
      return "var(--color-gold)";
    case "success":
      return "var(--color-green-organic)";
    case "system":
      return "var(--color-cyan-memory)";
    case "destruction":
      return "#ff4444";
    case "victory":
      return "#ff69b4";
    default:
      return "var(--color-gray)";
  }
};

// 当前显示的轮回次数
const displayLoopCount = computed(() => {
  if (currentLoopNumber.value === 2) {
    return FINAL_LOOP;
  }
  return eternalLoopCount.value;
});

// 切换语言
function toggleLanguage() {
  setLanguage(currentLanguage.value === "zh-CN" ? "en" : "zh-CN");
}
</script>

<template>
  <div
    class="dashboard"
    :class="{
      'destruction-mode': isDestructionPhase,
      'victory-mode': isVictoryPhase,
      'false-ending': showFalseEnding,
      flashing:
        isFlashing &&
        eternalLoopStarted &&
        !isVictoryPhase &&
        !isDestructionPhase,
    }"
  >
    <!-- 结局覆盖层 - 只显示 ! 不显示 FALSE -->
    <div
      v-if="showFalseEnding"
      class="false-ending-overlay"
      :style="{ opacity: falseEndingOpacity }"
    >
      <div class="false-symbol" :class="{ blink: falseEndingOpacity >= 1 }">
        !
      </div>
      <div class="false-subtitle">{{ t.amphoreusExperimentEnd }}</div>
      <button
        v-if="falseEndingOpacity >= 1"
        class="close-ending-btn"
        @click="closeEnding"
      >
        {{ currentLanguage === "zh-CN" ? "关闭" : "Close" }}
      </button>
    </div>

    <!-- 顶部标题列 -->
    <header class="header glass-panel">
      <div class="header-left">
        <span class="scepter-icon">⚜</span>
        <h1 class="gold-text">SCEPTER δ-me13</h1>
      </div>
      <div class="header-center">
        <span
          class="status-indicator"
          :class="{
            active: isRunning && !isDestructionPhase,
            paused: isPaused,
            destruction: isDestructionPhase,
            victory: isVictoryPhase,
          }"
        ></span>
        <span>{{
          showFalseEnding
            ? "!"
            : isVictoryPhase
              ? t.victory
              : isDestructionPhase
                ? t.inDestruction
                : isRunning
                  ? isPaused
                    ? t.paused
                    : t.running
                  : t.standby
        }}</span>
      </div>
      <div class="header-right">
        <button class="lang-btn" @click="toggleLanguage">
          {{ currentLanguage === "zh-CN" ? "EN" : "中" }}
        </button>
        <span class="phase-label" :class="{ danger: isDestructionPhase }">
          {{
            t.phases[currentPhase as keyof typeof t.phases] ||
            currentPhase.toUpperCase()
          }}
        </span>
      </div>
    </header>

    <!-- 主内容区 -->
    <main class="main-content">
      <!-- 左侧面板 -->
      <aside class="left-panel glass-panel">
        <h2>{{ t.systemStatus }}</h2>

        <div class="status-section">
          <h3>{{ t.worldSimulation }}</h3>
          <div class="status-item">
            <span>{{ t.targetWorldLabel }}</span>
            <span class="gold-text">{{ t.amphoreus }}</span>
          </div>
          <div class="status-item">
            <span>{{ t.journalInterfaceLabel }}</span>
            <span>As-I've-Written</span>
          </div>
        </div>

        <div class="status-section">
          <h3>{{ t.pathConvergence }}</h3>
          <div class="path-indicators">
            <div class="path-item erudition">
              <span class="path-dot"></span>
              <span>{{ t.erudition }}</span>
            </div>
            <div class="path-item remembrance">
              <span class="path-dot"></span>
              <span>{{ t.remembrance }}</span>
            </div>
            <div class="path-item destruction">
              <span class="path-dot"></span>
              <span>{{ t.destruction }}</span>
            </div>
          </div>
        </div>

        <div class="status-section">
          <h3>{{ t.exoVariables }}</h3>
          <div class="exo-status">
            <div class="exo-item" :class="{ arrived: starArrived }">
              <span class="exo-dot"></span>
              <span>{{ t.star }}</span>
            </div>
            <div
              class="exo-item"
              :class="{ arrived: danHengArrived, left: danHengLeft }"
            >
              <span class="exo-dot"></span>
              <span>{{ t.danHeng }} {{ danHengLeft ? t.left : "" }}</span>
            </div>
            <div class="exo-item" :class="{ arrived: mimiArrived }">
              <span class="exo-dot"></span>
              <span>{{ t.mimi }}</span>
            </div>
            <div class="exo-item" :class="{ arrived: march7Arrived }">
              <span class="exo-dot"></span>
              <span>{{ t.march7 }}</span>
            </div>
            <div class="exo-item" :class="{ arrived: xilianArrived }">
              <span class="exo-dot"></span>
              <span>{{ t.xilian }}</span>
            </div>
          </div>
        </div>

        <div class="status-section" v-if="irontombDefeated">
          <h3>{{ t.battleResult }}</h3>
          <div class="battle-result victory">
            <span>{{ t.irontombFallen }}</span>
          </div>
        </div>
      </aside>

      <!-- 中央区域 -->
      <section class="center-panel">
        <!-- 无限符号进度指示器 -->
        <div
          class="infinity-container"
          :class="{
            glitch:
              eternalLoopStarted && !simulationComplete && !isVictoryPhase,
            destruction: isDestructionPhase,
            victory: isVictoryPhase,
            flashing:
              isFlashing &&
              eternalLoopStarted &&
              !isVictoryPhase &&
              !isDestructionPhase,
          }"
        >
          <svg class="infinity-svg" viewBox="0 0 300 200">
            <path
              class="infinity-bg"
              :d="infinityPath"
              fill="none"
              stroke="rgba(255,255,255,0.1)"
              stroke-width="6"
              stroke-linecap="round"
            />
            <path
              class="infinity-progress"
              :d="infinityPath"
              fill="none"
              :stroke="themeColor"
              stroke-width="6"
              stroke-linecap="round"
              :stroke-dasharray="600"
              :stroke-dashoffset="600 - (currentProgress / 100) * 600"
            />
            <circle
              v-if="eternalLoopStarted && !simulationComplete"
              class="infinity-dot"
              :cx="infinityPoint.x"
              :cy="infinityPoint.y"
              r="8"
              :fill="themeColor"
            />
            <text
              x="150"
              y="105"
              text-anchor="middle"
              class="infinity-symbol-text"
              :fill="themeColor"
            >
              ∞
            </text>
          </svg>

          <div class="infinity-info">
            <div class="progress-value" :style="{ color: themeColor }">
              {{ currentProgress.toFixed(2) }}%
            </div>
            <div
              class="stage-name"
              :class="{
                destruction: isDestructionPhase,
                victory: isVictoryPhase,
              }"
            >
              {{ currentStage.name }}
            </div>
            <div class="stage-desc">{{ currentStage.description }}</div>
          </div>
        </div>

        <!-- 永劫轮回计数器 -->
        <div
          v-if="eternalLoopStarted"
          class="eternal-counter glass-panel"
          :class="{
            complete: simulationComplete,
            destruction: isDestructionPhase,
            victory: isVictoryPhase,
            flashing: isFlashing && !isVictoryPhase && !isDestructionPhase,
          }"
        >
          <div class="counter-label">
            {{ isVictoryPhase ? t.finalResult : t.eternalRecurrence }}
          </div>
          <div class="counter-value">
            <span class="counter-current"
              >{{ currentLanguage === "zh-CN" ? "第" : "#" }}
              {{ formatNumber(displayLoopCount) }}
              {{ currentLanguage === "zh-CN" ? "次" : "" }}</span
            >
          </div>
          <div v-if="currentLoopNumber === 2" class="counter-note">
            {{ t.lastLoopLabel }}
          </div>
          <div class="counter-progress">
            <div
              class="progress-bar"
              :class="{
                destruction: isDestructionPhase,
                victory: isVictoryPhase,
                flashing: isFlashing && !isVictoryPhase && !isDestructionPhase,
              }"
            >
              <div
                class="progress-bar-fill"
                :style="{
                  width: (displayLoopCount / FINAL_LOOP) * 100 + '%',
                  background: isDestructionPhase
                    ? 'linear-gradient(90deg, #8b0000, #ff4444, #ff6666)'
                    : isVictoryPhase
                      ? 'linear-gradient(90deg, #ff1493, #ff69b4, #ffb6c1)'
                      : isFlashing
                        ? 'linear-gradient(90deg, #8b0000, #ff4500, #ff6600)'
                        : 'linear-gradient(90deg, #8b0000, #c0392b, #e74c3c)',
                }"
              ></div>
            </div>
          </div>
        </div>

        <!-- 控制按钮 -->
        <div class="controls">
          <button
            class="btn btn-primary"
            @click="startSimulation"
            :disabled="isRunning && !isPaused"
          >
            {{ isRunning ? t.running : t.startSimulation }}
          </button>

          <button class="btn" @click="togglePause" :disabled="!isRunning">
            {{ isPaused ? t.resume : t.pause }}
          </button>

          <button class="btn btn-danger" @click="stop" :disabled="!isRunning">
            {{ t.stopBtn }}
          </button>

          <button class="btn" @click="reset">
            {{ t.resetBtn }}
          </button>

          <div class="speed-control">
            <span>{{ t.speed }}:</span>
            <button
              v-for="speed in [1, 2, 5, 10]"
              :key="speed"
              class="speed-btn"
              :class="{ active: simulationSpeed === speed }"
              @click="setSpeed(speed)"
            >
              {{ speed }}x
            </button>
          </div>
        </div>
      </section>

      <!-- 右侧面板 -->
      <aside class="right-panel glass-panel">
        <h2>As I've Written</h2>
        <div class="log-container">
          <div
            v-for="(log, index) in logs"
            :key="index"
            class="log-entry"
            :style="{ color: getLogColor(log.type) }"
          >
            <span class="log-time">[{{ log.timestamp }}]</span>
            <span class="log-message">{{ log.message }}</span>
          </div>
          <div v-if="logs.length === 0" class="log-empty">
            {{ t.waitingForSimulation }}
          </div>
        </div>
      </aside>
    </main>

    <!-- 底部状态列 -->
    <footer class="footer glass-panel">
      <div class="footer-item">
        <span>{{ t.directiveLabel }}:</span>
        <span class="gold-text">{{ t.seekPrimeMover }}</span>
      </div>
      <div class="footer-item" v-if="adminVisible">
        <span>{{ t.administrator }}:</span>
        <span>{{ t.lygus }}</span>
      </div>
      <div class="footer-item">
        <span v-if="showFalseEnding" class="victory-text"
          >! - {{ t.experimentEnd }}</span
        >
        <span v-else-if="irontombDefeated" class="victory-text"
          >✓ {{ t.irontombVictory }}</span
        >
        <span v-else-if="isDestructionPhase" class="destruction-text"
          >⚠ {{ t.inDestruction }}</span
        >
        <span v-else-if="eternalLoopStarted" class="error-text"
          >⚠ {{ t.inEternalLoop }}</span
        >
        <span v-else>{{ t.amphoreus }}</span>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.dashboard {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  padding: 16px;
  gap: 16px;
  transition: all 0.3s ease;
}

.dashboard.destruction-mode {
  background: linear-gradient(135deg, #1a0505 0%, #2d0a0a 50%, #0d0202 100%);
}

.dashboard.victory-mode {
  background: linear-gradient(135deg, #1a0510 0%, #2d0a1a 50%, #0d0207 100%);
}

.dashboard.flashing {
  animation: bgFlash 0.3s infinite alternate;
}

@keyframes bgFlash {
  from {
    background: linear-gradient(135deg, #1a0505 0%, #2d0a0a 50%, #0d0202 100%);
  }
  to {
    background: linear-gradient(135deg, #1a0a00 0%, #2d1500 50%, #0d0500 100%);
  }
}

/* ═══ 结局覆盖层 ═══ */
.false-ending-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.95);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  transition: opacity 0.5s ease;
}

.false-symbol {
  font-size: 250px;
  color: #ff4444;
  font-weight: bold;
  text-shadow:
    0 0 50px rgba(255, 68, 68, 0.8),
    0 0 100px rgba(255, 68, 68, 0.5);
}

.false-symbol.blink {
  animation: symbolBlink 1s infinite;
}

@keyframes symbolBlink {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0.3;
  }
}

.false-subtitle {
  font-size: 18px;
  color: var(--color-gray);
  margin-top: 40px;
}

.close-ending-btn {
  margin-top: 60px;
  padding: 12px 40px;
  background: transparent;
  border: 2px solid var(--color-gray);
  color: var(--color-gray);
  font-size: 16px;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.3s ease;
  animation: fadeIn 1s ease;
}

.close-ending-btn:hover {
  border-color: #ff4444;
  color: #ff4444;
  box-shadow: 0 0 20px rgba(255, 68, 68, 0.3);
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* ═══ 语言切换按钮 ═══ */
.lang-btn {
  padding: 4px 12px;
  background: transparent;
  border: 1px solid var(--color-gold);
  color: var(--color-gold);
  cursor: pointer;
  border-radius: 4px;
  font-size: 12px;
  margin-right: 12px;
  transition: all var(--transition-fast);
}

.lang-btn:hover {
  background: var(--color-gold);
  color: var(--color-blue-deep);
}

/* ═══ 顶部 ═══ */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.scepter-icon {
  font-size: 28px;
  color: var(--color-gold);
}

.header h1 {
  font-size: 20px;
  font-weight: 600;
  letter-spacing: 2px;
}

.header-center {
  display: flex;
  align-items: center;
  gap: 8px;
}

.header-right {
  display: flex;
  align-items: center;
}

.status-indicator {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--color-gray);
}

.status-indicator.active {
  background: var(--color-green-organic);
  box-shadow: 0 0 10px var(--color-green-organic);
  animation: pulse 1s infinite;
}

.status-indicator.paused {
  background: var(--color-gold);
  box-shadow: 0 0 10px var(--color-gold);
}

.status-indicator.destruction {
  background: #ff4444;
  box-shadow: 0 0 10px #ff4444;
  animation: pulse 0.5s infinite;
}

.status-indicator.victory {
  background: #ff69b4;
  box-shadow: 0 0 10px #ff69b4;
}

.phase-label {
  padding: 4px 12px;
  background: rgba(212, 175, 55, 0.2);
  border: 1px solid var(--color-gold);
  border-radius: 4px;
  font-size: 12px;
  letter-spacing: 1px;
}

.phase-label.danger {
  background: rgba(255, 68, 68, 0.2);
  border-color: #ff4444;
  color: #ff4444;
}

/* ═══ 主内容 ═══ */
.main-content {
  display: grid;
  grid-template-columns: 280px 1fr 320px;
  gap: 16px;
  flex: 1;
}

/* ═══ 左侧面板 ═══ */
.left-panel,
.right-panel {
  padding: 20px;
}

.left-panel h2,
.right-panel h2 {
  font-size: 14px;
  color: var(--color-gold);
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid rgba(212, 175, 55, 0.3);
}

.status-section {
  margin-bottom: 24px;
}

.status-section h3 {
  font-size: 12px;
  color: var(--color-gray);
  margin-bottom: 12px;
}

.status-item {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
  margin-bottom: 8px;
}

.path-indicators {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.path-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
}

.path-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.erudition .path-dot {
  background: var(--color-gold);
}
.remembrance .path-dot {
  background: var(--color-cyan-memory);
}
.destruction .path-dot {
  background: var(--color-red-destruction);
}

.exo-status {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.exo-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  opacity: 0.5;
  transition: all 0.3s ease;
}

.exo-item.arrived {
  opacity: 1;
}

.exo-item.left {
  opacity: 0.6;
  text-decoration: line-through;
}

.exo-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--color-gray);
  transition: all 0.3s ease;
}

.exo-item.arrived .exo-dot {
  background: #ff69b4;
  box-shadow: 0 0 10px #ff69b4;
}

.exo-item.left .exo-dot {
  background: var(--color-gray);
  box-shadow: none;
}

.battle-result {
  padding: 10px;
  border-radius: 4px;
  text-align: center;
  font-weight: bold;
}

.battle-result.victory {
  background: rgba(255, 105, 180, 0.2);
  border: 1px solid #ff69b4;
  color: #ff69b4;
}

/* ═══ 中央面板 ═══ */
.center-panel {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
}

.infinity-container {
  position: relative;
  width: 400px;
  height: 300px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.infinity-container.glitch {
  animation: glitch 0.5s infinite;
}

.infinity-container.destruction .infinity-svg {
  filter: drop-shadow(0 0 20px rgba(255, 68, 68, 0.8));
}

.infinity-container.victory .infinity-svg {
  filter: drop-shadow(0 0 20px rgba(255, 105, 180, 0.8));
}

.infinity-container.flashing .infinity-svg {
  animation: svgFlash 0.3s infinite alternate;
}

@keyframes svgFlash {
  from {
    filter: drop-shadow(0 0 20px rgba(192, 57, 43, 0.8));
  }
  to {
    filter: drop-shadow(0 0 20px rgba(255, 69, 0, 0.8));
  }
}

.infinity-svg {
  width: 100%;
  height: 200px;
  filter: drop-shadow(0 0 10px currentColor);
}

.infinity-progress {
  transition:
    stroke-dashoffset 0.5s ease,
    stroke 0.3s ease;
}

.infinity-dot {
  filter: drop-shadow(0 0 10px currentColor);
  animation: pulse 0.5s infinite;
}

.infinity-symbol-text {
  font-size: 60px;
  opacity: 0.3;
}

.infinity-info {
  text-align: center;
  margin-top: -20px;
}

.progress-value {
  font-size: 36px;
  font-weight: bold;
  transition: color 0.3s ease;
}

.stage-name {
  font-size: 18px;
  margin-top: 8px;
  transition: color 0.3s ease;
}

.stage-name.destruction {
  color: #ff4444;
}

.stage-name.victory {
  color: #ff69b4;
}

.stage-desc {
  font-size: 12px;
  color: var(--color-gray);
  margin-top: 4px;
  max-width: 300px;
}

/* ═══ 永劫轮回计数器 ═══ */
.eternal-counter {
  padding: 16px 24px;
  text-align: center;
  border-color: var(--color-red-destruction);
  transition: all 0.3s ease;
}

.eternal-counter.flashing {
  animation: counterFlash 0.3s infinite alternate;
}

@keyframes counterFlash {
  from {
    border-color: #c0392b;
    background: rgba(192, 57, 43, 0.1);
  }
  to {
    border-color: #ff4500;
    background: rgba(255, 69, 0, 0.1);
  }
}

.eternal-counter.destruction {
  border-color: #ff4444;
  background: rgba(255, 68, 68, 0.1);
}

.eternal-counter.victory {
  border-color: #ff69b4;
  background: rgba(255, 105, 180, 0.1);
}

.eternal-counter.complete {
  border-color: #ff69b4;
}

.counter-label {
  font-size: 12px;
  color: var(--color-red-destruction);
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: 8px;
}

.eternal-counter.victory .counter-label {
  color: #ff69b4;
}

.counter-value {
  font-family: var(--font-mono);
  font-size: 24px;
}

.counter-current {
  color: var(--color-gold);
}

.counter-note {
  font-size: 12px;
  color: var(--color-gold);
  margin-top: 4px;
}

.counter-progress {
  margin-top: 12px;
}

.progress-bar.flashing .progress-bar-fill {
  animation: barFlash 0.3s infinite alternate;
}

@keyframes barFlash {
  from {
    background: linear-gradient(90deg, #8b0000, #c0392b, #e74c3c);
  }
  to {
    background: linear-gradient(90deg, #8b2500, #ff4500, #ff6600);
  }
}

.progress-bar.destruction {
  background: rgba(255, 68, 68, 0.2);
}

.progress-bar.victory {
  background: rgba(255, 105, 180, 0.2);
}

/* ═══ 控制按钮 ═══ */
.controls {
  display: flex;
  gap: 12px;
  align-items: center;
  flex-wrap: wrap;
  justify-content: center;
}

.speed-control {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-left: 16px;
  font-size: 13px;
}

.speed-btn {
  padding: 4px 8px;
  background: transparent;
  border: 1px solid var(--color-gray);
  color: var(--color-gray);
  cursor: pointer;
  border-radius: 4px;
  font-size: 12px;
  transition: all var(--transition-fast);
}

.speed-btn.active,
.speed-btn:hover {
  border-color: var(--color-gold);
  color: var(--color-gold);
}

/* ═══ 右侧面板 ═══ */
.log-container {
  height: calc(100vh - 280px);
  overflow-y: auto;
  font-family: var(--font-mono);
  font-size: 11px;
  line-height: 1.6;
}

.log-entry {
  margin-bottom: 4px;
  word-break: break-word;
}

.log-time {
  color: var(--color-gray);
  margin-right: 8px;
}

.log-empty {
  color: var(--color-gray);
  font-style: italic;
}

/* ═══ 底部 ═══ */
.footer {
  display: flex;
  justify-content: space-between;
  padding: 12px 24px;
  font-size: 12px;
}

.footer-item {
  display: flex;
  gap: 8px;
}

.success-text,
.victory-text {
  color: #ff69b4;
}

.destruction-text {
  color: #ff4444;
  animation: pulse 0.5s infinite;
}

.error-text {
  color: var(--color-red-destruction);
}

/* ═══ 响应式 ═══ */
@media (max-width: 1200px) {
  .main-content {
    grid-template-columns: 1fr;
  }

  .left-panel,
  .right-panel {
    display: none;
  }
}
</style>
