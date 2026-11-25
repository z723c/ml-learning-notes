# 网络问题排查实例：从 SSH 报错到 GitHub 打不开

> **事件时间**：2026-10-15
> **一句话价值**：这三个阶段看起来是三个独立故障，实际是**同一条因果链**——
> 每一个"针对错误病因的修复"，都变成了下一阶段的问题来源。
>
> **相关文档**：[Git 与 GitHub 操作手册](git-manual.md) 第 8 章

---

## 0. 结论速览

| 阶段 | 症状 | 真因 | 修法 |
|---|---|---|---|
| A | `ssh-keygen` 报 `Too many arguments` | `-C` 写成了小写 `-c` | 改成 `-C`，或直接省略 |
| B | `Could not resolve hostname ssh.github.com` | `~/.ssh/config` 里写成 `ssh.github/com`（斜杠而非点） | 改回 `.com` |
| C | 浏览器 `ERR_SSL_PROTOCOL_ERROR`，GitHub 打不开 | hosts 里 `20.205.243.160 GitHub.com` 把**网页域名**指向了**SSH 端点** | 删掉手工加的 hosts 条目 |

**三个阶段有一个共同点：真因都在"我们自己的文件里"，而不在网络环境。** 但每一阶段的初始判断都指向了外部。

---

## 1. 关键背景：这台机器上已有的"网络改写者"

**这一节是整份复盘最重要的部分。** 这台机器在排查开始前就已经装了三个会修改网络行为的软件，而它们**一开始没有被盘点**：

| 软件 | 它做了什么 | 在本机留下的痕迹 |
|---|---|---|
| **Steam++（Watt Toolkit）** | 网络加速器。原理是把被墙的域名写进 hosts 指向 `127.0.0.1`，再由自己的**本地 443 代理**接管转发 | hosts 里 60+ 条 `127.0.0.1` 规则，`Steam++.Accelerator.exe` 监听 `0.0.0.0:443` |
| **aTrust（深信服）** | 校园网/企业零信任客户端，会装本地代理、干预流量 | hosts 里自动加的条目，4 个 `aTrust*.exe` 常驻进程 |
| **历史 hosts 规则** | 之前为其他目的添加的屏蔽项 | 例如 `127.0.0.1 download.endnote.com` |

> ### 教训 ①
> **动系统级网络配置之前，先盘点机器上已有哪些网络工具。**
> 否则你就是在别人已经改过的文件上再叠一层——不出问题时没事，一出问题就极难排查。
> 检查命令：
> ```powershell
> tasklist | findstr /i "watt steam atrust sangfor clash v2ray"
> ```

---

## 2. 三个阶段

### 阶段 A｜`ssh-keygen` 报 `Too many arguments`

**操作**

```bash
ssh-keygen -t ed25519 -c "207989701+z723c@users.noreply.github.com"
```

**报错**

```
Too many arguments.
usage: ssh-keygen [-q] [-a rounds] [-b bits] [-C comment] [-f output_keyfile]
                  [-m format] [-N new_passphrase] [-0 option]
                  [-t dsa | ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa]
                  [-w provider] [-Z cipher]
                  ...
                  ssh-keygen -c [-a rounds] [-C comment] [-f keyfile] [-P passphrase]
                  ...
```

**误判方向（错了四次）**

引号被转成弯引号 → Unicode 全角空格 → 短破折号 → 隐藏字符。**全都是字符编码方向的猜测。**

**真因**

`-C` 写成了小写 `-c`。

关键在于：**`-c` 是一个真实存在的选项**（作用是"修改已有密钥的注释"），而且它**不接收位置参数**。所以解析结果是：

| 参数 | 解析结果 |
|---|---|
| `-t ed25519` | ✓ 正常 |
| `-c` | ✓ 被当成"修改注释"模式 |
| `207989701+...` | ✗ **多出来的位置参数** → 报错 |

**证据其实就在屏幕上。** usage 输出的第二块里明确列着：

```
ssh-keygen -c [-a rounds] [-C comment] [-f keyfile] [-P passphrase]
```

