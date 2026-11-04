# PS2 Exercise 3 — collaboration setup

<!-- PS2_FINAL_TEAM_PLAN_START -->
## PS2 最终分工与前置顺序

本组完成第 1、2、3、5 题。A-E 为成员占位，确认后替换姓名。第 1、5 题沿用 PS1 的 Conda；第 2、3 题使用 Pixi，各题不要求统一环境工具。

### 仓库与环境

| 题目 | 小组仓库 | 环境安排 |
| --- | --- | --- |
| 第1题 | [first_repo](https://github.com/zcyMary/first_repo) | 沿用 PS1 的 Conda，补充检查工具 |
| 第2题 | [Smoking](https://github.com/starries-creator/ps_2_ex2_smoking_is_bad) | Pixi，环境名 `smoke` |
| 第3题 | [NBA](https://github.com/starries-creator/ps_2_ex3_database) | 沿用老师的 Pixi 配置，Python 3.12，环境名 `nba` |
| 第5题 | [Titanic](https://github.com/starries-creator/ps1_ex4_nb_to_repo_forked) | 沿用 Conda，Python 3.13.16、pandas 2.3 |

### 成员分工

| 成员 | 第1题 | 第2题 | 第3题 | 第5题 |
| --- | --- | --- | --- | --- |
| **A** | pre-commit、flake8、mypy 配置 | 变量分布图与解释 | 洞见① | 整合报告及 README |
| **B** | 忽略规则、CSV 跟踪验证 | **优先配置环境**，完善锁文件、README、nbstripout | 洞见② | 年龄、票价分析 |
| **C** | 第一组函数类型标注 | 数据清理、TODO、总体生存率 | **准备数据与表结构**，完成打包及加载模块解释 | 家庭变量分析 |
| **D** | 第二组函数类型标注 | 分组生存率比较＋整合 notebook | 洞见③ | 性别、舱位分析 |
| **E** | mypy 依赖验证，结合 B 的结果回答两问 | 年龄分组敏感性检查 | 洞见④＋整合 notebook | 缺失值与变量可用性 |

### 前置顺序

箭头表示先后；【并行】内的工作可同时开展。

#### 第1题：并行准备，再汇合验收

**同步仓库、确认旧 Conda 环境 →【并行：A 配置检查规则｜B 忽略规则/CSV 验证｜C/D 两组类型标注｜E 验证与记录】→ 类型标注 PR 审查并合并（推荐先）→ A 同步最新代码并运行全文件检查 → 按责任修正、复查通过 → 工具配置 PR 审查并合并 → 各人同步并安装 hooks**

B 的忽略规则 PR 可独立审查合并。E 在 A 的规则可用后验证 mypy，并结合 B 的记录完成答案。类型问题由 C/D 修正，配置与格式问题由 A 协调。三类 PR 分开，各需两名非作者 review 并批准；最终检查需规则与标注齐备。

#### 第2题：环境先行，分析并行

**B 配好 Pixi smoke 环境、锁文件和 README → C 清理并准备数据 →【并行：A 变量分布｜D 分组生存率｜E 年龄分组敏感性】→ 各自交齐代码、图表和解释 → D 整合 notebook、复跑检查**

nbstripout 配置可与准备和分析并行完善；提交前各成员在自己的 clone 安装 hook。

#### 第3题 NBA：数据可读后并行，最后整合

**本机数据库可读、路径及所需表/列明确 →【并行：A 洞见①｜B 洞见②｜D 洞见③｜E 洞见④｜C 打包｜共同认领 warm-up】→ 四条洞见交齐，且打包/函数导入验证通过 → E 接入 analysis.ipynb → 从头复跑、修正并审查**

C 优先提供数据获取、连接和表结构说明；其他人若已自行验证数据可读，也可开始。选题讨论可与数据准备并行。无需先完善整份 warm_up.ipynb、pyproject.toml 或最终 analysis.ipynb；打包和导入验证是最终整合条件，不是开工门槛。

#### 第5题：环境确认后并行分析

**各自确认原 Conda 环境可用 →【并行：B 年龄/票价｜C 家庭变量｜D 性别/舱位｜E 缺失值/变量可用性】→ 各自交齐代码、图表和解释 → A 整合报告及 README → 复跑、审查与修正**

报告≤500词，不含图。README 补充可视化及运行说明，同时保留原项目说明。

### 交付与协作

各作者交齐自己的代码、必要图表和简短解释；第3题每条洞见还需包含查询和相关函数。整合者负责接入、复跑和统一格式。通过分支和 PR 协作，开工前划清函数、文件和 notebook 修改范围。

作业占位文件和原 notebook 中的 TODO 由对应成员完成；本次只同步分工及操作说明，不预填分析、答案或报告。
<!-- PS2_FINAL_TEAM_PLAN_END -->

## Start here

The PS2 setup uses Python 3.12 and a committed lock file. Four platforms are
resolved: macOS Apple Silicon, macOS Intel, Linux x86-64, and Windows x86-64.
Runtime validation is performed on macOS Apple Silicon; other platforms are
dependency-resolved, not runtime-tested. Install Pixi from https://pixi.sh/ .

From the repository root:

```bash
pixi install --locked -e nba
pixi run -e nba jupyter
```

Use the Python kernel from that environment. Do not use a global Python or a
teammate's absolute environment path. Other CPU architectures require a team
manifest/lock update first. See [CONTRIBUTING.md](CONTRIBUTING.md) for branches,
reviews, notebook editing, and local-file rules.

## Files and unfinished coursework

- `warm_up.ipynb`, `nba/data_loader.py`, `.pre-commit-config.yaml`: original teaching material, unchanged.
- `nba/wrangling.py`, `nba/visualisation.py`: intentionally EMPTY function modules.
- `queries/insight_1.sql` through `insight_4.sql`: intentionally EMPTY query files.
- `analysis.ipynb`: valid empty notebook for the final four-or-more insights.
- `docs/data_loader_notes.md`: intentionally EMPTY explanations.
- `pyproject.toml`: intentionally EMPTY coursework placeholder; the package is NOT yet installable.
- `figures/` and `data/`: final exports and local downloaded data respectively.

Run commands from the repository root until packaging is completed. The existing
`pixi.toml` works independently of the empty `pyproject.toml`; do not run `pip install -e .`
until the packaging owner completes it. Each insight author supplies their query,
appropriate figure, modular functions, and explanation. The integrator assembles
them in `analysis.ipynb`. No NBA analysis or data download is performed by this setup.

The original hook configuration is provided upstream. Each member can install it with
`pixi run -e nba pre-commit install`; existing coursework may require fixes before
all hooks pass. Do not confuse environment verification with assignment completion.
Keep each member's Kaggle token local and never commit or paste it into PRs.


## Setup verification

Verified on 2026-11-03 with Python 3.12.16 on macOS Apple Silicon.
Checks passed: notebook valid: warm_up.ipynb; notebook valid: analysis.ipynb; headless PNG rendering; SQLite/DuckDB in-memory queries and empty package modules import; original loader --help and provided hook configuration validate; no credentials used; fresh Jupyter kernel executes disposable Python/pandas cell.
Other platforms were lock-resolved only. No coursework analysis, answers,
model training, or Kaggle data download was performed.

## Original repository instructions (retained)

# PS 2 Ex 3

# Setup

## Environment

This project uses [Pixi](https://pixi.sh) for the environment. Install Pixi if you
do not have it yet, then from the repository root run:

```bash
pixi install
```

Activate the environment by running:

```bash
pixi shell
```

You can also run commands without activating the shell, for example
`pixi run python nba/data_loader.py ...`.

## Pre-commit

This repository uses pre-commit to run some checks before each commit. To install pre-commit, run:

```bash
pixi run pre-commit install
```

To run the checks manually, run:

```bash
pixi run pre-commit run --all-files
```

# Getting the data

1. create a Kaggle account: https://www.kaggle.com/
2. get API keys and user name
   - Go to your account, and click on your profile in the top right
   - Then click on "Settings"
   - Scroll down to the API section and click on "Create New Token"
   - Get your username and API key from there

We have written a data loader function for you in the "nba/data_loader.py".This allows you to
download the data with by running the script from the terminal. Run the following command in the
terminal being at the root of the repository.

```bash
pixi run python nba/data_loader.py -u "your_user_name" -k "your_api_key" -d "wyattowalsh/basketball"
```

Replace "your_user_name" and "your_api_key" with your username and API key. This creates a json
file at "~/.kaggle/kaggle.json" with your username and API key, which is used to authenticate your
account and download the data.
