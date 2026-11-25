# Python 控制语句语法速查（if / match / while / for）

> 用途：写代码时查**语法结构**。只列骨架，不讲行为细节 —— 行为靠练习和检验。
> 对应课程：黑马程序员《Python+AI 零基础入门到大神》「if / match / while / for」
> 检验与错题见 [`docs/review-log.md`](../../docs/review-log.md)。

---

## 0. 先记住三条通用规则

Python 的复合语句和 C / Java 差别很大：

| 规则 | 说明 | 反例 |
|---|---|---|
| **行末必须有冒号 `:`** | 少了就是 `SyntaxError` | ~~`if x > 0`~~ |
| **代码块靠缩进划分** | 不用花括号；同一块缩进必须一致（习惯 4 空格） | ~~`if x: print(1)`~~ 单行虽合法但不推荐 |
| **条件不用括号** | `if x > 0:` 而不是 `if (x > 0):` | 加了括号能跑，但没必要 |

---

## 1. `if`

### 单分支

```python
if 条件:
    语句
```

### 两分支

```python
if 条件:
    语句
else:
    语句
```

### 多分支

```python
if 条件1:
    语句
elif 条件2:
    语句
elif 条件3:
    语句
else:
    语句
```

> `elif` 是 Python 自己的关键字，**不是** `else if`。

### 嵌套

```python
if 条件1:
    if 条件2:
        语句
    else:
        语句
else:
    语句
```

### 三元表达式（一行 if-else）

```python
变量 = 值1 if 条件 else 值2
```

---

## 2. `match`（⚠️ 需要 Python 3.10+）

> **你的主力环境 `medclip` 是 Python 3.9，跑 `match` 会报错。**
> 练 `match` 用：`C:\Python314\python.exe` 或 conda `base`（3.13）。

### 基本形态

```python
match 值:
    case 模式1:
        语句
    case 模式2:
        语句
    case _:
        语句
```

### 常用模式

```python
match x:
    case 1:                  # 字面量
        语句
    case 1 | 2:              # 或模式：1 或 2
        语句
    case "abc":              # 也可以是字符串
        语句
    case 变量名:              # 捕获：把值绑到变量上（相当于兜底）
        语句
    case _:                  # 通配：兜底，不绑定
        语句
    case n if n > 0:         # 守卫：模式 + 额外条件
        语句
```

### 容器模式（进阶）

```python
match 序列:
    case [a, b]:             # 长度 2 的序列
        语句
    case {"k": v}:           # 含键 "k" 的字典
        语句
```

---

## 3. `while`

### 基本形态

```python
while 条件:
    语句
```

### 带 `else`

```python
while 条件:
    语句
else:
    语句
```

### 死循环 + `break` 退出（最常见）

```python
while True:
    if 退出条件:
        break
    语句
```

---

## 4. `for`

### 基本形态

```python
for 变量 in 可迭代对象:
    语句
```

### 常见搭配

```python
for i in range(5):                    # 0..4
    语句

for 元素 in 列表:
    语句

for 索引, 元素 in enumerate(列表):      # 同时要索引和值
    语句

for 键, 值 in 字典.items():            # 同时要键和值
    语句
```

### 带 `else`

```python
for 变量 in 可迭代对象:
    语句
else:
    语句
```

---

## 5. `break` / `continue`

```python
while 条件:
    if 某条件:
        break        # 立刻结束【整个】循环
    if 另一条件:
        continue     # 跳过本次剩下的语句，直接进下一次
    语句
```

> `break` 只跳出**它所在的那一层**循环。

---

## 6. `range()` 的四种写法

```python
range(5)            # 0 1 2 3 4
range(2, 5)         # 2 3 4
range(0, 10, 2)     # 0 2 4 6 8
range(5, 0, -1)     # 5 4 3 2 1
```

结构：`range(起点, 终点, 步长)` —— **含起点，不含终点**。

---

## 7. 什么算「假」

`if` / `while` 的条件不要求是 `bool`，任何值都能判真假：

| 值为「假」的 | 值为「真」的 |
|---|---|
| `False` | `True` |
| `None` | 任何对象 |
| `0`、`0.0` | 非零数（含负数） |
| `""`（空字符串） | 非空字符串（含 `" "` 一个空格） |
| `[]`、`()`、`{}`、`set()`（空容器） | 非空容器 |

> 记法：**「空」和「零」为假，其余为真**。`0` 和 `False` 是一回事。

---

## 8. 一份能一次跑通的骨架

```python
# if
score = 85
if score >= 90:
    level = "A"
elif score >= 60:
    level = "B"
else:
    level = "C"
print(level)

# for + range + break
for i in range(1, 10):
    if i == 4:
        break
    print(i, end=" ")
print()

# while
n = 3
while n > 0:
    print(n, end=" ")
    n -= 1
print()
```