它同时说明了两件事：`-c` 是合法选项；而且它的子选项才是 `-C comment`。

**修法**

```bash
ssh-keygen -t ed25519 -C "你的注释"
```

或者干脆**省略 `-C`**——注释只是给人看的标签，GitHub 认证不看它：

```bash
ssh-keygen -t ed25519
```

> ### 教训 ②
> **报错里出现 `usage:` 时，它是证据，不是噪音。**
> 排查"多出参数"类报错的第一步，永远是对照 usage 核对你用的**每一个选项**：
> **字母对不对、大小写对不对、它接不接参数。**

---

### 阶段 B｜`Could not resolve hostname`

**前置条件**

GitHub 的 SSH 22 端口被拒（`Connection refused`），所以决定改走 GitHub 官方支持的 `ssh.github.com:443`。为了一劳永逸，把配置写进了 `~/.ssh/config`：

```
Host github.com
  HostName ssh.github.com
  Port 443
  User git
```

**报错**

```
ssh: Could not resolve hostname ssh.github.com: Name or service not known
```

**误判方向**

- 我的判断：配置文件里混进了不可见字符（**方向对了一半**）
- 用户的判断：DNS 问题

**中途方案（这一步埋下了阶段 C 的雷）**

用户执行了：`ping` / `nslookup` 拿到 IP → 修改 hosts 固定 `ssh.github.com` → **还是同样的报错**。

**决定性信号**

> **手敲 `ssh -T -p 443 git@ssh.github.com` 能通，走配置文件不能通。**

**真因**

`~/.ssh/config` 里写的是 `ssh.github/com` —— **斜杠而不是点**。

**为什么改 hosts 完全无效**

带 `/` 的"主机名"在 `getaddrinfo` 阶段就直接失败了，**根本不会去查 hosts 文件**。所以"加了 IP 却没生效"是必然的。

**修法**：把 `/` 改回 `.`。

> ### 教训 ③
> **"我按某个方案修了，但报错一模一样" → 这不是"修得不够"，而是病因判断错了。**
> 正确反应是**回退**：撤销改动，重新读报错。在原方案上叠加新修法，只会让系统越来越难排查。
>
> ### 教训 ④
> **同一个域名"手敲能通、走配置文件不能通" → 几乎一定是配置文件里的字符问题，不是网络。**
> 这个不对称性极有诊断价值：手敲和读文件走的是同一条网络路径，唯一变量就是字符。
>
> ### 教训 ⑤
> **"我加了 IP 却没生效" —— 这句本身就是证据：说明压根没走到 DNS 查询。**
> 排查时要把"修复无效"当作一条线索，而不是继续加修法。

---

### 阶段 C｜浏览器 `ERR_SSL_PROTOCOL_ERROR`

**现象**

GitHub 网页突然打不开，报"此站点的连接不安全 / github.com 发送了无效的响应"，错误码 `ERR_SSL_PROTOCOL_ERROR`。

**用户的怀疑**：是不是刚才删 hosts 条目删坏的？

**第一次判断（逻辑排除）**

你删掉的是 `ssh.github.com` 的条目，而浏览器访问的是 `github.com`，**它从来不查那个条目**。而且"删除 hosts 条目"这个动作本身只会**恢复默认 DNS 行为**，不可能凭空制造解析错误。

**但要求先查一件事：hosts 文件里到底还剩什么。** ← 这一步是关键

结果：**三行手工条目全都还在**，包括一行我们完全不知道的：

```
20.205.243.160 ssh.github.com
20.205.243.160 GitHub.com        ← 就是它
20.205.243.160 ssh.github.com
```

**三条独立证据**

**证据 1｜`ping -n 1 github.com` → `20.205.243.160`**

注意**不是 `127.0.0.1`**。说明 hosts 里手写的那条**排在 Steam++ 的 `127.0.0.1 github.com` 前面，赢了**。（本次观察到 Windows 采用了靠前的那条规则。）

**证据 2｜`20.205.243.160` 是 `ssh.github.com` 的 IP，不是 `github.com` 的**

第一次连 SSH 时终端里就印着：

