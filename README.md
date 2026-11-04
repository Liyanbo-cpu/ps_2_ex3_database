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

#### 第1题：并行准备，再汇合验收

1. **先确认基线和环境**：各人同步仓库，激活自己的 PS1 Conda 环境，安装现有项目依赖及所需检查工具。
2. **三条线并行**：A 在独立分支配置 hooks、flake8、mypy，先明确检查规则；B 验证并修订忽略规则和 CSV 跟踪行为；C/D 按约定函数范围加类型标注。C/D 可先动手，不必等 A 的配置合并或全文件检查通过。E 同步收集 B 的 CSV 验证记录，并验证 mypy 依赖问题。
3. **推荐先验收类型标注，再验收工具配置**：C/D 的类型标注 PR 经两名非作者 review 后由仓库主人合并；B 的忽略规则 PR 可独立审查合并。随后 A 同步最新主分支，将工具配置与已标注代码一起运行全文件检查；类型问题由 C/D 修正，配置和格式问题由 A 协调处理，E 完成两问答案。
4. **最后审查、合并并各自安装**：hooks、忽略规则、类型标注分别保留独立 PR，各需两名非作者 review。工具 PR 检查通过后由仓库主人合并；各人同步并在自己的 clone 安装 hooks。A 前期交付的是可运行的规则配置，最终“全文件通过”需等配置和标注齐备。

#### 第2题

**B 环境 → C 数据准备 → A/D/E 分析 → D 整合**。nbstripout 配置可并行完善，提交前各自在本机装好 hook。

#### 第3题 NBA：数据先可用，洞见先做，最终 notebook 后整合

- **启动洞见的必要条件**：本机数据库已下载并可读取，已确认数据库相对路径及所需表/列。C 优先给出获取、连接与表结构说明；各人按说明在本机准备数据。已自行完成这些验证的成员可先开始，不必等 C 的其他工作全部结束。
- **可并行的工作**：A/B/D/E 提出选题并分别开展四条洞见的查询、函数、图表和解释；C 的打包配置以及共同认领的 warm-up 可同步进行。选题讨论可以在数据准备期间开始。
- **不构成开工门槛**：不用先完成整份 `warm_up.ipynb`、`pyproject.toml`，或完善最终 `analysis.ipynb`。warm-up 用于熟悉和核验数据库；最终 notebook 用于展示已经完成的发现。
- **最终整合条件**：四条洞见各自交齐查询、函数、必要图表和解释，并完成打包/函数导入验证后，由 E 接入 `analysis.ipynb` 并从头复跑。

#### 第5题

**各自确认原 Conda 环境可用 → B/C/D/E 并行分析 → A 整合**。报告≤500词，不含图；README 补充可视化说明，同时保留原项目说明。

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
