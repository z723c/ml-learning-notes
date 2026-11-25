# python/

Python 学习区。**笔记和代码分开放，用编号对齐。**

| 目录 | 放什么 | 命名方式 |
|---|---|---|
| `notes/` | **笔记**（`.md`）：概念、认知修正、踩过的坑 | `<编号>_<主题>.md` |
| `code/` | **练习代码**（`.py`）：能直接跑的东西 | `<编号>_<主题>.py` |

## 编号对照

| 编号 | 主题 | 笔记 | 代码 |
|---|---|---|---|
| **01** | 变量与对象、字面量与数据类型 | [`notes/01_variables.md`](notes/01_variables.md) | [`code/01_variables.py`](code/01_variables.py) |
| **02** | 字符串、运算符 | [`notes/02_strings-operators.md`](notes/02_strings-operators.md) | [`code/02_strings.py`](code/02_strings.py) |
| **03** | `if` / `match` / `while` / `for` | [`notes/03_if-while-for.md`](notes/03_if-while-for.md) | [`code/03_if-while-for.py`](code/03_if-while-for.py) |

> 同一个编号的 `.md` 和 `.py` 是同一件事的两面：**`.md` 记你懂了什么，`.py` 是你写出来的东西。**

## 五条约定

1. **一个主题一份笔记**，新内容编号往后排（04、05…），不要复用旧编号
2. **笔记里不放可运行脚本** —— 代码一律进 `code/`
3. **两个文件夹按编号一一对应**，找不到对应代码就说明这个主题还没动手
4. 笔记格式参考 [`../templates/notes.md`](../templates/notes.md)
5. **文件名只用英文字母、数字、下划线、连字符** —— 中文标点（`、` `，`）会让 Markdown 链接和命令行出问题

> 检验与错题记录在 [`../docs/review-log.md`](../docs/review-log.md)，不放在这里。
