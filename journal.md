# journal（每天三行）

## 11-04

写了：`main()` 里加了三样——`len(sys.argv) < 2` 判用法、`int(sys.argv[2])` 取 N（默认 10）、`try/except FileNotFoundError` 打"文件不存在"；`count_words(words, n)` 把上限传进去；晚上做了两数之和（字典存已见值）和有效的字母异位词（手写计数抵消），本地判题 12/12。

卡在：断言写成 `len(cw) == n`，`n=30` 但 `sample.txt` 只有 24 个不同词，程序被我自己的断言崩掉——把"最多 n 条"当成了"一定 n 条"，改成 `<=` 才对；另外在 `D:\python\project` 下直接跑脚本，`sample.txt` 找不到，得先 `cd` 进 `bootcamp`（PyCharm 里对应的是 Working directory）。

明天：Day 3，用 `logging` 换掉 print，同时写 `wordcount.log` 和控制台，读文件成功打 INFO、失败打 ERROR；顺手把 N 传非数字的 `ValueError` 包一层，别让它崩。

## 11-05

写了：把 day03 的 print 换成 logging——`basicConfig` 里配了 `level=INFO`、带时间戳的 format、`FileHandler('wordcount.log')` + `StreamHandler()`；读文件成功记 INFO，`FileNotFoundError` 记 ERROR 后 return。验证过：`nope.txt` 出 ERROR 且不崩，`sample.txt 5` 先出 INFO 再出 5 行结果。同时做了 217/125 两题 + 定了 5 条差异

卡在：① logging 的整体结构第一次见——logger / handler / formatter / level 各管什么、谁先谁后，能跑起来但说不清；② 不看速查表就排不出 `basicConfig` 里那几行，`format` 里 `%(message)s` 中间多敲一个空格就报错；③ 不知道该把哪些 print 换成 logging、哪些该留，这个纠结得最久（最后定：过程与异常走 logging，结果输出留 print）。

明天：Day 4，`git init` + 3 次提交 + 补 README；提交信息写成"每天加了什么"，day01/02/03 三个文件正好对应三段历史。（**晚：Day 4 已提前到今晚做完，明天改走 Day 5**）

## 11-05 晚｜补记：Day 4 提前完成

写了：`git init` + `.gitignore`（`__pycache__/`、`wordcount.log`、`.idea/`）+ 5 次提交（day1 / day2 / day3 / chore / refactor）；`read_text` 改成 `Path(path).read_text(encoding='utf-8')`，删掉手写 with；README 从"使用说明"重写成真正的项目说明（怎么跑 / 输出示例 / 演进历史 / 已知限制）。

卡在：① `.gitignore` 第一次文件名拼错，规则没生效，`git status` 里还是一堆缓存文件，改名后单独提交一次才干净；② refactor 改完差点直接 commit，先跑了一遍才确认输出没变——以后每次 commit 前跑一次，这条要变成肌肉记忆；③ 空文件跑 `day03_wordcount.py` 会 `IndexError`（`cw[0]` 撞上空列表），今天才亲眼看到"断言挡不住空输入"。

明天：Day 5，`test_wordcount.py` 三个用例（小写化、去标点、取前 N），`pytest -v` 全绿，再故意改坏一个断言看它变红；下午装 MySQL 8、建库建表，把 W2 提前两天起。

## 11-06

写了：`test_wordcount.py` 四个用例（小写化、去标点、取前 N、空输入），先红后绿跑通 `4 passed`；故意把断言改坏两次，确认 `pytest` 的红是长什么样、报错里 `assert 实际 == 期望` 怎么读；下午在 MySQL 建 `bootcamp` 库和 `words` 表，用 `insert / update / delete / select ... where ... order by` 把增删改查各跑了两轮。

卡在：① SQL 语句基本忘光——创库、创表、CRUD 每一条都要查手册才写得出来，`creat`、`dateime`、列定义写重、漏分号、`select * where` 少 `from`，一天里五处语法错；② 为了让 `test_count_top_n` 变绿，把 `count_words` 的默认值从 10 改成了 1——测试绿了，但函数和它自己的 docstring「前 10 个」矛盾了，等于用改契约的方式让测试闭嘴（后来默认值改回 10、测试显式传 n，空输入也补了 `if not cw: return`，见 cde0207）；③ 环境踩坑：激活的是别的项目的 `.venv1`，`pytest` 一开始「没装」，其实是装错环境；`python -m venv .vemv` 还打错一个字，留下一个死环境。

明天：Day 6，`words.py` 只做 `add` / `list`，JSON 存 `{"apple": "苹果"}`，文件不存在从 `{}` 起；重复 `add` 的行为（覆盖还是报错）自己定，但要写进 README。


