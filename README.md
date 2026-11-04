# PS2 Exercise 3 — collaboration setup

<!-- PS2_FINAL_TEAM_PLAN_START -->
## PS2 最终分工与前置顺序

本组完成第1、2、3、5题，A-E为成员占位。第1、5题沿用PS1的Conda；第2、3题使用Pixi。整合、报告、复跑和过程检查均分配到人；只有最终验收不指定人员。

### 仓库与环境

| 题目 | 小组仓库 | 环境安排 |
| --- | --- | --- |
| 第1题 | [first_repo](https://github.com/zcyMary/first_repo) | 沿用PS1的Conda，补充检查工具 |
| 第2题 | [Smoking](https://github.com/starries-creator/ps_2_ex2_smoking_is_bad) | Pixi，环境名 smoke；B优先完成正式配置 |
| 第3题 | [NBA](https://github.com/starries-creator/ps_2_ex3_database) | 沿用老师的Pixi，Python 3.12，环境名 nba |
| 第5题 | [Titanic](https://github.com/starries-creator/ps1_ex4_nb_to_repo_forked) | 沿用Conda，Python 3.13.16、pandas 2.3 |

### 成员分工

| 成员 | 第1题 | 第2题 | 第3题 | 第5题 |
| --- | --- | --- | --- | --- |
| A | 工具配置、全文件检查、跟进工具PR；审查忽略及类型PR | 变量分布图与解释 | 洞见①；数据库结构小题 | 筛选最终图表，撰写≤500词报告正文 |
| B | 忽略规则、CSV验证、跟进忽略PR；审查工具PR | 优先完成Pixi smoke环境、锁文件、nbstripout及环境README | 洞见②；表清单小题；检查整合结果 | 年龄/票价分析；组装报告notebook、完善README、复跑及跟进合并 |
| C | data_cleaner.py类型标注；协调类型PR | 年龄分组敏感性分析；检查整合结果 | 优先完成数据入口；打包、loader说明及安装/导入验证 | 家庭变量分析；检查报告与整合结果 |
| D | data_loader.py、visualizer.py类型标注；审查忽略及工具PR | 数据准备、基础统计与总体生存率；整合notebook/README、复跑及跟进合并 | 洞见③；字段小题 | 性别/舱位分析 |
| E | 验证mypy依赖、完成两问说明；审查类型PR | 按年龄分组比较吸烟与生存率，解释混杂关系 | 洞见④；日期范围小题；整合notebook/README、复跑及跟进合并 | 缺失值与特征可用性分析 |

### 工作边界

- NBA四个洞见选择相近复杂度；A/B/D/E各自交付SQL、分析/绘图函数、图和解释，并修复自己的代码。C负责安装和导入，E负责汇总调用。
- 第5题优先复用已有分析和图；B/C/D/E各交图及简短解释，供A筛选和写作。报告正文≤500词，不含图。
- 检查人负责提出问题并复核，原作者负责修改；整合人负责组装、运行和协调。B优先完成第2题环境，C优先提供NBA可读数据入口。
- 各题通过分支和PR协作，开工前划清函数、文件及notebook修改范围。合并跟进人删除对应已合并的远程和本地分支；未合并分支保留。

### 前置顺序

箭头表示先后；【并行】内的工作可同时开展。各题最后的“最终验收”不指定人员。以下为组员后续完成作业的流程。

#### 第1题：沿用Conda，三个主要PR，工具PR最后

**【并行：A工具配置｜B忽略规则｜C/D类型标注｜E依赖验证、两问初稿】→【并行：B忽略PR，由A/D审查、B跟进合并｜C/D类型PR，由A/E审查、C跟进合并】→ A同步两项结果并做全文件检查，B/C/D修复所属部分，E补全两问并交A收录 → A提交工具PR，B/D审查，A跟进合并 → 最终验收**

每条PR均需两名非作者批准。C标注data_cleaner.py；D标注data_loader.py和visualizer.py。E结合B的CSV结果与依赖验证完成两问，随A的工具PR提交。A/B/C分别负责工具/忽略/类型PR的合并跟进和已合并来源分支清理；按仓库权限执行。各人在合并后同步并安装hooks。

#### 第2题：Pixi环境先行，D整合，C检查

**B完成并验证smoke环境 → D完成数据准备、基础统计和总体生存率 →【并行：A分布图｜C年龄分组敏感性｜E年龄分组比较｜D整理notebook结构】→ D整合notebook/README并完整复跑 → C检查，D协调A/B/C/E修复所属部分，C复核 → D跟进合并并清理分支 → 最终验收**

C/E先约定基础年龄分组和生存率口径，再分别开展比较与敏感性分析。B负责锁文件、nbstripout和环境说明；各成员在自己的clone安装hook。D的数据准备、基础统计与总体生存率计作同一组基础TODO；D的整合限于接入、复跑、统一格式和协调，各作者修自己的代码、图和解释。

#### 第3题NBA：数据可读后并行，E整合，B检查

**C提供下载/建库步骤、可读取的数据库入口及表字段说明 →【并行：A/B/D/E各完成小题和一个洞见｜C打包、loader说明及安装/导入验证】→ E整合最终notebook/README并完整复跑 → B检查，E协调A/B/C/D修复所属部分，B复核 → E跟进合并并清理分支 → 最终验收**

warm-up分工：C路径/连接，A数据库结构，B表清单，D指定表字段，E最早/最晚比赛日期。选题可与数据准备并行；各人在本机验证数据可读后即可分析，无须等待整份warm_up.ipynb或打包完成。C的安装/导入验证在最终整合前完成，不代写四位洞见作者的分析函数。

#### 第5题：沿用Conda，A写作、B组装、C检查

**各自确认原Conda环境可用 →【并行：B年龄/票价｜C家庭变量｜D性别/舱位｜E缺失值/可用性】→【并行：A筛图、写报告｜B整理图文件、README】→ B将选定图表和A的文字组装进报告notebook并完整复跑 → C检查，A修文字、B修组装，B/C/D/E各修分析，C复核 → B跟进合并并清理分支 → 最终验收**

B/C/D/E先交图及简短解释；A负责图表取舍和≤500词正文，B负责报告装配、README及复跑。B保留原README说明，完成时将原项目介绍与本次可视化说明一起完善；保留docs/readme-history中的原README备份。C负责检查、反馈和复核，不代替原作者修改报告或代码。

### 作业占位

作业占位文件和原notebook中的TODO留给对应成员完成；本次只同步分工和流程，不预填分析、答案或报告。
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
