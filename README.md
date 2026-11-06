# 词频统计小工具

> Python 7 天练习项目 · Day 1–4 已完成 · 只用标准库

读一个文本文件，切出英文单词、统一小写、统计词频，打印出现次数最多的前 N 个。

这个项目不是为了"有用"，是为了把一个小程序从**能跑**推到**像个项目**：先跑通，再加命令行参数，再让报错说人话，再把日志落盘，最后用 git 把每一次改动留下来。

## 怎么跑

```bash
cd D:\python\project\bootcamp

python day03_wordcount.py sample.txt 10    # 前 10 个高频词
python day03_wordcount.py sample.txt 20    # 前 20 个
python day03_wordcount.py                  # 缺参数：打印用法后退出
python day03_wordcount.py nope.txt         # 文件不存在：提示后退出，不抛堆栈
python day03_wordcount.py sample.txt abc   # N 不是数字：提示"N必须是数字"
```

参数：`<文件> [N]`，N 缺省 10。

- 过程与异常写入 `wordcount.log`（UTF-8、带时间戳与级别）；
- 词频结果走 stdout（`print`），因为那是给人看的结果，不是排查轨迹。

## 输出示例

`python day03_wordcount.py sample.txt 10`：

```
1. is         4
2. a          4
3. code       4
4. skill      3
5. python     2
6. practice   2
7. language   1
8. easy       1
9. to         1
10. read      1
```

`log` 文件里对应的是：

```
2026-11-05 20:09:26,501 [INFO] __main__ - 读取文件成功
```

## 代码怎么长成这样（git 历史）

| 提交 | 改了什么 | 为什么 |
|---|---|---|
| `day1` | 四个函数：read / split / count / print | 先跑通，别的都往后放 |
| `day2` | 命令行传文件与 N；`FileNotFoundError` 兜底 | 换文件不用改代码；报错要说人话 |
| `day3` | `logging` 双通道（文件 + 控制台），双通道各管一边 | 事后能查"哪次运行、读了哪个文件" |
| `chore` | 修 `.gitignore` 拼写，忽略 `wordcount.log` / `__pycache__` | 日志和缓存不该进仓库 |
| `refactor` | `read_text` 改用 `pathlib` | 三行变两行，语义更直白 |

`git log --oneline` 就能复现这条演进线——面试问"你怎么做版本管理"，指着它讲。

## 已知限制

- **只认英文**：正则 `[A-Za-z]+`，中文整段被丢弃（Day 2 原计划就写了"中文暂时不管"）。
- **没去停用词**：`is` / `a` 会占前排，看结果时心里要有数。
- **空输入会崩**：文件里没有英文单词时 `cw` 是空列表，`cw[0]` 抛 `IndexError`，`assert` 那段挡不住空列表——Day 5 写测试时正好补一个用例。
- **没有测试**：Day 5 补 `test_wordcount.py`。

## 环境

Python 3.10+，无第三方依赖。

## 进度

- [x] Day 1：打印词频前 10
- [x] Day 2：命令行参数 + 文件不存在不崩
- [x] Day 3：`wordcount.log` 里有 INFO 与 ERROR
- [x] Day 4：`git log` 三次以上提交
- [ ] Day 5：`pytest` 跑过 3 个用例
- [ ] Day 6–7：命令行单词本 `add` / `list` / `search` / `delete`

## 三条规矩（给自己）

1. 不许让 AI 生成整个文件——只让它解释报错、review 我写的 20 行。
2. 每段 AI 给的代码，删一行再跑一次，看它怎么坏。
3. 每天在 `journal.md` 写三行：写了什么 / 卡在哪 / 明天第一件事。