```
The authenticity of host '[ssh.github.com]:443 ([20.205.243.160]:443)' can't be established.
```

**证据 3｜`curl -I https://github.com`**

```
curl: (35) schannel: failed to receive handshake, SSL/TLS connection failed
```

"failed to receive handshake" = TCP 连上了，但**对方没有回一个合法的 TLS 握手包**。

**真因**

**`20.205.243.160 GitHub.com` 这一行，把网页域名 `github.com` 指向了 SSH 端点。**

那个端口的 443 上跑的是 **SSH 服务**，不是 HTTPS 服务。浏览器发出 TLS ClientHello，对面按 SSH 协议响应——**这就是 `ERR_SSL_PROTOCOL_ERROR` 的字面含义**：TCP 通了，TLS 谈不成。

**旁证（确认 Steam++ 是正常的，被我们绕过了）**

```powershell
netstat -ano | findstr :443
#   TCP    0.0.0.0:443    LISTENING    15708

tasklist | findstr /i "watt"
#   Steam++.Accelerator.exe    15708    ← PID 对上了
```

Steam++ 正在运行、本地代理工作正常。**它是被那行 pin 绕过去的，不是它坏了。**

**修法**

管理员权限编辑 `C:\Windows\System32\drivers\etc\hosts`，删掉手工加的三行（`# Steam++ Start ... End` 那一段**不要动**）。

**为什么删了 pin，SSH 还能通**

SSH 靠的是 `~/.ssh/config` 里的 `HostName ssh.github.com`，然后由 **DNS** 解析出 IP。最早那次成功的 `ssh -T -p 443 git@ssh.github.com` 就是纯靠 DNS 解析到 `20.205.243.160` 的——**那三行 pin 从头到尾都是多余的。**

> ### 教训 ⑥
> **域名要逐字符核对。**
> `.` 和 `/`、`-` 和 `_`、`,` 和 `.` 在等宽字体下很难分辨。
> 核查命令：`cat -A ~/.ssh/config`（`M-`/`^M`/`^I` 标记会暴露异常字符）
>
> ### 教训 ⑦
> **错误的修复不会自己消失，它会以一个新问题的形式回来。**
> 本阶段的三行 hosts，正是阶段 B 排查时加的；而阶段 B 的真因是纯字符错误，跟 DNS 和 hosts 毫无关系。
> **为一个不存在的病因做的修复，会在别处以更难懂的方式爆发。**

---

## 3. 因果链（闭环）

```
【起点】未盘点机器上已有的网络工具
        （Steam++ / aTrust / 历史 hosts 规则）
              │
              │  在一个"已被别人改过"的 hosts 上作业
              ▼
阶段 A  ── 选项大小写写错（-c / -C）
        └→ 误判为引号/编码问题 ──→ 换单引号绕过
                                   （任务继续了，但真因没被理解）

阶段 B  ── 域名写成 ssh.github/com
        └→ 报 DNS 解析失败
              ├→ 误判为 DNS 问题 ──→ 改 hosts 固定 IP ──→ 无效
              │                                          │
              │                                          └─→ 【埋雷】写入 3 行 hosts
              │                                              其中一行指向了网页域名
              └→ 观察到"手敲能通 / 配置不能通" ──→ 发现斜杠，修好

阶段 C  ── 阶段 B 埋的雷爆发
        └→ 网页域名被指向 SSH 端点 ──→ 浏览器 ERR_SSL_PROTOCOL_ERROR
              └→ 三条独立证据收敛 ──→ 定位到那一行 ──→ 删除
```

**闭环之处**：阶段 C 的问题，是阶段 B **针对一个不存在的病因所做的修复**留下的副作用。而阶段 B 的病因（斜杠）从头到尾都不需要碰 hosts。

---

## 4. 可迁移的判据（最值钱的部分）

