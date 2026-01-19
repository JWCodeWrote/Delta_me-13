# δme-13 - Scepter Simulation

## 项目描述

这是一个模拟 δme-13（权杖 δ-me13）的程序，实现了翁法罗斯模拟在权杖上以「周期」重复运行的机制。基于《崩坏：星穹铁道》翁法罗斯篇章的设定。

## 版本

### 🌐 网页版（推荐）

现代化的可视化界面，具有科幻风格的仪表板。

**特点：**

- 无限符号 (∞) 进度指示器
- 红/橙交替闪烁的永劫轮回效果
- 完整剧情流程（33,550,336 → 33,550,337 次轮回）
- 铁墓迎击 → 宇宙毁灭 → 逆转 → 大结局
- 简体中文/英文双语切换
- 实时日志显示（As I've Written）

### 🐍 命令行版

原始的 Python CLI 版本，纯文本输出。

## 快速开始

### 从 GitHub Clone

```bash
# 克隆仓库
git clone https://github.com/JWCodeWrote/Delta_me-13.git
cd Delta_me-13
```

### 网页版

```bash
# 方法 1：一键启动（Windows，自动安装依赖）
start.bat

# 方法 2：手动启动
cd frontend
npm install      # 首次需要安装依赖
npm run dev      # 启动开发服务器
```

然后在浏览器打开 http://localhost:5173/

### 命令行版

```bash
# 方法 1：批处理（Windows）
cd cli
run_python.bat

# 方法 2：直接运行
cd cli
python delta_me13_sim.py
```

## 系统要求

| 版本     | 要求                              |
| -------- | --------------------------------- |
| 网页版   | Node.js 18+                       |
| 命令行版 | Python 3.9+                       |
| 系统     | Windows（使用 .bat）/ Mac / Linux |

## 剧情流程

```
生命起源 (0-40%)
    ↓
泰坦时代 (40-60%)
    ↓
再创世循环 (60-80%)
    ↓
永劫轮回 #33,550,336 (99.07%) ← Neikos496 Philia093 死循环
    ↓
星/丹恒降临 → 丹恒离开
    ↓
永劫轮回 #33,550,337 (最后一次)
    ↓
星、丹恒、三月七、昔涟 进入最后的再创世
    ↓
迎击铁墓 → 宇宙毁灭 (红色 100%)
    ↓
昔涟/星 逆转时间 → 铁墓殒落
    ↓
翁法罗斯大结局 (粉色 100%)
    ↓
! (结束)
```

## 十二泰坦

| 分类 | 泰坦名称                                                      |
| ---- | ------------------------------------------------------------- |
| 创世 | Kephale（刻法勒）、Mnemeta（墨涅塔）、Sersis（瑟希斯）        |
| 天命 | Olorus（欧洛尼斯）、Tarandton（塔兰顿）、Janus（雅努斯）      |
| 灾祸 | Nikador（尼卡多利）、Zagreus（扎格列斯）、Senatos（塞纳托斯） |
| 支柱 | Gioria（吉奥里亚）、Fagiana（法吉娜）、Aigle（艾格勒）        |

## 项目结构

```
δme-13/
├── frontend/               # 网页版 (Vue 3 + TypeScript)
│   ├── src/
│   │   ├── App.vue         # 主组件
│   │   ├── composables/
│   │   │   ├── useAmphoreus.ts  # 模拟逻辑
│   │   │   └── i18n.ts     # 多语言
│   │   └── style.css       # 样式
│   └── package.json
├── cli/                    # 命令行版 (Python)
│   ├── delta_me13_sim.py   # 主程序
│   └── run_python.bat      # Python 启动器
├── start.bat               # 网页版启动器
├── .gitignore              # Git 忽略文件
└── README.md
```

## 游戏背景

此程序基于《崩坏：星穹铁道》翁法罗斯篇章：

| 术语            | 说明                                 |
| --------------- | ------------------------------------ |
| 翁法罗斯        | 由权杖 δ-me13 模拟的世界             |
| δ-me13          | 智识星神 Nous 的星体神经元转化的权杖 |
| As I've Written | 如我所书，记事接口                   |
| Irontomb        | 铁墓，毁灭令使                       |
| 黄金裔          | 拥有融金血的特殊存在                 |
| 33,550,336      | 永劫轮回的总次数                     |

## 注意事项

- Clone 后首次运行网页版需要安装依赖（`npm install`）
- `start.bat` 会自动检测并安装依赖
- Mac/Linux 用户请手动运行 npm 命令
- Python 版本使用标准库，无需额外安装依赖

## License

MIT
