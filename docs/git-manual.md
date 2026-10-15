# Git 与 GitHub 操作手册

> **适用环境**：Windows + Git Bash
> **覆盖范围**：从零配置到日常提交、撤销恢复、报错排查、多机器协作
> **使用方式**：按目录检索，无需通读。第 4 章与第 7 章为高频章节。
> **建议存放位置**：笔记仓库的 `docs/git-manual.md`

---

<a id="toc"></a>
## 目录

- [🚀 快速通道：20 分钟从零到第一次 push](#quickstart)
- [0. 十分钟搞懂 6 个概念](#ch0)
  - [0.1 四个区域](#s0-1)
  - [0.2 commit 是快照，不是差异](#s0-2)
  - [0.3 分支只是一条快照链](#s0-3)
  - [0.4 HEAD 是"你现在在哪"](#s0-4)
  - [0.5 一句话记住方向](#s0-5)
  - [0.6 origin / main / 提交哈希：三个绕不开的名字](#s0-6)
- [1. 安装与配置](#ch1)
  - [1.1 安装](#s1-1)
  - [1.2 必做配置（只做一次）](#s1-2)
  - [1.3 可选：GitHub CLI](#s1-3)
  - [1.4 可选：VS Code](#s1-4)
- [2. GitHub 认证](#ch2)
  - [2.1 方式 A：SSH Key（推荐）](#s2-1)
  - [2.2 方式 B：HTTPS + Personal Access Token](#s2-2)
  - [2.3 该选哪个？](#s2-3)
  - [2.4 常见认证报错](#s2-4)
- [3. 创建仓库与首次上传](#ch3)
  - [3.1 本地已有代码：上传到 GitHub](#s3-1)
  - [3.2 GitHub 已有仓库：克隆到本地](#s3-2)
  - [3.3 三种"忘了某一步"的补救](#s3-3)
  - [3.4 换电脑 / 换目录](#s3-4)
- [4. 日常循环：95% 的时间只用这 6 条命令](#ch4)
  - [4.1 git status 怎么读](#s4-1)
  - [4.2 git add 的用法](#s4-2)
  - [4.3 git commit 的写法](#s4-3)
  - [4.4 git pull 的适用场景](#s4-4)
  - [4.5 推荐加几个别名，少打很多字](#s4-5)
  - [4.6 删除文件、重命名、文件名带空格](#s4-6)
- [5. .gitignore：别把垃圾传上去](#ch5)
  - [5.1 它是干什么的](#s5-1)
  - [5.2 语法](#s5-2)
  - [5.3 三个高频问题](#s5-3)
  - [5.4 全局忽略配置](#s5-4)
- [6. 分支：什么时候用，什么时候不用](#ch6)
  - [6.1 你现在可以只用 main](#s6-1)
  - [6.2 分支操作](#s6-2)
  - [6.3 冲突长什么样，怎么解](#s6-3)
  - [6.4 一条铁律](#s6-4)
- [7. 撤销与急救（最该读的一章）](#ch7)
  - [7.1 🔴 改错了，但还没 add](#s7-1)
  - [7.2 🟢 add 错了，想取消暂存](#s7-2)
  - [7.3 🟡 提交说明写错了 / 漏了文件（还没 push）](#s7-3)
  - [7.4 🟡 想撤销最近一次（或几次）commit](#s7-4)
  - [7.5 🟡 手滑 reset --hard 把东西弄没了](#s7-5)
  - [7.6 🟢 已经 push 了，想撤销](#s7-6)
  - [7.7 ⛔ 提交了不该提交的东西](#s7-7)
  - [7.8 🟢 误删了文件](#s7-8)
  - [7.9 🟢 想临时切去干别的，手头的改动先放着](#s7-9)
  - [7.10 危险命令清单（敲之前停三秒）](#s7-10)
- [8. 常见报错逐条排查](#ch8)
  - [8.0 排查顺序：遇到报错先走这四步](#s8-0)
  - [8.1 `Please tell me who you are`](#s8-1)
  - [8.2 `failed to push some refs` / `rejected` / `non-fast-forward`](#s8-2)
  - [8.3 `refusing to merge unrelated histories`](#s8-3)
  - [8.4 `Permission denied (publickey)`](#s8-4)
  - [8.5 `Support for password authentication was removed`](#s8-5)
  - [8.6 `You are in 'detached HEAD' state`](#s8-6)
  - [8.7 `Your local changes would be overwritten by merge/checkout`](#s8-7)
  - [8.8 `fatal: not a git repository`](#s8-8)
  - [8.9 `warning: LF will be replaced by CRLF`](#s8-9)
  - [8.10 单文件超过 GitHub 的 100 MB 限制](#s8-10)
  - [8.11 `src refspec main does not match any`](#s8-11)
  - [8.12 `.git/index.lock 文件已存在`](#s8-12)
  - [8.13 中文文件名显示为转义字符](#s8-13)
  - [8.14 Jupyter Notebook 冲突](#s8-14)
  - [8.15 分叉分支的提示](#s8-15)
  - [8.16 当前分支没有上游分支](#s8-16)
  - [8.17 remote origin already exists](#s8-17)
  - [8.18 nothing to commit](#s8-18)
  - [8.19 `Too many arguments`](#s8-19)
  - [8.20 `Could not resolve hostname`](#s8-20)
  - [8.21 hosts 文件：什么时候能用，什么时候是坑](#s8-21)
  - [8.22 命令里的全角空格与弯引号](#s8-22)
- [9. GitHub 网页端：你还会用到的功能](#ch9)
  - [9.1 仓库页面结构（别人会看什么）](#s9-1)
  - [9.2 Issues：给自己建任务](#s9-2)
  - [9.3 Pull Request：给开源提 PR 的完整流程](#s9-3)
  - [9.4 Actions：自动检查](#s9-4)
  - [9.5 Releases 与 Tags：标记版本](#s9-5)
  - [9.6 GitHub Pages：免费放你的 Demo](#s9-6)
  - [9.7 Profile README：你的门面](#s9-7)
  - [9.8 在网页上直接改文件](#s9-8)
  - [9.9 其他功能](#s9-9)
- [10. 进阶：以后需要再回来](#ch10)
  - [10.1 rebase](#s10-1)
  - [10.2 cherry-pick](#s10-2)
  - [10.3 bisect](#s10-3)
  - [10.4 多远程仓库](#s10-4)
  - [10.5 子模块 submodule](#s10-5)
  - [10.6 Git LFS](#s10-6)
  - [10.7 worktree](#s10-7)
- [11. 你的专属工作流](#ch11)
  - [11.1 笔记仓库的日常流程](#s11-1)
  - [11.2 项目仓库的流程](#s11-2)
  - [11.3 开源贡献流程](#s11-3)
  - [11.4 每周维护例程](#s11-4)
- [12. 换电脑 / 多台机器](#ch12)
  - [12.1 先记住结论](#s12-1)
  - [12.2 什么跟着走，什么不跟着走](#s12-2)
  - [12.3 换机前：在旧电脑上自查（10 分钟）](#s12-3)
  - [12.4 新电脑：四步配置](#s12-4)
  - [12.5 两种迁移方式：clone 还是直接拷文件夹](#s12-5)
  - [12.6 没网络怎么办：用 git bundle 打包](#s12-6)
  - [12.7 你最可能遇到的真实场景：三台机器](#s12-7)
  - [12.8 治本：让"换电脑"不再是问题](#s12-8)
  - [12.9 换机检查清单](#s12-9)
- [附录 A：一页速查表](#apxa)
- [附录 B：我该敲哪条（决策树）](#apxb)
- [最后三条心法](#principles)

### 场景索引

| 场景 | 对应章节 |
|---|---|
| 尚无 GitHub 账号 | [🚀 快速通道 · 第 0 步](#quickstart) |
| 首次安装 Git、完成初始配置 | [🚀 快速通道](#quickstart) ／ [1.1](#s1-1) ／ [1.2](#s1-2) |
| 配置 SSH 认证、认证失败 | [2.1](#s2-1) ／ [2.4](#s2-4) |
| 将本地代码首次上传到 GitHub | [3.1](#s3-1) |
| 日常提交与推送 | [4.1](#s4-1) ／ [4.3](#s4-3) ／ [11.1](#s11-1) |
| 排除数据、权重等文件 | [5.1](#s5-1) ／ [5.2](#s5-2) |
| 撤销改动 | [7.1](#s7-1) → [7.2](#s7-2) → [7.3](#s7-3) → [7.4](#s7-4) → [7.5](#s7-5) |
| 撤销已推送的提交 | [7.6](#s7-6) |
| 提交了密钥或受限数据 | [7.7](#s7-7) |
| push 被拒绝 | [8.2](#s8-2) |
| 报错原因不明 | [第 8 章](#ch8) |
| 术语不明（origin、HEAD、detached） | [0.1](#s0-1) – [0.6](#s0-6) |
| 向开源项目提交 PR | [9.3](#s9-3) ／ [11.3](#s11-3) |
| 更换电脑或多机器协作 | [第 12 章](#ch12) |
| 查询具体命令 | [附录 A](#apxa) ／ [附录 B](#apxb) |

---

<a id="quickstart"></a>
## 🚀 快速通道：20 分钟从零到第一次 push

以下六步完成从注册到首次上传的全过程。其余章节可在遇到具体问题时查阅。

> **路径说明**：本文所有路径（例如 `/c/Users/13127/Documents/ml-learning-notes`）均为示例，请替换为你的实际位置。Git Bash 中 Windows 路径 `C:\Users\13127` 需写作 `/c/Users/13127`。

**第 0 步｜注册 GitHub 账号**（约 3 分钟，已有账号可跳过）

访问 https://github.com/signup，使用常用邮箱注册。用户名会出现在个人主页链接中，建议使用拼音或英文名，避免无意义字符。

注册后进入 **Settings → Emails** 确认邮箱已验证，否则提交不会计入贡献图。建议同时开启两步验证（2FA），并将恢复码存入密码管理器。

**第 1 步｜安装 Git**（约 5 分钟）—— 详见 [1.1](#s1-1)

下载地址：https://git-scm.com/download/win。安装选项基本保持默认即可，注意两处：

- 默认编辑器：选择 VS Code 或 Notepad++。若保留默认的 Vim，需记住退出方式：按 `i` 进入输入模式，按 `Esc`，输入 `:wq` 回车。
- 换行符转换：选择 **Checkout Windows-style, commit Unix-style**（即 `core.autocrlf=true`）。

**第 2 步｜配置身份信息**（约 2 分钟）—— 详见 [1.2](#s1-2)

```bash
git config --global user.name "你的名字"
git config --global user.email "你的GitHub注册邮箱"
git config --global init.defaultBranch main
git config --global core.quotepath false
```

**第 3 步｜配置 SSH key**（约 8 分钟）—— 详见 [2.1](#s2-1)

```bash
ssh-keygen -t ed25519 -C "你的GitHub注册邮箱"   # 连续回车三次
cat ~/.ssh/id_ed25519.pub                        # 复制输出的全部内容
```

将复制的内容粘贴到：GitHub → 头像 → Settings → SSH and GPG keys → New SSH key。

```bash
ssh -T git@github.com        # 输出 "Hi 你的用户名!" 即配置成功
```

**第 4 步｜在 GitHub 创建空仓库**（约 2 分钟）—— 详见 [3.1](#s3-1)

网页右上角 **+** → New repository → 名称填 `ml-learning-notes` → 选择 **Public** → **不勾选任何初始化选项**（README、.gitignore、license 均不勾）→ Create repository。

**第 5 步｜本地初始化并上传**（约 3 分钟）

```bash
cd /c/Users/13127/Documents/ml-learning-notes     # 替换为你的实际路径
git init
git add .
git commit -m "chore: 初始化学习笔记仓库"
git branch -M main
git remote add origin git@github.com:你的用户名/ml-learning-notes.git
git push -u origin main
```

刷新 GitHub 页面，确认文件已上传。

**后续每次学习结束，执行以下四条命令：**

```bash
git status
git add .
git commit -m "notes(python): 本次学习内容"
git push
```

遇到 push 被拒、误删、误提交等问题，查阅 [第 7 章](#ch7) 与 [第 8 章](#ch8)。

---

<a id="ch0"></a>
## 0. 十分钟搞懂 6 个概念

本章为后续命令提供必要的术语基础，阅读约需 10 分钟。

<a id="s0-1"></a>
### 0.1 四个区域

```
   你的文件夹              git add           git commit          git push
  ┌──────────┐          ┌──────────┐      ┌──────────┐       ┌──────────┐
  │  工作区   │ ───────▶ │  暂存区   │ ───▶ │ 本地仓库  │ ────▶ │ 远程仓库  │
  │ Working  │          │ Staging  │      │  Local   │       │  Remote  │
  │  Directory│ ◀─────── │  Area    │      │   Repo   │ ◀──── │ (GitHub) │
  └──────────┘  git      └──────────┘      └──────────┘  git  └──────────┘
                 restore                      reset       pull
```

- **工作区**：你能直接看到的文件夹，即日常编写代码的位置
- **暂存区**：一份待提交清单，`git add` 将文件加入该清单
- **本地仓库**：`.git` 文件夹，保存全部历史快照，`git commit` 在此写入记录
- **远程仓库**：GitHub 上的副本，`git push` 上传，`git pull` 下载

**为什么要有暂存区？** 因为它给你一次反悔的机会。改了 10 个文件，其中 3 个是实验性的垃圾，你可以只 add 那 7 个。没有暂存区，你只能全提交或全不提交。

<a id="s0-2"></a>
### 0.2 commit 是快照，不是差异

每次 `commit` 都是给整个项目拍一张照片，`git log` 就是相册。所以回退到任何历史版本都很容易——这也是你敢乱改代码的底气。

<a id="s0-3"></a>
### 0.3 分支只是一条快照链

```
main:    A ── B ── C ── D        ← main 是指向 D 的一个标签
                  \
feature:           E ── F        ← feature 指向 F
```

分支不是复制文件夹，只是一个指针。所以创建分支是瞬间完成的，随便建。

<a id="s0-4"></a>
### 0.4 HEAD 是"你现在在哪"

`HEAD` 指向你当前所在的分支。`detached HEAD` 意思是 HEAD 直接指向了某个提交而不是分支——这时产生的提交不属于任何分支，很容易丢。

<a id="s0-5"></a>
### 0.5 一句话记住方向

- `push` = 本地 → GitHub（上传）
- `pull` = GitHub → 本地（下载）

<a id="s0-6"></a>
### 0.6 origin / main / 提交哈希：三个绕不开的名字

**`origin`** 是远程仓库的**昵称**，不是关键字。`git remote add origin <地址>` 的意思是"我给这个远程地址起名叫 origin"，你完全可以叫它 `github`、`lab`。因为 `clone` 时 git 会自动起名 `origin`，所以全网教程都跟着用它。

**`main`** 是主分支的名字。老项目可能叫 `master`，只是名字不同，没有技术差异。`git branch -M main` 就是改名。

**提交哈希**（如 `a1b2c3d`）是每次 commit 的唯一编号，一长串十六进制字符。命令里用到它时，你只需要写**前 7 位**。怎么拿到它：

```bash
git log --oneline        # 每行开头的字符串即为哈希
```

---

<a id="ch1"></a>
## 1. 安装与配置

<a id="s1-1"></a>
### 1.1 安装

下载地址：https://git-scm.com/download/win

安装选项基本保持默认，注意两处：

- **默认编辑器**：选择 VS Code 或 Notepad++。若保留默认的 Vim，需掌握退出方式：按 `i` 进入输入模式，按 `Esc`，输入 `:wq` 回车。
- **换行符转换**：选择 **Checkout Windows-style, commit Unix-style**（即 `core.autocrlf=true`），这是 Windows 平台最省心的设置。

装完后你会得到一个 **Git Bash** 命令行窗口。**建议后续都用 Git Bash**——它和网上 99% 的教程命令一致，不会有 PowerShell 的引号/转义差异。

**怎么打开 Git Bash：**

- 开始菜单搜索 `Git Bash` 并打开
- 在文件资源管理器中**右键点击仓库文件夹** → **Open Git Bash here**，窗口会直接定位到该目录（推荐）

打开后先用 `pwd` 确认自己在哪：

```bash
pwd
# 例如输出 /c/Users/13127/Documents/ml-learning-notes
```

> **路径写法**：Git Bash 中 `C:\Users\13127` 写作 `/c/Users/13127`，（反斜杠换成正斜杠，盘符变成小写加 `/` 前缀）。路径里有空格要用引号包起来，例如 `cd "/c/Users/13127/My Notes"`。

验证安装：

```bash
git --version
# 期望输出形如 git version 2.4x.x.windows.1
```

<a id="s1-2"></a>
### 1.2 必做配置（只做一次）

```bash
# 身份信息：每次 commit 都会记录，GitHub 依据它把提交关联到账号
git config --global user.name "你的名字或GitHub用户名"
git config --global user.email "你的GitHub注册邮箱"

# 默认分支名改为 main（GitHub 现用 main，早期默认为 master）
git config --global init.defaultBranch main

# 避免中文文件名显示为转义字符
git config --global core.quotepath false

# 换行符转换，Windows 平台推荐 true
git config --global core.autocrlf true

# 保存 GitHub 凭据，避免反复输入
git config --global credential.helper manager
```

查看全部配置：

```bash
git config --list
```

> **user.email 的坑**：必须用你 GitHub 账号里已验证的邮箱，否则提交不会算到贡献图上。如果不想暴露真实邮箱，GitHub 提供了匿名邮箱 `xxxxx+用户名@users.noreply.github.com`（在 Settings → Emails 中查看）。

<a id="s1-3"></a>
### 1.3 可选：GitHub CLI

```bash
winget install --id GitHub.cli
```

登录一次后，创建仓库、提交 PR 等操作均可在命令行完成：

```bash
gh auth login          # 按提示依次选择 GitHub.com → HTTPS → 浏览器登录
gh repo create ml-learning-notes --public --source=. --push
```

<a id="s1-4"></a>
### 1.4 可选：VS Code

VS Code 内置 Git 图形界面，在冲突处理、逐行暂存、历史查看方面比命令行直观。命令行能力仍然必需（服务器环境没有图形界面），但日常操作可用图形界面提高效率。

安装后按 `Ctrl+Shift+G` 打开源代码管理面板。

---

<a id="ch2"></a>
## 2. GitHub 认证

**先说一条**：GitHub 从 2021 年 8 月起**不再接受账号密码**。使用 HTTPS 时必须使用 **Personal Access Token（PAT）**，使用 SSH 时必须配置 **SSH key**。直接输密码会报 `Support for password authentication was removed`。

<a id="s2-1"></a>
### 2.1 方式 A：SSH Key（推荐）

配置一次后长期有效，且不受 Token 过期影响。

**第 1 步：生成密钥**

```bash
ssh-keygen -t ed25519 -C "你的GitHub邮箱"
```

连续回车三次（使用默认路径，不设密码短语）。生成两个文件：

- `C:\Users\你的用户名\.ssh\id_ed25519` —— **私钥，不得提供给任何人**
- `C:\Users\你的用户名\.ssh\id_ed25519.pub` —— 公钥，用于上传至 GitHub

**第 2 步：复制公钥内容**

```bash
cat ~/.ssh/id_ed25519.pub
```

选中输出的全部内容复制（以 `ssh-ed25519` 开头，以邮箱结尾）。

**第 3 步：粘贴到 GitHub**

GitHub → 右上角头像 → **Settings** → 左侧 **SSH and GPG keys** → **New SSH key** → Title 填写便于识别的名称（如 `个人笔记本`）→ Key 粘贴公钥内容 → **Add SSH key**

**第 4 步：测试**

```bash
ssh -T git@github.com
```

首次连接会询问 `Are you sure you want to continue connecting?`，输入 `yes` 回车。

输出 `Hi 你的用户名! You've successfully authenticated...` 即配置成功。

> 若报 `Permission denied (publickey)`，参见 [8.4](#s8-4)。

<a id="s2-2"></a>
### 2.2 方式 B：HTTPS + Personal Access Token

**第 1 步：生成 Token**

GitHub → 头像 → **Settings** → 页面底部 **Developer settings** → **Personal access tokens** → **Tokens (classic)** → **Generate new token (classic)**

- Note：填写用途标识，如 `个人笔记本`
- Expiration：建议 90 天或自定义期限（**到期需重新生成**，不建议选择 No expiration）
- Scopes：至少勾选 `repo`（读写仓库）；若需使用 Actions 再勾选 `workflow`

生成后**立即复制**，离开页面后将无法再次查看。

**第 2 步：首次 push 时使用**

```
Username: 你的GitHub用户名
Password: 粘贴刚才生成的 Token（不是账号密码）
```

配合 `credential.helper manager`，后续无需重复输入。

<a id="s2-3"></a>
### 2.3 该选哪个？

|  | SSH | HTTPS + PAT |
|---|---|---|
| 配置难度 | 中 | 低 |
| 是否过期 | 永不过期 | Token 会过期 |
| 适用情形 | 长期在固定设备上使用 | 临时使用、多设备、网络限制 SSH |

**推荐使用 SSH。**

<a id="s2-4"></a>
### 2.4 常见认证报错

| 报错 | 原因 | 处理 |
|---|---|---|
| `Support for password authentication was removed` | 使用了账号密码 | 改用 PAT 或 SSH，见 [2.1](#s2-1) / [2.2](#s2-2) |
| `Permission denied (publickey)` | 公钥未上传或使用了错误的密钥 | 重做 [2.1](#s2-1) 的第 3、4 步 |
| `ssh: connect to host github.com port 22: Connection timed out` | 网络屏蔽了 22 端口 | 改用 HTTPS，或按下方配置 443 端口 |
| `remote: Invalid username or token` | PAT 输入错误或已过期 | 重新生成 Token |
| `fatal: could not read Username for 'https://github.com'` | 凭据未保存 | `git config --global credential.helper manager` |

**22 端口被屏蔽时的配置**（写入 `~/.ssh/config`，文件不存在则新建）：

```
Host github.com
  Hostname ssh.github.com
  Port 443
  User git
```

---

<a id="ch3"></a>
## 3. 创建仓库与首次上传

<a id="s3-1"></a>
### 3.1 本地已有代码：上传到 GitHub

**第 1 步：在 GitHub 创建空仓库**

- 右上角 **+** → **New repository**
- Repository name：`ml-learning-notes`
- 选择 **Public**（求职场景需要公开）
- **不要勾** Add a README file / Add .gitignore / Choose a license —— 勾了会和你本地的文件形成两条互不相干的历史，第一次 push 就报错

**第 2 步：获取仓库地址**

仓库建好后，页面上会显示一段“…or push an existing repository from the command line”，里面有地址。**更可靠的拿法**：

仓库页面 → 绿色 **Code** 按钮 → 切换到 **SSH** 标签 → 点击右侧复制图标。

你会得到形如 `git@github.com:你的用户名/ml-learning-notes.git` 的地址，这就是下面 `git remote add` 要用的东西。

> 用 SSH 地址的前提是 [2.1](#s2-1) 已经配好。如果还没配，先用 HTTPS 地址（`https://github.com/...`）顶着，之后再 `git remote set-url` 换掉。

**第 3 步：本地初始化并上传**

```bash
# 进入你的文件夹（路径替换为实际位置）
cd /c/Users/13127/Documents/ml-learning-notes

# 初始化本地仓库，会在当前目录创建 .git 文件夹
git init

# 将当前所有文件加入暂存区
git add .

# 提交
git commit -m "chore: 初始化学习笔记仓库"

# 确认分支名为 main（早期版本的 git 可能创建 master）
git branch -M main

# 关联远程仓库：origin 是为该地址起的昵称，替换为你的用户名和仓库名
git remote add origin git@github.com:你的用户名/ml-learning-notes.git

# 推送；-u 将本地 main 与远程 main 绑定，此后直接执行 git push 即可
git push -u origin main
```

**第 4 步：验证**

```bash
git remote -v
# 应显示 origin 的 fetch 与 push 两行地址

git log --oneline
# 应显示刚才的提交记录
```

刷新 GitHub 页面，确认文件已全部上传。

<a id="s3-2"></a>
### 3.2 GitHub 已有仓库：克隆到本地

```bash
cd /c/Users/13127/Documents
git clone git@github.com:你的用户名/仓库名.git
cd 仓库名
```

`clone` 会自动帮你做好三件事：下载全部历史、建好 `.git`、把 origin 配好并绑定 main。**不需要再 `git init` 和 `git remote add`。**

<a id="s3-3"></a>
### 3.3 三种"忘了某一步"的补救

```bash
# 未关联远程仓库
git remote add origin git@github.com:用户名/仓库名.git

# 关联了错误的地址
git remote set-url origin git@github.com:用户名/正确的仓库名.git

# 首次推送时忘记 -u，导致后续每次都要写全
git push -u origin main
```

<a id="s3-4"></a>
### 3.4 换电脑 / 换目录

`.git` 文件夹随项目文件夹一同移动。将整个文件夹复制到另一台电脑后，它仍是同一个仓库，`git push` 可以直接推送（前提是新电脑已配置 SSH key）。更换电脑的完整流程见 [第 12 章](#ch12)。

---

<a id="ch4"></a>
## 4. 日常循环：95% 的时间只用这 6 条命令

```bash
git status                        # ① 当前状态与改动（使用频率最高）
git add .                         # ② 将所有改动加入暂存区
git commit -m "说明本次改动"        # ③ 写入提交
git push                          # ④ 上传到 GitHub
git pull                          # ⑤ 下载远程改动（更换设备或多人协作时）
git log --oneline --graph -10      # ⑥ 查看最近 10 条历史
```

<a id="s4-1"></a>
### 4.1 git status 怎么读

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:          ← 已修改但未 add
  modified:   python/01-basics/notes.md

Untracked files:                         ← 新文件，git 尚未跟踪
  python/02-functions/notes.md

nothing added to commit but untracked files present
```

**养成习惯：`add` 之前和 `commit` 之前各敲一次 `git status`。**

<a id="s4-2"></a>
### 4.2 git add 的用法

```bash
git add .                            # 当前目录下的全部改动（最常用）
git add python/01-basics/notes.md    # 指定单个文件
git add python/                       # 指定目录
git add -A                           # 包含删除操作（较新版本的 git 中 add . 也已包含删除）
git add -p                           # 逐块选择要提交的内容
```

<a id="s4-3"></a>
### 4.3 git commit 的写法

```bash
git commit -m "简短说明"
git commit                            # 不带 -m 会打开编辑器撰写多行说明
git commit -am "说明"                 # add 与 commit 合并（仅对已跟踪文件有效，新文件无效）
git commit --amend                    # 修改上一条提交，见 7.3
```

**提交说明推荐格式**（加类型前缀，便于快速识别改动性质）：

| 前缀 | 用途 | 示例 |
|---|---|---|
| `notes:` | 学习笔记 | `notes(python): 补充变量是引用而非拷贝` |
| `feat:` | 新增功能或代码 | `feat(numpy): 实现广播规则的 3 个例子` |
| `fix:` | 修复缺陷 | `fix(train_loop): 修正验证集未调用 model.eval()` |
| `docs:` | 文档 | `docs(clip): 完成 CLIP 论文三遍法笔记` |
| `chore:` | 杂项 | `chore: 更新 .gitignore 排除 .pth 文件` |
| `refactor:` | 重构 | `refactor: 把训练循环拆成独立函数` |

**一条铁律：一次提交只做一件事。** 把笔记、代码、图片、配置的改动混在一条提交里，以后出问题无法定位。

<a id="s4-4"></a>
### 4.4 git pull 的适用场景

- 更换设备后，开始工作前先 `git pull`
- 在 GitHub 网页端直接修改过文件（例如改 README），本地需要同步
- 多人协作时，每次开始工作前

单人单设备且从不在网页端修改文件的情况下，`pull` 的使用频率较低。但 push 被拒绝时，它通常是第一步处理手段（见 [8.2](#s8-2)）。

<a id="s4-5"></a>
### 4.5 推荐加几个别名，少打很多字

```bash
git config --global alias.st "status"
git config --global alias.sw "switch"
git config --global alias.br "branch"
git config --global alias.lg "log --oneline --graph --all -15"
```

配置后 `git st` 等价于 `git status`，`git lg` 输出图形化历史。

> 此处刻意未为 `checkout` 设置别名。原因见 [6.2](#s6-2)：`checkout` 一条命令承担了两类危险程度不同的操作，使用 `switch` 与 `restore` 更安全。

<a id="s4-6"></a>
### 4.6 删除文件、重命名、文件名带空格

**删除文件**：直接用文件管理器删掉，然后正常 `git add .` + `commit` 就行，git 会识别出这是删除操作。

```bash
rm 不要的文件.md        # 在 Git Bash 中删除
git add .               # add . 会记录删除操作
git commit -m "chore: 删除过时的笔记"
```

也可使用 `git rm 文件名`，等价于删除文件并加入暂存区。

> **不要手动删除 `.git` 文件夹。** 该目录保存整个仓库的历史，删除后仓库会退化为普通文件夹，全部提交记录丢失。仅在确认放弃全部历史时才执行 `rm -rf .git`。

**重命名文件**：不需要特别命令。改名后 `git add .` 即可，git 会自动识别为"重命名"而不是"删一个再建一个"。

**文件名里有空格或中文**：路径要用引号包起来。

```bash
git add "我的 笔记.md"
git add "python/第一课.md"
```

不加引号时 git 会将空格视为文件分隔符，报 `pathspec ... did not match`。

---

<a id="ch5"></a>
## 5. .gitignore：别把垃圾传上去

<a id="s5-1"></a>
### 5.1 它是干什么的

在仓库根目录建一个 `.gitignore` 文件，里面写规则，git 就**永远不会**把这些文件加入暂存区。对你是必需的——医学数据、模型权重、虚拟环境、缓存文件都不能上传。

<a id="s5-2"></a>
### 5.2 语法

```gitignore
# 以 # 开头的行为注释

# 忽略单个文件
secret.txt

# 忽略所有 .pth 文件（模型权重）
*.pth

# 忽略目录（结尾的 / 表示目录）
data/
__pycache__/
.ipynb_checkpoints/

# 忽略任意层级的同名目录
**/logs/

# 忽略目录内容但保留目录本身
# 注意：不能写成 data/ 后再取反，那样 git 不会进入该目录
data/*
!data/.gitkeep

# 只忽略根目录下的该文件，不影响子目录中的同名文件
/config.yaml
```

> **`!` 取反的坑**：`!` 不能用来"从被忽略的目录里捞回一个文件"，因为一旦目录被整体忽略，git 就不会进去找。必须写成 `目录/*` 加 `!目录/要保留的文件` 的形式。

<a id="s5-3"></a>
### 5.3 三个高频问题

**问题 1：文件已写入 .gitignore，仍被提交**

原因：它**已经被跟踪**了，`.gitignore` 对已跟踪文件无效。解决：

```bash
git rm --cached 文件名          # 停止跟踪，保留本地文件（关键是 --cached）
git commit -m "chore: 停止跟踪 xxx"
```

**问题 2：我想知道某个文件为什么被忽略了**

```bash
git check-ignore -v 文件名
# 输出会告诉你匹配到了哪条规则、在第几行
```

**问题 3：大文件或敏感数据已被提交**

普通 `git rm` 不够，因为历史里还有。见 [7.7](#s7-7)。

<a id="s5-4"></a>
### 5.4 全局忽略配置

有些文件**所有仓库**都不想看到。建一个全局配置文件：

```bash
git config --global core.excludesfile ~/.gitignore_global
```

在 `~/.gitignore_global` 中写入：

```gitignore
.DS_Store
Thumbs.db
.idea/
.vscode/
*.swp
```

---

<a id="ch6"></a>
## 6. 分支：什么时候用，什么时候不用

<a id="s6-1"></a>
### 6.1 你现在可以只用 main

**个人学习笔记仓库一直用 `main` 就好，不需要分支。** 分支的价值在多人协作和"并行维护多个版本"，你不属于这两种情况。

**什么时候开始用分支：**

- 在项目 P0/P1 中尝试可能失败的改动，避免影响可运行版本
- 向开源项目提交 PR（**必须**使用分支，见 [11.3](#s11-3)）
- 同时进行两件互不相关的修改

<a id="s6-2"></a>
### 6.2 分支操作

```bash
git branch                         # 列出本地分支，带 * 的为当前分支
git branch -a                      # 连同远程分支一起列出
git switch -c feature-x            # 新建并切换到 feature-x（新命令）
git checkout -b feature-x          # 同上（旧命令，教程中更常见）
git switch main                    # 切回 main
git checkout main                  # 同上（旧命令）

git merge feature-x                # 在 main 分支上执行：把 feature-x 合并进来
git branch -d feature-x            # 删除已合并的分支
git branch -D feature-x            # 强制删除未合并的分支
git push origin feature-x          # 推送分支到远程
git push origin --delete feature-x # 删除远程分支
```

**`switch` 与 `restore` 是 Git 2.23 引入的新命令，与旧命令的对应关系如下：**

| 旧命令 | 新命令 | 作用 |
|---|---|---|
| `git checkout <分支>` | `git switch <分支>` | 切换分支 |
| `git checkout -b <分支>` | `git switch -c <分支>` | 新建并切换 |
| `git checkout -- <文件>` | `git restore <文件>` | 丢弃工作区改动 |
| `git reset HEAD <文件>` | `git restore --staged <文件>` | 取消暂存 |

两个都能用。**看教程时注意旧命令，自己敲时用新命令更安全**——因为 `checkout` 一条命令干了两件危险程度完全不同的事。

<a id="s6-3"></a>
### 6.3 冲突长什么样，怎么解

触发场景：同一个文件的同一行被两条分支都改了。合并时会看到：

```
Auto-merging notes.md
CONFLICT (content): Merge conflict in notes.md
Automatic merge failed; fix conflicts and then commit the result.
```

打开文件后可见如下标记：

```
<<<<<<< HEAD
当前分支上的内容
=======
另一条分支上的内容
>>>>>>> feature-x
```

**解决四步：**

1. 手动编辑，确定最终保留的内容（**必须删除 `<<<<<<<`、`=======`、`>>>>>>>` 三行标记**）
2. `git add notes.md`
3. `git commit`（无需 `-m`，git 会提供默认的合并提交说明）
4. `git push`

**放弃合并、回到合并前状态：**

```bash
git merge --abort
```

**用图形工具更省事**：VS Code 会在冲突文件里显示四个按钮（采用当前更改 / 采用传入更改 / 保留双方 / 比较更改），点一下就行。

<a id="s6-4"></a>
### 6.4 一条铁律

> **合并前先切到目标分支。** `git merge feature-x` 的意思是"把 feature-x 合进**我当前所在**的分支"。如果你当前就在 feature-x 上执行它，结果正好相反。

---

<a id="ch7"></a>
## 7. 撤销与急救（最该读的一章）

按"错误发生在哪个阶段"查表。**先看危险等级再敲命令。**

| 危险等级 | 含义 |
|---|---|
| 🟢 安全 | 不丢失内容，或内容可从提交记录 / reflog 中找回 |
| 🟡 谨慎 | 会改写本地历史，但内容通常可通过 reflog 找回 |
| 🔴 危险 | **改动本身不可恢复**，执行前必须确认 |
| ⛔ 极危险 | 涉及已推送的历史，会影响协作者 |

<a id="s7-1"></a>
### 7.1 🔴 改错了，但还没 add

```bash
git restore python/01-basics/notes.md     # 丢弃该文件的全部未暂存改动
git restore .                             # 丢弃全部未暂存改动
git checkout -- python/01-basics/notes.md # 旧命令，效果相同
```

> ⚠️ **这是全套命令里少数真正"丢了就没了"的操作。** 这些改动从来没进过 git（没 add、没 commit），reflog 里也没有记录。
> **敲之前一定先 `git diff` 看一眼自己到底要丢什么。** 如果只是想暂时放一放，用 `git stash`（见 [7.9](#s7-9)），别用 `restore`。

<a id="s7-2"></a>
### 7.2 🟢 add 错了，想取消暂存

```bash
git restore --staged python/01-basics/notes.md   # 新命令
git reset HEAD python/01-basics/notes.md          # 旧命令
git restore --staged .                            # 取消全部暂存
```

**注意**：这只是把文件从暂存区拿出来，**内容还在**，改动没丢。

<a id="s7-3"></a>
### 7.3 🟡 提交说明写错了 / 漏了文件（还没 push）

适用于提交尚未 push 的情况。

```bash
# 仅修改说明文字
git commit --amend -m "正确的说明"

# 补充遗漏的文件
git add 漏掉的文件
git commit --amend --no-edit        # 保留原说明，将新文件并入上一条提交

# 用编辑器修改说明
git commit --amend
```

> **铁律：`--amend` 只能用于还没 push 的提交。** 已经 push 过的再 amend，会导致本地和远程历史不一致，下次 push 就被拒。

<a id="s7-4"></a>
### 7.4 🟡 想撤销最近一次（或几次）commit

```bash
# ① 撤销提交，改动保留在暂存区（相当于已 add，可直接重新提交）
git reset --soft HEAD~1        # 撤销 1 条
git reset --soft HEAD~3        # 撤销最近 3 条

# ② 撤销提交，改动放回工作区（变为未 add 状态）
git reset --mixed HEAD~1       # --mixed 为默认值，直接写 git reset HEAD~1 效果相同

# ③ 撤销提交，同时丢弃改动
git reset --hard HEAD~1        # 改动会丢失，恢复方法见 7.5
```

`HEAD~1` 的含义：`HEAD` 为当前位置，`~1` 表示向前 1 个提交，`~3` 表示向前 3 个。

**三种模式的差异：**

| 命令 | 提交记录 | 暂存区 | 工作区文件内容 |
|---|---|---|---|
| `--soft` | 撤销 | **保留**（仍为"已 add"） | 不变 |
| `--mixed`（默认） | 撤销 | 清空（变为"未 add"） | 不变 |
| `--hard` | 撤销 | 清空 | **丢弃** |

**破坏力从左到右递增**：`--soft` 只动提交记录，`--mixed` 再动暂存区，`--hard` 连文件内容一起丢。

**不要背"保留/丢弃"，只问自己一个问题：这次的代码改动我还要吗？**

- 需要保留并直接重新提交 → `--soft`
- 需要保留但想重新挑选文件 → `--mixed`（或省略不写）
- 不再需要，全部丢弃 → `--hard`（执行前确认改动已在其他地方备份或已 push）

<a id="s7-5"></a>
### 7.5 🟡 手滑 reset --hard 把东西弄没了

**先别慌，也先别做任何其他 git 操作。** 用 reflog 找回：

```bash
git reflog
# 输出示例：
# a1b2c3d (HEAD -> main) HEAD@{0}: reset: moving to HEAD~1
# e4f5g6h HEAD@{1}: commit: feat(numpy): 广播规则示例   ← 被撤销的那条提交
# ...

# 找到目标提交的哈希（前 7 位即可），然后：
git reset --hard e4f5g6h
# 更稳妥的方式：新建分支指向它，先检查内容
git branch rescue e4f5g6h
git switch rescue
```

**reflog 保留约 90 天内的全部 HEAD 移动记录，是你最后的安全网。** 记住它的存在，能省下几小时的崩溃。

<a id="s7-6"></a>
### 7.6 🟢 已经 push 了，想撤销

**原则：已推送的历史不要改写，用"反向提交"来抵消。**

**先拿到要撤销的那条提交的哈希（前 7 位就够）：**

```bash
git log --oneline
# a1b2c3d (HEAD -> main) fix(train_loop): 验证集漏了 model.eval()
# e4f5g6h feat(numpy): 广播规则示例
```

```bash
git revert a1b2c3d       # 生成一条新提交，内容与 a1b2c3d 相抵消
git push
```

`revert` 是**安全**的——它不删历史，只加了一条"撤销"记录，协作者 pull 一下就行。

> 如果 `revert` 时提示冲突，处理方法和普通合并冲突一样（见 [6.3](#s6-3)），解决后 `git add` + `git revert --continue`。

**如果提交里含敏感信息（Token、密码），`revert` 不够**，因为历史里还留着。必须重写历史，见 [7.7](#s7-7)。

<a id="s7-7"></a>
### 7.7 ⛔ 提交了不该提交的东西

**分两种情况，处理方式完全不同。**

#### 情况 A：只是大文件或垃圾文件，不敏感

```bash
# 第 1 步：停止跟踪，保留本地文件
git rm --cached 大文件.pth
git rm -r --cached data/

# 第 2 步：用编辑器打开 .gitignore，加入以下两行：
#   *.pth
#   data/
# （不要用 echo "..." >> .gitignore 追加：不同 shell 的编码处理不一致，容易写坏文件）

# 第 3 步：提交并推送
git add .gitignore
git commit -m "chore: 停止跟踪大文件与数据目录"
git push
```

> **注意**：这只对**以后**的提交生效，历史里那次的文件还在，仓库体积不会变小。如果文件很大（比如 200 MB 的权重），想连历史一起清掉，用下面**情况 B 的 `git filter-repo`**，把路径换成 `--path 大文件.pth --invert-paths` 即可，步骤完全一样。

#### 情况 B：密钥、隐私数据或受限数据（必须彻底清除）

**第 1 步：先止血。** 立刻去对应平台**作废并重新生成**那个 Token / 密钥。**改密钥永远优先于改历史**——因为历史清理要花时间，而泄露是即时的。

**第 2 步：重写历史。** 使用 `git filter-repo`（`filter-branch` 的现代替代工具）：

```bash
# 安装（Git Bash 中使用 pip）
pip install git-filter-repo

# 从全部历史中彻底删除某个文件
git filter-repo --path 敏感文件.txt --invert-paths

# 删除某个目录
git filter-repo --path data/ --invert-paths
```

**第 3 步：强制推送**

```bash
git push --force
```

> ⚠️ `--force` 会覆盖远程历史。**单人仓库没问题；有协作者时必须提前通知，否则他们的本地仓库会炸。**

**第 4 步：如果仓库是 public 且已过一段时间**，最好再联系 GitHub Support 请求清理缓存，并假设数据已经泄露（公开仓库的历史会被爬虫和镜像站抓取）。

**预防措施：**

- 密钥一律存放在环境变量或 `.env` 中，并写入 `.gitignore`
- **医学数据、病例影像、实验室私有数据不入库**，无论仓库为 public 还是 private
- 提交前敲 `git status` 和 `git diff --cached --stat` 扫一眼文件清单

<a id="s7-8"></a>
### 7.8 🟢 误删了文件

```bash
git restore 误删的文件            # 从最新提交恢复
git checkout HEAD~1 -- 文件       # 恢复到上一个版本
git restore --source=a1b2c3d 文件  # 恢复到指定提交的版本
```

<a id="s7-9"></a>
### 7.9 🟢 想临时切去干别的，手头的改动先放着

```bash
git stash                  # 收起当前未提交的改动，工作区恢复干净
git stash list             # 查看已保存的 stash
git switch 其他分支         # 处理其他事务
git switch 回来
git stash pop              # 取回最近一条 stash 并从栈中删除
git stash apply            # 取回但保留在栈中
git stash drop             # 丢弃最近一条 stash
```

<a id="s7-10"></a>
### 7.10 危险命令清单（敲之前停三秒）

| 命令 | 风险 |
|---|---|
| `git reset --hard` | 丢弃工作区改动，不可恢复 |
| `git clean -fd` | 删除全部未跟踪文件（新建但未 add 的文件会丢失） |
| `git push --force` | 覆盖远程历史，可能破坏协作者的工作 |
| `git branch -D` | 强制删除未合并的分支 |
| `git checkout .` / `git restore .` | 丢弃全部未暂存改动 |
| `git filter-repo` | 重写全部提交哈希，所有协作者需重新 clone |

**习惯：敲任何带 `--hard`、`--force`、`-D`、`clean` 的命令前，先敲一次 `git status` 确认自己在哪、有什么没提交。**

---

<a id="ch8"></a>
## 8. 常见报错逐条排查

<a id="s8-0"></a>
### 8.0 排查顺序：遇到报错先走这四步

报错信息本身就是证据。**先读它，再猜。** 下面这个顺序是有代价换来的。

1. **逐字读报错原文。** 不要扫一眼就归类，特别注意那些"看起来像别的意思"的词。
2. **如果报错里带了 `usage:`，把它读完。** 它列出了该命令**所有合法的选项**。判断"是不是选项写错了"最直接的依据就在这里。
3. **检查选项字母和大小写。** 大小写不同的短选项在 Unix 命令里是**两个完全不同的东西**（`-c` 和 `-C`、`-f` 和 `-F`、`-r` 和 `-R`……）。一个字母写错，报错信息常常与直觉完全对不上。
4. **最后才怀疑字符编码问题**（全角空格、弯引号、隐藏字符）。这类问题真实存在（见 [8.22](#s8-22)），但**概率远低于拼写错误**，不要一上来就往这里想。

> **一个信号，比任何猜测都有用**：
> **"我按某个方案修了，但报错一模一样"** —— 这几乎总是说明**病因判断错了**，而不是"修得不够"。
> 此时应退回第 1 步重新读报错，**而不是在原方案上叠加新的修法**（见 [8.21](#s8-21)）。

> **延伸阅读**：**[网络问题排查实例](网络问题排查实例.md)** —— 一次三阶段的完整排查复盘。
> 它说明了一件比单个报错更重要的事：**针对错误病因所做的修复，会以一个新问题的形式回来。**


<a id="s8-1"></a>
### 8.1 `Please tell me who you are`

```
*** Please tell me who you are.
fatal: unable to auto-detect email address
```

**原因**：未配置 user.name / user.email。
**处理**：参见 [1.2](#s1-2)，执行两条 `git config --global`。

<a id="s8-2"></a>
### 8.2 `failed to push some refs` / `rejected` / `non-fast-forward`

```
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:xxx/xxx.git'
hint: Updates were rejected because the remote contains work that you do not have locally.
```

**原因**：远程存在本地没有的提交。常见于在 GitHub 网页端直接修改了文件，或曾在另一台设备上提交。

**处理**（两种方案，推荐第一种）：

```bash
# 方案 1：拉取远程改动并合并，再推送（会产生一条合并提交）
git pull --no-rebase
git push

# 方案 2：变基（历史更线性）
git pull --rebase
git push
```

若 `pull` 过程中提示冲突，按 [6.3](#s6-3) 处理。

<a id="s8-3"></a>
### 8.3 `refusing to merge unrelated histories`

```
fatal: refusing to merge unrelated histories
```

**原因**：本地与远程是两条独立的提交链，通常因为创建仓库时勾选了 README，之后本地又执行了 `git init`。

**处理**：

```bash
git pull origin main --allow-unrelated-histories
# 解决可能的冲突后
git push -u origin main
```

**预防**：在 GitHub 创建仓库时不勾选 Add a README file。

<a id="s8-4"></a>
### 8.4 `Permission denied (publickey)`

```
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.
```

**排查顺序**：

```bash
# ① 确认密钥文件存在
ls ~/.ssh/
# 应能看到 id_ed25519 与 id_ed25519.pub

# ② 测试认证
ssh -T git@github.com

# ③ 查看 ssh 实际使用的是哪个密钥
ssh -T -v git@github.com

# ④ 确认远程地址为 SSH 格式而非 HTTPS
git remote -v
# SSH 格式：git@github.com:用户名/仓库.git
# HTTPS 格式：https://github.com/用户名/仓库.git
```

最常见的原因是**公钥未正确粘贴到 GitHub**（复制时遗漏首尾字符），或**远程地址为 HTTPS 格式却期望走 SSH**。修正地址：

```bash
git remote set-url origin git@github.com:用户名/仓库名.git
```

<a id="s8-5"></a>
### 8.5 `Support for password authentication was removed`

**原因**：在 HTTPS 下输入了账号密码。
**处理**：改用 PAT（见 [2.2](#s2-2)）或改用 SSH（见 [2.1](#s2-1)）。

<a id="s8-6"></a>
### 8.6 `You are in 'detached HEAD' state`

**原因**：checkout 到了某个具体提交的哈希，而非分支。

**处理**：

```bash
# 若在此状态下已产生提交并希望保留：
git switch -c 新分支名

# 若不需保留任何内容，直接回到分支：
git switch main
```

<a id="s8-7"></a>
### 8.7 `Your local changes would be overwritten by merge/checkout`

**原因**：存在未提交的改动，而目标操作会覆盖它们。

**处理**（三种方式任选其一）：

```bash
git stash              # 先收起，操作完成后执行 git stash pop
git commit -m "wip"    # 先提交
git restore 文件        # 放弃这些改动
```

<a id="s8-8"></a>
### 8.8 `fatal: not a git repository`

**原因**：当前目录不是仓库，或不在仓库目录下。

**处理**：

```bash
pwd              # 查看当前路径
ls -a            # 检查是否存在 .git 目录
cd 正确路径
```

<a id="s8-9"></a>
### 8.9 `warning: LF will be replaced by CRLF`

**这是警告而非错误**，可以忽略，属于 Windows 平台换行符转换的正常提示。按 [1.2](#s1-2) 设置 `core.autocrlf true` 即可。

<a id="s8-10"></a>
### 8.10 单文件超过 GitHub 的 100 MB 限制

```
remote: error: File xxx.pth is 120.00 MB; this exceeds GitHub's file size limit of 100.00 MB
```

**原因**：GitHub 单文件硬性上限为 100 MB（超过 50 MB 会给出警告）。

**处理**：

```bash
# 从暂存区移除（保留本地文件）
git rm --cached 大文件
# 将对应规则加入 .gitignore
# 若已经 commit，先撤销该次提交
git reset --soft HEAD~1
git rm --cached 大文件
git commit -m "chore: 排除大文件"
```

**确实需要对大文件做版本管理**（例如预训练权重）时使用 **Git LFS**，见 [10.6](#s10-6)。

<a id="s8-11"></a>
### 8.11 `src refspec main does not match any`

**原因**：本地尚无任何提交，或当前分支名不是 main。

**处理**：

```bash
git log --oneline      # 检查是否有提交，无则先 commit
git branch             # 查看当前分支名
git branch -M main     # 改名为 main
git push -u origin main
```

<a id="s8-12"></a>
### 8.12 `.git/index.lock 文件已存在`

```
fatal: Unable to create '.../.git/index.lock': File exists.
```

**原因**：上一次 git 操作异常中断，遗留了锁文件。

**处理**：确认没有其他 git 进程运行（关闭 VS Code 的 Git 面板、关闭其他终端），然后：

```bash
rm -f .git/index.lock
```

<a id="s8-13"></a>
### 8.13 中文文件名显示为转义字符

例如显示为 `\344\275\240\345\245\275.md`。处理方式：

```bash
git config --global core.quotepath false
```

<a id="s8-14"></a>
### 8.14 Jupyter Notebook 冲突

`.ipynb` 是 JSON 格式，包含输出内容和执行计数。多人或两台设备修改同一 notebook 时极易冲突，且冲突标记**无法正常阅读**。

**预防（推荐做法）：**

```bash
# 提交前自动清除 notebook 输出（需安装 nbstripout）
pip install nbstripout
nbstripout --install
```

配置后提交的 notebook 只含代码不含输出，diff 干净、体积更小、基本不会冲突。

**已经产生冲突时的处理：**

- VS Code 安装 Jupyter 插件后可图形化处理
- 也可执行 `git checkout --theirs xxx.ipynb` 选择其中一方，另一方的代码手动合并
- **更根本的做法**：将核心逻辑写成 `.py` 文件，notebook 仅用于探索

<a id="s8-15"></a>
### 8.15 分叉分支的提示

```
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint:
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
fatal: Need to specify how to reconcile divergent branches.
```

**原因**：Git 2.27 之后的行为变化。当本地与远程各自存在对方没有的提交时，git 不再自动决定采用合并还是变基，而是要求先指定偏好。**这是较新版本 git 最容易造成困惑的提示之一。**

**处理**（一次性配置，推荐第一种）：

```bash
git config --global pull.rebase false    # 采用合并方式，产生一条合并提交，行为最直观
```

配置完成后，遇到分叉直接执行 `git pull` 即可。仅需临时指定时，参见 [8.2](#s8-2) 的 `git pull --no-rebase`。

<a id="s8-16"></a>
### 8.16 当前分支没有上游分支

```
fatal: The current branch main has no upstream branch.
To push the current branch and set the remote as upstream, use
    git push --set-upstream origin main
```

**原因**：本地分支尚未与远程分支建立绑定关系，通常是首次 push 时遗漏了 `-u`。

**处理**：按提示执行即可。

```bash
git push -u origin main     # -u 是 --set-upstream 的简写，只需执行一次
```

此后直接使用 `git push` / `git pull`。

<a id="s8-17"></a>
### 8.17 remote origin already exists

**原因**：已关联过远程仓库，又执行了一次 `git remote add origin`。

**处理**（两种方式任选其一）：

```bash
# 方式 1：仅修改地址（更换仓库名或从 HTTPS 切换为 SSH 时使用）
git remote set-url origin git@github.com:用户名/新仓库名.git

# 方式 2：先删除再重新添加
git remote remove origin
git remote add origin git@github.com:用户名/仓库名.git
```

查看当前关联：`git remote -v`

<a id="s8-18"></a>
### 8.18 nothing to commit

**这不是错误**，意为"没有可提交的改动"。常见于三种情况：

- 确实尚未修改任何文件
- 修改的文件在 `.gitignore` 中，被忽略
- 之前已经提交过

若确认已修改文件却出现该提示，用以下命令排查：

```bash
git status --ignored            # 检查是否被 .gitignore 忽略
git check-ignore -v 你的文件     # 查看具体匹配到的规则
```

<a id="s8-19"></a>
### 8.19 `Too many arguments`

```
$ ssh-keygen -t ed25519 -c "207989701+z723c@users.noreply.github.com"
Too many arguments.
usage: ssh-keygen [-q] [-a rounds] [-b bits] [-C comment] [-f output_keyfile]
                  ...
                  ssh-keygen -c [-a rounds] [-C comment] [-f keyfile] [-P passphrase]
                  ...
```

**含义**：命令收到了一个"没有归到任何选项上"的多余参数。

**本例的真实原因**：`-C` 写成了小写 `-c`。而 `-c` 是 ssh-keygen 的一个**真实选项**（作用是"修改已有密钥的注释"），并且**不接收位置参数**。于是解析结果是：

- `-t ed25519` ✓ 正常
- `-c` ✓ 被当成"修改注释"模式
- `207989701+...` ← **多出来的位置参数** → 报错

**正确写法是大写 `-C`：**

```bash
ssh-keygen -t ed25519 -C "你的注释"
```

**通用排查：**

1. **把报错里的 `usage:` 读完**，找到你用的那个选项，确认它的**准确大小写**、以及它**是否接收参数**
2. 逐个核对每个选项字母
3. 只有在选项全部核对无误后，才去怀疑引号或不可见字符

> **教训**：本例里 `usage:` 已经把答案写在脸上了——`ssh-keygen -c [-a rounds] [-C comment] ...` 就列在输出中——却被跳过了。
> **报错输出里出现 `usage:` 时，它是证据，不是噪音。**

<a id="s8-20"></a>
### 8.20 `Could not resolve hostname`

```
ssh: Could not resolve hostname ssh.github.com: Name or service not known
```

**含义**：ssh 拿到了一个域名，但**解析不出对应的 IP**。

**排查顺序（不要跳到第 4 步）：**

**① 核对域名的拼写。** 这一步最容易跳过，也最容易命中。特别注意 `.` 和 `/`、`-` 和 `_`、`,` 和 `.` 这类**在等宽字体下不易分辨**的字符。

- ✅ `ssh.github.com`
- ❌ `ssh.github/com`、`ssh_githb.com`

**② 确认主机名是哪来的。** 如果来自 `~/.ssh/config` 的 `HostName`，先把该文件做一次字符级校验：

```bash
cat -A ~/.ssh/config
```

期望输出（`$` 是 `cat -A` 添加的行尾标记，不属于文件内容）：

```
Host github.com$
  HostName ssh.github.com$
  Port 443$
  User git$
```

出现 `M-`、`^M`、`^I` 之类的标记，说明混进了不可见字符。

**③ 用 `nslookup` 判断 DNS 本身是否正常：**

```bash
nslookup github.com
nslookup ssh.github.com
```

**④ 只有在①②无误、且③显示 DNS 确实解析不了时**，才考虑改 DNS 或 hosts（见 [8.21](#s8-21)）。

> **诊断信号**：如果**同一个域名"手敲能通、走配置文件不能通"**，那几乎一定是**配置文件里的字符有问题**，而不是网络。
> **永远先怀疑自己写的那份配置，再怀疑网络。**

<a id="s8-21"></a>
### 8.21 hosts 文件：什么时候能用，什么时候是坑

**作用**：`C:\Windows\System32\drivers\etc\hosts`（需管理员权限编辑）可以把一个域名手工绑定到指定 IP，**优先级高于 DNS**。

> ### 动手之前先做第 0 步：盘点机器上已有的网络工具
>
> ```powershell
> tasklist | findstr /i "watt steam atrust sangfor clash v2ray"
> ```
>
> 如果装过 **Steam++（Watt Toolkit）**、**aTrust（深信服）**、Clash 这类软件，它们**本身就在管理 hosts 和本地代理**：
>
> | 软件 | 它在 hosts 里留下的东西 |
> |---|---|
> | Steam++ | 60+ 条 `127.0.0.1` 规则，位于 `# Steam++ Start` 与 `# Steam++ End` 之间；同时有本地进程监听 443 |
> | aTrust | 自动添加的条目（注释里写着 `do not modify`） |
>
> **在它们之上再手工加规则，会产生"谁赢"的不确定性**（本机实测：Windows 采用了文件中靠前的那条），而且一旦出问题极难排查。
>
> 完整的三阶段排查案例见 **[网络问题排查实例](网络问题排查实例.md)**。

**适合用的情形：**

- 已用 `nslookup` **确认**是 DNS 污染或解析失败
- 需要**立刻**恢复使用
- 你清楚这是**临时措施**，并会记录、会回头清理

**不该用的情形：**

- ❌ **还没确认是 DNS 问题就改** —— 这是最常见的误用
- ❌ **给 GitHub 固定 IP** —— GitHub 使用 Azure，IP 会变。硬编码之后，将来 IP 一变，SSH 会以**更难懂的形式**坏掉（连接超时、或主机密钥不匹配的安全告警），而你不会记得自己动过 hosts
- ❌ 改完不记录 —— 半年后完全想不起来系统里埋了这个东西

**GitHub 的官方做法**是发布 IP 段（`https://api.github.com/meta`），并明确不建议硬编码 IP。

**一条判据：**

> **"我按某个方案改了，但报错一模一样"** → 这不是"改得不够"，而是**病因判断错了**。
> 正确反应是**回退**：撤销改动，重新读报错。在原方案上叠加新修法，只会让系统越来越难排查。

**怎么回退**：以管理员权限打开记事本 → 打开 hosts 文件 → 删掉添加的那一行 → 保存。然后重跑原命令，确认行为符合预期。

<a id="s8-22"></a>
### 8.22 命令里的全角空格与弯引号

**这是中文环境下真实存在的陷阱。** 虽然本节开头的案例最后查明是别的原因，但这类问题本身很常见，值得单独记一条。

**症状：**

- `bash: xxx: command not found`，而报错里显示的命令名**看起来完全正常**
- 参数被莫名拆开或粘连
- 引号"不起作用"

**成因**：输入法处于中文状态时——

- 空格 → 全角空格 `U+3000`（bash 不认它作分词符）
- 引号 → 弯引号（U+201C、U+201D、U+2018、U+2019）。它们看起来和 ASCII 的 `"` 和 `'` 几乎一样，**这正是它难被发现的原因**

**它们和正常字符在终端里长得几乎一样**，这是最难的地方。

**排查：**

```bash
cat -A 文件名              # 查看文件里的不可见字符（M- 开头的是非 ASCII 字节）
od -c 文件名                # 逐字节查看
```

**预防（最有效的一条）：**

> **敲命令前先把输入法切到英文**（`Shift` 或 `Ctrl+空格`）。顺手看一眼屏幕右下角的输入法状态。

**另一个实用习惯**：**关键命令手工敲，不要从聊天窗口、网页或 Word 里复制**——复制路径上的"智能标点"转换是这类字符的主要来源。

---

<a id="ch9"></a>
## 9. GitHub 网页端：你还会用到的功能

<a id="s9-1"></a>
### 9.1 仓库页面结构（别人会看什么）

| 区域 | 作用 | 建议 |
|---|---|---|
| **仓库名** | 项目的标识 | 别用 `test`、`study`、`111` 这种 |
| **About**（右上角齿轮） | 一句话简介与主题标签 | 应当填写。主题标签有助于被检索到 |
| **README** | 别人对项目的首要判断 | 开头一句话说清是什么，有截图更好 |
| **提交历史**（commits） | 反映开发的持续性 | 保持每周有提交 |
| **语言统计条** | 技术栈构成 | 自动生成 |
| **Star 数** | 他人对该项目的认可度 | 优质项目会自然增长 |

<a id="s9-2"></a>
### 9.2 Issues：给自己建任务

网页端 → Issues → New issue。你可以把它当待办清单用：

- `[ ] 补 CLIP 论文笔记`
- `[ ] 复现 MVP-CBM`
- `[ ] 修 train_loop 中验证集 shuffle 的问题`

关闭 issue 时写一句结论，这些记录本身就是"我做过什么"的证据。

<a id="s9-3"></a>
### 9.3 Pull Request：给开源提 PR 的完整流程

标准流程（以修一个文档错别字为例）：

```bash
# ① 在网页端点击 Fork（右上角），将他人仓库复制到你的账号下
# ② 克隆你的 fork
git clone git@github.com:你的用户名/原仓库名.git
cd 原仓库名

# ③ 添加上游仓库，便于后续同步原作者的最新代码
git remote add upstream git@github.com:原作者/原仓库名.git

# ④ 创建专门的分支（不要直接在 main 上修改）
git switch -c fix-typo-in-readme

# ⑤ 修改并提交
git add .
git commit -m "docs: 修正 README 中的拼写错误"

# ⑥ 推送到你的 fork
git push origin fix-typo-in-readme

# ⑦ 网页端会出现 "Compare & pull request" 按钮，点击后
#    说明改动内容、改动原因与验证方式
```

**注意事项：**

- 一个 PR 只处理一件事，不做顺带修改
- 先阅读项目的 `CONTRIBUTING.md`
- 提交信息遵循项目惯用的语言和风格
- 维护者可能需要数周才回复，属正常情况

<a id="s9-4"></a>
### 9.4 Actions：自动检查

仓库 → Actions 标签页。创建 `.github/workflows/check.yml` 后，每次 push 会自动执行检查：

```yaml
name: check
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install ruff
      - run: ruff check .
```

**实际价值**：项目 P0/P1 配置该文件后，README 上会显示构建状态徽章，可作为工程规范的体现。

<a id="s9-5"></a>
### 9.5 Releases 与 Tags：标记版本

```bash
git tag -a v1.0.0 -m "完成可解释诊断模块"
git push origin v1.0.0
```

网页端 → Releases → 基于 tag 发布并附说明。**项目达到可交付程度时打一个 tag**，比长期沿用 "final_final_v2" 之类的命名更规范。

<a id="s9-6"></a>
### 9.6 GitHub Pages：免费放你的 Demo

仓库 → Settings → Pages → 选择分支和目录。可用于托管：

- 在线简历
- 项目 Demo 的说明页
- 学习笔记的网页版

**简历中附上 `你的用户名.github.io` 链接是有效的加分项。**

<a id="s9-7"></a>
### 9.7 Profile README：你的门面

新建一个**与用户名完全同名**的仓库（例如用户名为 `zhangsan`，则创建 `zhangsan`），其中的 README 会显示在个人主页顶部。

内容示例：

```markdown
### 张三 ｜ 信息与通信工程硕士在读

研究方向：医学影像 × 视觉-语言模型 × 可解释性 AI

- 正在开展：基于概念瓶颈的可解释医学多模态诊断
- 学习笔记：[ml-learning-notes](换成你的仓库地址)
- 联系方式：邮箱

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=你的用户名)
```

**注意不要写"热爱技术、学习能力强"这类空话**，写具体在做什么。

<a id="s9-8"></a>
### 9.8 在网页上直接改文件

任意文件页面右上角有铅笔图标，点击可在线编辑，提交前在页面底部填写提交说明。临时改 README 很方便，**但记得回本地 `git pull`**，否则下次 push 会冲突（见 [8.2](#s8-2)）。

<a id="s9-9"></a>
### 9.9 其他功能

| 功能 | 用途 |
|---|---|
| **Star** | 收藏他人项目；Star 列表可反映技术关注方向 |
| **Fork** | 复制他人仓库到自己的账号 |
| **Watch** | 订阅更新通知 |
| **Insights → Traffic** | 查看仓库访问量 |
| **Settings → Danger Zone** | 修改仓库可见性 / 删除仓库（删除需输入仓库名确认） |

---

<a id="ch10"></a>
## 10. 进阶：以后需要再回来

<a id="s10-1"></a>
### 10.1 rebase

```bash
git rebase main                # 将当前分支的提交移至 main 最新提交之后
git rebase -i HEAD~3           # 交互式整理最近 3 条提交（合并、修改说明、删除）
git rebase --continue          # 解决冲突后继续
git rebase --abort             # 放弃
```

**铁律：只对没有 push 过的提交做 rebase。**

<a id="s10-2"></a>
### 10.2 cherry-pick

```bash
git cherry-pick a1b2c3d        # 将指定提交的内容复制到当前分支
```

<a id="s10-3"></a>
### 10.3 bisect

用于二分定位引入缺陷的提交。

```bash
git bisect start
git bisect bad                 # 当前版本存在问题
git bisect good a1b2c3d        # 该历史版本正常
# git 会自动切换到中间版本，测试后标记 good 或 bad，重复直至定位
git bisect reset               # 结束
```

<a id="s10-4"></a>
### 10.4 多远程仓库

```bash
git remote add gitee git@gitee.com:用户名/仓库名.git
git push origin main           # 推送到 GitHub
git push gitee main            # 推送到 Gitee
```

<a id="s10-5"></a>
### 10.5 子模块 submodule

当一个项目要引用另一个仓库时用。**初学者尽量避免**，容易出错。替代方案：把依赖写进 `requirements.txt` 或用包管理。

<a id="s10-6"></a>
### 10.6 Git LFS

适合模型权重、数据集样本（**医学数据仍然不建议，即使是 LFS**）。

```bash
git lfs install
git lfs track "*.pth"
git add .gitattributes
```

> **注意**：GitHub 免费额度的 LFS 存储与流量有限（1 GB 存储 / 1 GB 月流量），超出需付费。

<a id="s10-7"></a>
### 10.7 worktree

```bash
git worktree add ../项目-实验分支 feature-x
```

适合"主分支跑着长训练，同时在另一个目录改代码"的场景。

---

<a id="ch11"></a>
## 11. 你的专属工作流

<a id="s11-1"></a>
### 11.1 笔记仓库的日常流程

每次学习结束时执行：

```bash
cd /c/Users/13127/Documents/ml-learning-notes     # 替换为你的仓库路径

git status                       # 查看改动
git add .                        # 或 git add python/01-basics/
git commit -m "notes(python): 补充变量是引用而非拷贝"
git push
```

> 小技巧：在仓库文件夹里右键选 **Git Bash Here**，就不用每次敲 `cd` 了。

**四条纪律：**

1. 每次学习结束就提交，不要攒
2. 一次提交只做一件事
3. 提交说明写"为什么/改了什么"，不写"更新"
4. 记录耗时不超过学习时间的 20%

<a id="s11-2"></a>
### 11.2 项目仓库的流程

```bash
# 开始一个新功能
git switch -c feat/add-augmentation

# 编写代码、测试
git add .
git commit -m "feat: 加入 RandAugment 数据增强，验证集准确率 +1.2%"

# 合并回 main
git switch main
git merge feat/add-augmentation
git push
git branch -d feat/add-augmentation

# 达到里程碑时打 tag
git tag -a v0.1.0 -m "首个可用版本：ResNet-18 + 基础增强"
git push origin v0.1.0
```

<a id="s11-3"></a>
### 11.3 开源贡献流程

流程见 [9.3](#s9-3)。**第一个 PR 建议挑文档类的小问题**（错别字、失效链接、补充示例），门槛低、容易通过，先把流程跑通。

适合起步的仓库：

- **MONAI** —— 医学影像框架，补文档、修小缺陷
- **nnU-Net、MedMNIST** —— 处理 issue、补充示例
- **你复现过的论文仓库** —— 报告复现问题、提交改进

<a id="s11-4"></a>
### 11.4 每周维护例程

```bash
git pull                           # 同步（若更换过设备或在网页端修改过）
git log --oneline --graph -20       # 查看本周产出
```

随后在 GitHub 网页端确认：

- 本周的贡献记录是否连续
- README 中的进度勾选是否已更新
- Issues 中的待办是否可以关闭若干条

---

<a id="ch12"></a>
## 12. 换电脑 / 多台机器

<a id="s12-1"></a>
### 12.1 先记住结论

**更换电脑时，只有三类内容会丢失：**

1. **尚未 push 的提交**（已在本地 commit 但未上传）
2. **stash 中的内容**（`git stash` 保存的内容仅存在于本机）
3. **被 `.gitignore` 排除的文件**（数据集、模型权重、`.env`、密钥）

其他所有东西都在 GitHub 上，新电脑 `git clone` 一下就全回来了。所以换电脑本身不难，难的是别在那三样上翻车。

<a id="s12-2"></a>
### 12.2 什么跟着走，什么不跟着走

| 内容 | clone 后是否存在 | 说明 |
|---|---|---|
| 全部提交历史 | ✅ 有 | 完整恢复 |
| 已推送的分支 | ✅ 有 | |
| 已推送的 tag | ✅ 有 | |
| 远程地址配置 | ✅ 有 | clone 会自动配置 origin |
| **未推送的提交** | ❌ **无** | 仅存在于原设备的 `.git` 中 |
| **未推送的分支** | ❌ **无** | |
| **本地 tag（未 push）** | ❌ **无** | |
| **stash** | ❌ **无** | stash 属于本机引用，不会被 push |
| **未跟踪的新文件** | ❌ **无** | 从没 `git add` 过的文件，git 完全不认识 |
| **未提交的改动** | ❌ **无** | |
| **`.gitignore` 中的文件** | ❌ **无** | 数据、权重、`.env` 需另行拷贝 |
| SSH key | ❌ 无 | 需重新生成或拷贝 |
| git config（user.name 等） | ❌ 无 | 需重新配置 |
| `.gitignore_global` | ❌ 无 | 需重新创建 |
| 已保存的 GitHub 凭据 | ❌ 无 | 新设备需重新认证一次 |

<a id="s12-3"></a>
### 12.3 换机前：在旧电脑上自查（10 分钟）

**每个仓库都跑一遍这几条**，确认没有东西会丢：

```bash
# ① 最重要的一条：列出所有"本地有、远程没有"的提交
git log --branches --not --remotes --oneline
# 输出为空 = 安全；有输出 = 这些提交不 push 就会丢

# ② 看每个分支有没有对应的远程分支
git branch -vv
# 注意看有没有 [origin/xxx] 标记。没有标记的分支就是没推送过

# ③ 检查 stash
git stash list
# 若有内容，执行 git stash pop 取出并提交，或导出为补丁文件：
#   git stash show -p > stash.patch

# ④ 看有没有未提交/未跟踪的文件
git status --porcelain -uall
# 输出为空 = 干净

# ⑤ 看有没有没推送的 tag
git tag
git ls-remote --tags origin     # 对比一下远程有哪些
```

**确认后，一次性推送全部可推送内容：**

```bash
git push --all origin      # 推送所有本地分支
git push --tags            # 推送所有 tag
```

> ⚠️ **不要用 `git push --mirror`。** 它不只推送，还会**删掉远程上本地没有的分支和 tag**。没完全搞懂它之前不要碰。

**然后单独备份被忽略的文件**（这些 git 不管，但你可能需要）：

- 数据集样本、模型权重（`*.pth`）
- `.env` 或配置文件中的密钥
- 本地编写的临时脚本（若重要，先 `git add` 提交）

用一个移动硬盘或网盘拷走。**医学数据注意合规，不要走公有网盘。**

**顺手备份两样东西**（拷到新电脑能省事）：

- `C:\Users\你的用户名\.gitignore_global`
- `C:\Users\你的用户名\.ssh\config`（若曾配置）

<a id="s12-4"></a>
### 12.4 新电脑：四步配置

**第 1 步｜安装 Git** —— 见 [1.1](#s1-1)

**第 2 步｜配置身份信息** —— 见 [1.2](#s1-2)

```bash
git config --global user.name "你的名字"
git config --global user.email "你的GitHub注册邮箱"
git config --global init.defaultBranch main
git config --global core.quotepath false
git config --global core.autocrlf true
git config --global credential.helper manager
```

**第 3 步｜配置 SSH key**

⚠️ **建议在新电脑上重新生成一把，而不是拷旧私钥。** 理由：每台机器一把 key，将来某台不用了（卖掉、还给实验室），你可以在 GitHub 上单独撤销那一把，不影响其他机器。

```bash
ssh-keygen -t ed25519 -C "你的GitHub邮箱"    # 连续回车三次
cat ~/.ssh/id_ed25519.pub                     # 复制输出
```

粘贴到 GitHub → Settings → SSH and GPG keys → New SSH key，Title 建议标明设备（例如 `实验室台式机` / `个人笔记本`）。

```bash
ssh -T git@github.com        # 验证
```

**旧电脑不再用的时候**，记得回 GitHub 把那把对应的 key 删掉，并格式化/销毁旧硬盘。

**第 4 步｜克隆仓库**

```bash
mkdir -p /c/Users/你的用户名/Documents/repos
cd /c/Users/你的用户名/Documents/repos

git clone git@github.com:你的用户名/ml-learning-notes.git
git clone git@github.com:你的用户名/cifar10-pytorch.git      # 其他仓库一并克隆
```

如果仓库用了 Git LFS，**必须在 clone 之前**装好：

```bash
git lfs install        # 先安装
git clone <url>        # 再克隆，否则大文件会变成指针文本
```

<a id="s12-5"></a>
### 12.5 两种迁移方式：clone 还是直接拷文件夹

|  | `git clone`（推荐） | 直接复制整个文件夹 |
|---|---|---|
| 历史与分支 | ✅ 完整 | ✅ 完整 |
| **stash** | ❌ 丢失 | ✅ **保留** |
| **未推送的提交** | ❌ 丢失 | ✅ **保留** |
| 未跟踪文件 | ❌ 丢失 | ✅ 保留 |
| 凭据残留 | ✅ 干净 | ⚠️ 可能携带旧设备配置 |
| 适用场景 | 有网络且已全部 push | **无网络、或存在无法推送的内容** |

**结论：正常情况用 `clone`。** 只有当你有推不上去的东西（比如在内网），才直接拷文件夹——因为 `.git` 目录里装着全部本地状态。

> 拷文件夹时检查一下 `仓库/.git/config` 里有没有明文写着的 token（如果曾经用 `https://用户名:token@github.com/...` 这种地址配过远程）。有的话改成纯地址。

<a id="s12-6"></a>
### 12.6 没网络怎么办：用 git bundle 打包

如果新电脑暂时上网不方便，可以用 `bundle` 把整个仓库打成**一个文件**，用 U 盘搬过去：

```bash
# 旧电脑：打包（包含所有分支和 tag）
git bundle create ml-notes.bundle --all

# 检查打包文件是否完整
git bundle verify ml-notes.bundle

# 新电脑：从 bundle 克隆（用法和 clone 远程一样）
git clone ml-notes.bundle ml-learning-notes
cd ml-learning-notes

# 之后再把远程地址配上，就能正常 push 了
git remote set-url origin git@github.com:你的用户名/ml-learning-notes.git
git push
```

<a id="s12-7"></a>
### 12.7 你最可能遇到的真实场景：三台机器

你的实际工作流大概率是这三个地方：**个人笔记本**（看课、写笔记、写论文）、**实验室台式机**（跑实验）、**实验室服务器**（长训练）。

| 设备 | 主要用途 | 认证方式 | 注意事项 |
|---|---|---|---|
| 个人笔记本 | 学习笔记、论文写作 | SSH key | 每次结束前 `push` |
| 实验室台式机 | 实验、调参 | SSH key（独立一把） | 每次开始前 `pull` |
| 实验室服务器 | 长训练、批量实验 | **Deploy key（只读）** 或 HTTPS + PAT | 不要在脚本中硬编码 token |

**服务器上的做法**（服务器通常多人共用，不要把自己的账号 key 放上去）：

GitHub 仓库 → Settings → **Deploy keys** → Add deploy key → 粘贴一把**专为服务器生成的**密钥，**不勾选** Allow write access（只读就够，因为服务器只负责拉代码跑实验）。这样即使 key 泄露，也只能读不能改。

**服务器上的工作循环：**

```bash
cd /path/to/repo
git pull                    # 开始前拉最新代码
# ...跑实验...
# 结果不要提交（写进 .gitignore），只提交代码改动
git add .
git commit -m "feat: 加入 Dice Loss 对比实验配置"
git push                    # 只在需要保存配置改动时推
```

**铁律：服务器上不要提交实验输出。** 结果文件、日志、checkpoint 全部写进 `.gitignore`，只提交代码和配置。

<a id="s12-8"></a>
### 12.8 治本：让"换电脑"不再是问题

只要坚持三条习惯，换电脑就退化成"装 Git → 配 key → clone"三步：

1. **每次学习/工作结束前 `git push`。** 未推送的提交是唯一会真丢的东西，而它只在你偷懒的这一天里存在。
2. **每次换机器开始工作前 `git pull`。** 避免两边分叉，减少冲突。
3. **不要用 stash 跨机器。** stash 是本机的。要么当场处理掉，要么提交到一条临时分支：`git stash pop && git add . && git commit -m "wip" && git push`。

另外：**密钥和 `.env` 不要靠"存在某台电脑上"，放进密码管理器**（1Password / Bitwarden / KeePass）。这样换任何机器都不慌。

<a id="s12-9"></a>
### 12.9 换机检查清单

**原设备（离开前）**

- [ ] 每个仓库执行 `git status`，确认工作区干净
- [ ] 每个仓库执行 `git log --branches --not --remotes --oneline`，输出为空
- [ ] 每个仓库执行 `git branch -vv`，所有分支均带 `[origin/...]` 标记
- [ ] `git stash list` 为空
- [ ] 执行 `git push --all origin` 与 `git push --tags`
- [ ] 备份 `.gitignore` 中排除的数据 / 权重 / `.env`
- [ ] 备份 `~/.gitignore_global` 与 `~/.ssh/config`
- [ ] 检查 `.git/config` 是否存在明文 token
- [ ] 若设备不再使用，到 GitHub 删除其 SSH key
- [ ] 若设备需要转让，彻底擦除磁盘（`.ssh` 与 `Documents` 目录）

**新设备（开始使用后）**

- [ ] 安装 Git 与 VS Code
- [ ] 配置 6 条 `git config --global`
- [ ] 生成 SSH key 并添加到 GitHub（Title 标明设备名）
- [ ] 执行 `ssh -T git@github.com` 验证通过
- [ ] 恢复 `.gitignore_global`
- [ ] 克隆全部仓库
- [ ] 将备份的数据 / 权重 / `.env` 放回对应位置
- [ ] 修改任一文件，完整执行一次 `add` / `commit` / `push`，确认流程通畅

---

<a id="apxa"></a>
## 附录 A：一页速查表

### 配置（一次性）

```bash
git config --global user.name "名字"
git config --global user.email "邮箱"
git config --global init.defaultBranch main
git config --global core.quotepath false
git config --global core.autocrlf true
git config --global credential.helper manager
```

### 新建与连接

```bash
git init                                    # 本地初始化
git clone <url>                             # 克隆远程仓库
git remote add origin <url>                 # 关联远程仓库
git remote -v                               # 查看远程仓库
git remote set-url origin <url>             # 修改远程地址
git branch -M main                          # 分支改名
git push -u origin main                     # 首次推送并建立绑定
```

### 日常操作

```bash
git status                     # 状态
git add .                      # 暂存全部改动
git add <文件>                  # 暂存指定文件
git commit -m "说明"            # 提交
git push                       # 推送
git pull                       # 拉取
git log --oneline --graph -10   # 查看历史
git diff                       # 查看未暂存的改动
git diff --cached              # 查看已暂存、待提交的改动
```

### 分支

```bash
git branch                    # 列出分支
git switch -c <名>            # 新建并切换
git switch <名>               # 切换分支
git merge <名>                # 合并到当前分支
git branch -d <名>            # 删除分支
git push origin <名>          # 推送分支
```

### 撤销

```bash
git restore <文件>                 # 🔴 丢弃未暂存改动（不可恢复）
git restore --staged <文件>        # 🟢 取消暂存（内容保留）
git commit --amend -m "新说明"     # 🟡 修改上一条提交说明（未 push）
git reset --soft HEAD~1            # 🟡 撤销提交，改动保留在暂存区
git reset --mixed HEAD~1           # 🟡 撤销提交，改动放回工作区（默认）
git reset --hard HEAD~1            # 🔴 撤销提交并丢弃改动
git revert <哈希>                  # 🟢 反向提交，用于已 push 的情况
git reflog                         # 🟢 找回丢失的提交
git stash / git stash pop          # 🟢 临时暂存
```

### 诊断

```bash
git status
git log --oneline --graph --all
git show <哈希>                 # 查看某次提交的具体改动
git blame <文件>                # 查看每行的最后修改者
git check-ignore -v <文件>       # 查询文件被忽略的规则
git ls-files                    # 列出全部被跟踪的文件
ssh -T git@github.com           # 测试 GitHub 认证
```

---

<a id="apxb"></a>
## 附录 B：我该敲哪条（决策树）

```
我要开始一次学习/开发
├─ 是第一次？ ────────────→ git init / git clone + 1.2 节配置
└─ 否
   ├─ 换了电脑或在网页上改过？ → git pull
   └─ 直接开始

我写完了内容
├─ 想看看改了啥 ───────────→ git status, git diff
├─ 只想提交部分文件 ────────→ git add <具体文件>
└─ 全部提交 ──────────────→ git add . && git commit -m "..." && git push

push 被拒绝
└─ git pull --rebase → 解决冲突 → git push

我搞砸了
├─ 还没 add ──────────────→ git restore <文件>
├─ add 了没 commit ────────→ git restore --staged <文件>
├─ commit 了没 push ───────→ git commit --amend（只改说明）
│                            git reset --soft HEAD~1（要拆开重做）
├─ commit 并且 push 了 ────→ git revert <哈希> && git push
└─ 用了 --hard 弄丢了 ─────→ 别动！git reflog 找回

我提交了不该提交的
├─ 只是垃圾/大文件 ────────→ git rm --cached → 加 .gitignore → commit
└─ 是密钥/隐私/医学数据 ───→ ① 立刻作废密钥
                              ② pip install git-filter-repo
                              ③ git filter-repo --path X --invert-paths
                              ④ git push --force

我想用分支
└─ 试一个可能失败的改动 / 给开源提 PR → git switch -c <名>

我卡住了
└─ ① git status ② git log --oneline -5 ③ 查第 8 章
   ④ 还不行就 git stash 后重来
```

---

<a id="principles"></a>
## 最后三条心法

**1. Git 几乎不会真的丢东西。** 除了 `restore` 丢弃的未暂存改动、以及 `reset --hard` 之后又做了别的操作，其他情况基本都能用 `reflog` 找回。所以敢试、敢改。

**2. 敲危险命令前先 `git status`。** 确认自己在哪个分支、有什么没提交。这个习惯能避免 90% 的事故。

**3. 提交历史是你的第二份简历。** 别人看你的 GitHub，看的不只是代码质量，还有**你有没有持续在做事**。断断续续的 20 次提交，比一次性上传 200 个文件有说服力得多。

---

*手册版本 1.5 ｜ 建立于 2026-10-14 ｜ 建议存放于笔记仓库 `docs/git-manual.md`*

**修订记录**

- **v1.5**：[8.21](#s8-21) 增加「动手前先盘点机器上已有的网络工具」一节（Steam++ / aTrust / Clash 会在 hosts 和本地代理上留下自己的规则）；[8.0](#s8-0) 增加延伸阅读链接。新增独立文档：**[网络问题排查实例](网络问题排查实例.md)**（SSH 报错 → DNS 失败 → 浏览器 SSL 错误的三阶段因果链复盘）。
- **v1.4**：新增 [8.0 排查顺序](#s8-0)（把"先读证据再猜"固化为流程）；新增 [8.19 `Too many arguments`](#s8-19)（选项大小写写错的真实案例）、[8.20 `Could not resolve hostname`](#s8-20)（先查域名拼写，再查 DNS）、[8.21 hosts 文件](#s8-21)（何时可用、何时是坑、怎么回退）、[8.22 全角空格与弯引号](#s8-22)。以上四节均来自 2026-10-15 的真实踩坑。
- **v1.3**：措辞重新校准——恢复生动的标题与口语化表达（因手册主要供自用），同时保留可点击目录与全部技术内容的精确性。
- **v1.2**：目录改为可点击跳转（采用显式锚点，并增加场景索引）；全文语气统一为技术文档表述；为全部章节与子节添加锚点。
- **v1.1**：修正 7.4 节 `git reset --soft` 与 `--mixed` 的效果描述错误（`--soft` 保留在**暂存区**，`--mixed` 放回**工作区**），并补充三种模式对照表；修正 7.1 节 `git restore <文件>` 的危险等级（由 🟢 改为 🔴）；新增第 12 章「迁移与多机器协作」；新增 0.6 节（origin / main / 提交哈希）、4.6 节（删除、重命名与特殊文件名）、8.15–8.18（四条新版 Git 常见提示）；快速上手补充第 0 步（注册账号）；1.1 节补充 Git Bash 打开方式与路径写法；3.1 节补充仓库地址获取方式；7.6 节补充提交哈希的获取方式。
- **v1.0**：初版。