| # | 判据 | 用在哪 |
|---|---|---|
| 1 | 报错带 `usage:` → **先对照它核对选项的字母、大小写、是否接收参数** | 任何命令的"参数类"报错 |
| 2 | **"修了没用" ≠ 修得不够，而是病因判断错了** → 回退，重新读报错 | 任何排查 |
| 3 | **同一域名"手敲能通、走配置不能通" → 配置文件的字符问题，不是网络** | SSH / 代理 / 配置文件类问题 |
| 4 | **"加了 IP 却没生效" → 说明压根没走到 DNS 查询** | hosts / DNS 排查 |
| 5 | **动系统级网络配置前，先盘点机器上已有的网络工具** | 一切网络配置操作 |
| 6 | 域名逐字符核对（`.` `/` `-` `_` 难以分辨） | 配置文件类问题 |
| 7 | **错误的修复不会消失，会以新问题的形式回来** | 决定"要不要绕过"时 |

---

## 5. 诊断命令工具箱

| 目的 | 命令 | 关键点 |
|---|---|---|
| **系统实际解析到哪**（会读 hosts） | `ping -n 1 域名` | 显示的是**生效后**的 IP |
| **真实 DNS 答案**（**不读 hosts**） | `nslookup 域名` | **这两条的差异是本次破案关键** |
| 本机端口被谁占用 | `netstat -ano \| findstr :443` | 记下 PID |
| PID 对应哪个进程 | `tasklist \| findstr /i 进程名` | |
| 命令行测 HTTPS（绕开浏览器） | `curl -I https://域名` | 失败时能区分网络层与浏览器层 |
| 查看 hosts 全文 | `cat /c/Windows/System32/drivers/etc/hosts` | |
| 查看配置文件的隐藏字符 | `cat -A 文件` | `M-` / `^M` / `^I` |
| 盘点网络类软件 | `tasklist \| findstr /i "watt steam atrust sangfor clash v2ray"` | |

> **最有用的一条对比**：
> `ping 域名` **读** hosts 文件，`nslookup 域名` **不读** hosts 文件。
> 两个结果不一样，就说明 hosts 在起作用——差异本身就能定位问题。

---

## 6. 防复发

### 6.1 遇到"某技术网站打不开 / SSL 错误"时

**第一件事：看 Steam++ 在不在运行。**

它的机制是"把域名写成 `127.0.0.1`，由自己的本地代理接管"。所以：

| Steam++ 状态 | 结果 |
|---|---|
| **在运行** | 本地 443 代理接管 → 走加速线路 → 正常 |
| **没在运行** | 域名仍指向 `127.0.0.1`，但没人接管 → **各种迷惑的 SSL / 连接错误** |

### 6.2 依赖 Steam++ 才能访问的域名（部分）

它写进 hosts 的名单里包含这些**与学习直接相关**的：

```
127.0.0.1 huggingface.co          ← 下载 CLIP / 医学多模态模型要用
127.0.0.1 raw.githubusercontent.com
127.0.0.1 api.github.com
127.0.0.1 google.com
```

**只要 Steam++ 没在运行，这些站点全部不可用**，而且报错看起来像是"网站坏了"，不像"被墙"。

### 6.3 不要做的事

- ❌ **不要手工删 `# Steam++ Start ... End` 那一段** —— Steam++ 下次启动会重写，而且可能写得不一样，比现在更难查
- ❌ **不要手工往 hosts 里加 GitHub 相关条目** —— 会和 Steam++ 的规则冲突，产生"谁赢"的不确定性
- ❌ **不要动 aTrust 相关条目** —— 那是校园网客户端自动加的，删了可能影响校园网接入

### 6.4 要停用 Steam++ 的 hosts 改写时

用它自己的功能（设置里的「**还原 Hosts / 清除 Hosts**」），而非手工编辑。

---

## 7. 本次涉及的路径速查

| 位置 | 是什么 |
|---|---|
| `~/.ssh/config` | SSH 配置：`github.com` → `ssh.github.com:443` |
| `~/.ssh/id_ed25519(.pub)` | SSH 密钥对 |
| `C:\Windows\System32\drivers\etc\hosts` | 需**管理员权限**编辑 |
| `归档/ssh-config-github` | 当时为避免粘贴损坏而准备的文件（内容已并入手册 2.4 / 8.20） |
