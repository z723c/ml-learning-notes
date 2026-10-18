# Python 变量与对象：变量是名字，不是盒子

> 对应课程：黑马程序员《Python+AI 零基础入门到大神》「字面量与变量 / 标识符 / 数据类型」
> 状态：🟢 已学完，检验过 1 次
> **检验过程与错题不在这里**，见 [`docs/review-log.md`](../../docs/review-log.md)。

## 一句话总结

Python 的变量不是"装东西的盒子"，而是"贴在对象上的名字"。赋值是让名字指向对象，不是复制对象——这一条解释了后面所有"改了 a 结果 b 也变了"。

## 核心概念

| 概念 | 我的理解 | 最小例子 |
|---|---|---|
| 字面量 | 程序里写死的值，本身**没有名字** | `18`、`"abc"`、`True`、`None` |
| 对象 | 真正存数据的东西，有类型和 id | `id([1, 2])` |
| 变量 | 贴在对象上的**名字**，不是容器 | `num = 1` 是 `num` 指向 `1` |
| 可变 / 不可变 | 能否原地改内容。list / dict / set 可变；int / float / str / tuple / bool / None 不可变 | 见「认知修正 3」 |
| 赋值 | 让名字指向另一个对象，**不复制** | `b = a` |
| 标识符 | 硬性：字母 / 数字 / 下划线、不能数字开头、不能是**关键字**。规范：见名知意、小写、下划线连接 | `name_1` ✅　`1name` ❌　`True` ❌ |
| 查 / 判类型 | `type()` 查看，`isinstance()` 判断 | `type(1)` → `<class 'int'>` |
| bool 与 int | **`bool` 是 `int` 的子类**，`True` 就当作 1 | `issubclass(bool, int)` → `True` |

## 认知修正 ★

1. **我原来以为**变量是"装值的容器"
   **实际上是**：容器只在**不可变对象**上碰巧成立，一碰可变对象或赋值 / 传参就崩。
   **裁决工具**：比 `id(a) == id(b)` —— 相同就是同一个对象有多个名字。

2. **我原来以为** `b = a` 是把 a 的内容复制一份给 b
   **实际上是**：只是让 `b` 指向同一个对象。要真复制用 `a.copy()`（浅）或 `copy.deepcopy(a)`（深）。
   **为什么容易搞错**：C 那类语言的变量语义更接近"盒子"，直觉会带过来；而不可变对象看起来"复制"了，因为 `y += 1` 其实是新建对象再改指向。

3. **我原来以为** `b += [3]` 就是 `b = b + [3]`
   **实际上是**：`+=` 对可变对象调 `__iadd__`，**原地改**（`a` 跟着变、`a is b` 仍 `True`）；`b = b + [3]` **新建列表**（`a` 不变、`a is b` 变 `False`）。
   **int 上两者等价，list 上不等价。**

4. **我原来以为**类型不同就会报错
   **实际上是**：只有"要求两边同类型"的运算符才报错（`str + int`）。`"3" * 3` 合法（重复 → `333`）、`1 + 1.0` 合法（提升为 float）、`==` 按数值比（`1 == 1.0` → `True`，`"1" == 1` → **`False` 而不报错**）。

5. **我原来以为** `isinstance` 只能一个个类型判断
   **实际上是**：第二个参数可以是**元组** —— `isinstance(v, (int, float))`，任意一个匹配即 `True`。

6. **我原来以为** `type()` 和 `isinstance()` 差不多
   **实际上是**：`type()` 返回**最具体**的类；`isinstance()` 沿**继承链**检查。
   所以 `type(True) == int` → `False`，但 `isinstance(True, int)` → `True`。
   **后果**：判断"是不是数字"时 `isinstance(v, int)` 会把 `True` 算进去。
   **PyTorch 里**：每个模型都是 `nn.Module` 的子类，所以只用 `isinstance`，`type(x) == nn.Module` 永远是 `False`。

7. **我原来以为** `True` 不能当标识符是因为它是"特殊字符"
   **实际上是**：它是**关键字**（`keyword.iskeyword("True")` → `True`）。特殊字符指 `&` `@` 这类符号。

## 关键代码

### 引用 / 浅拷贝 / 深拷贝

```python
import copy

a = [[1, 2], [3, 4]]

b = a                  # 同一个对象
c = a.copy()           # 浅拷贝：外层新对象，内层还是共享
d = copy.deepcopy(a)   # 深拷贝：完全独立

a[0].append(99)
print(b)   # [[1, 2, 99], [3, 4]]
print(c)   # [[1, 2, 99], [3, 4]]  ← 浅拷贝挡不住嵌套层
print(d)   # [[1, 2], [3, 4]]     ← 深拷贝才独立
```

### `+=` vs `+`

```python
a = [1, 2]; b = a
b += [3]          # 原地改
print(a, a is b)  # [1, 2, 3] True

a = [1, 2]; b = a
b = b + [3]       # 新建列表
print(a, a is b)  # [1, 2] False
```

### 判断"是不是数字"（要排除 bool）

```python
def is_number(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)

print(is_number(3), is_number(3.0), is_number(True), is_number("3"))
# True True False False
```

## 容易踩的坑

- **函数默认参数用可变对象**：`def f(x, acc=[])` —— 默认值只在定义时创建一次，会跨调用累积。改成 `def f(x, acc=None): acc = [] if acc is None else acc`
- **用 `is` 比较值**：`is` 比"是不是同一个对象"，比值要用 `==`
- **`str + int` 报错，但 `str * int` 不报错**（后者是重复）
- **`bool` 混进数字判断**：`isinstance(True, int)` 是 `True`
- **`print(type(x))` 输出 `<class 'int'>`**，不是 `int`（报错信息里也是这个格式）

## 还没搞懂的问题

- [x] 小整数缓存的范围是多少？—— **-5 到 256**，CPython 启动时预创建。超过 256 的相同字面量在**同一代码块**里可能因常量去重而共享，**不要依赖 `is`**
- [ ] 深拷贝遇到循环引用会怎样？

## 参考

- 课程：黑马程序员《Python+AI 零基础入门到大神》「字面量与变量 / 标识符 / 数据类型」
- 文档：Python 官方教程 "Data model" 一节
