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

## 11-07

写了：`words.py` 补齐行为约定——`strip().lower()` 归一、重复 add 打"已更新"、`save()` 挪出分支无条件执行、用法提示从成功路径挪回防呆分支；`test_words.py` 加 `test_add_twice_then_load`（`Apple` / `apple` 只留一个 key）；`db_check.py` 用 pymysql 连 `bootcamp` 库查 `words` 表、与 `day03` 输出对账；闭卷复现 `t11.py`（骨架 60%）；LeetCode 283 移动零 / 209 长度最小的子数组 / 3 无重复最长子串。

卡在：① 归一化时把 `save()` 关进了 `else`，`test_add_then_load` 当场变红——第一次真的被回归测试拦住，也第一次体会到"判断要在修改之前、落盘必须无条件"；② 闭卷时 API 全线失守：`json(f)`、`open` 漏 `encoding`、`return json.dump(...)`、`split()` 当 `strip()`、`data` 没 `.items()`、`cmd_add` 少传 `path`、缺 `sys.exit()`；③ 移动零把"遇到非零才交换"写成"遇到零才交换"，根因是没定义 `slow` 的不变量；④ `test_db.py` 起名撞了 pytest 收集规则（所有 `test_*.py` 都会被 import 执行），一导入就 `ModuleNotFoundError: pymysql`，直接把整个套件带崩，改名 `db_check.py` 后 `7 passed`；⑤ `pymysql` 只装在当时的那个环境，bootcamp 的 `.venv` 和 anaconda 里都没有——换解释器就跑不起来，这是环境问题不是代码问题。

明天：Day 7，`search` / `delete` 两个子命令 + 2 个用例；下午 W2 收尾（JOIN / 聚合 + 用 pymysql 把 `words.json` 写进 MySQL）；傍晚合并两份执行版、根目录文件归位；顺手补 `requirements.txt` 把依赖钉住。

## 11-08

写了：`cmd_search`（前缀匹配 + 无结果提示）和 `cmd_delete`（不存在时提示、`save()` 无条件执行），新增 2 个用例，`pytest` 到 **9 passed**；建 `dictionary` 表（`word` 做主键）跑通 JSON→MySQL 迁移（`sync_to_mysql.py`，upsert + `commit()` 放在循环外）；用 `LEFT JOIN` 把"词频"和"词典"连起来对账；LeetCode 206 反转链表 + 704 二分查找。

卡在：① SQL 一天 14 处报错，其中 8 处是 11-07 原样复发（表名、`VARCHAR` 长度、时间戳默认值、多行插入括号、`SELECT`/`WHERE` 职责、`DELETE` 条件、`ORDER BY` + `LIMIT`）——查手册查出来的语法，隔一天就还回去了；② 工程习惯：`executemany` 拿去跑建表、建表语句放进 `for` 循环、`commit()` 忘了放循环外；③ `LEFT JOIN` 查不出数据，实际是左表 `words` 被之前的 `DELETE` 清空了；④ 测试里 `from bootcamp.words import`、给测试函数乱加 `app` 参数、`cmd_search` 传 4 个参数、`data.items()` 当成员判断用、`data()` 当函数调用；⑤ 缩进把"收集结果"和"判断 + 打印"一起写进了 `for` 循环，导致每遍历一个词就打印一次；⑥ 链表反转里调用自身忘了 `self.`。

明天：11/09 周日，闭卷默写七条 SQL（对照清单看能过几条）、答昨天欠的卡、W1 回环重跑 `day01`–`day03` 与 `words.py` 四个命令；傍晚把驾照"哪家 / 多少钱 / 多久"查出来给结论（11/10 是截止线）。

## 11-09

写了：盲敲复习——闭卷默写七条 SQL 并在 MySQL 里逐条执行（`DELETE`、`SELECT` 各错一处），答掉卡 9 和卡 10；项目 A 的 A1 起跑：`A1_project/a1_get.py` 里用 `requests.get` + `timeout` + 状态码断言，跑通 GitHub star 数（54732），顺手走过 404 和连接超时两条错误路径；LeetCode 128 最长连续序列 + 49 字母异位词分组。

卡在：① `DELETE words WHERE ...` 漏了 `FROM`，报 1064，报错位置指向 `near 'WHERE word = 'banana''`；② `SELECT (word, freq) FROM words` 多加了括号，报 1241 `Operand should contain 1 column(s)`；③ 二分查找把 `mid` 写成 `right - left + 1`——那是区间长度，不是中点；④ 盲敲 pytest 还是不熟：命令会敲，但说不清 `-v` / `-q` / `-x` 各管什么，红的时候先看哪一行也含糊；⑤ 文件名手打错一次（`ai_get.py`）、目录多进一层（`A1_project`）一次。

明天：Day 9（11/10），先把两条 SQL 笔误改掉、七条重默到 7/7；pytest 盲敲练熟（三个参数 + 手写一个会变红的用例）；A2 把 `get(url)` 和 `check(resp, code)` 封成两个函数、调用两次（200 与 404）；驾校确认报哪家（11/14 前定）。

## 11-10

写了：`sql\practice.sql` 重建到 `test_bootcamp` 库（`varchar(50)`、`utf8mb4`、`drop table if exists`），七条从头重跑；A2 修成窄捕获（`except requests.RequestException`）、`check` 改用 `RuntimeError` 并带上"期望 / 实际"、404 那条改成 `check(r2, 404)`；pytest 亲手验证 `-x` 与 `--tb=short`；HTTP 三组笔记（401 vs 403、GET 幂等、PUT vs PATCH、Token 无状态）；盲敲 128 与 49；LeetCode 20 有效括号、21 合并两个有序链表、160 相交链表、141 环形链表。晚上把第二天的活提前做了：A3 三个用例（`test_a3.py`：`check` 通过 / `check` 抛错 / 真请求集成）、A4 数据外置（`data/cases.yaml` + `parametrize` 跑 2 条）、SQL 分组 `GROUP BY` / `HAVING` 与事务三段（`START TRANSACTION` → `ROLLBACK` → `COMMIT`）。收尾又修了三处并把套件跑绿：`test_a4` 改用 `Path(__file__).parent / "data" / "cases.yaml"`、`get()` 去掉 `sys.exit` 改成让异常上抛、`FakeResp` 传实例且集成用例补上 `check(get(url), 200)`——在 `bootcamp` 根目录 `python -m pytest -q` 得到 **14 passed**（词频 4 + 单词本 5 + A3 三 + A4 两）。

卡在：① PowerShell 不支持 `<` 输入重定向（`ParserError: RedirectionNotSupported`），得用 `Get-Content | mysql` 或 `source`；② 脚本里 `UPDATE ... freq=2` 之后再 `DELETE ... freq=60` 删不到——语句之间共享状态；③ 建表时把 `unique(word)` 写进了表选项，唯一约束要写在括号内；④ `except Exception` 太宽：`data['stargazers_count:']` 多打一个冒号触发 `KeyError`，被外层兜住直接 `exit(1)`，404 那步根本没跑；⑤ `raise ('...')` 不能抛字符串、`except Exception:` 没 `as e` 却用了 `{e}`；⑥ 128 内层循环没有递增变量、`curr_len` 初始化成 0；⑦ 49 对整个列表 `sorted(strs)`、新建 key 时忘了 `append` 当前元素、`dic.value()` / `dic()` / `list[dic.values()]`；⑧ A3/A4 的坑：测试文件与函数都以 `test_` 开头 pytest 才扫得到、`@pytest.mark.skipif` 拼写与"必须带条件"、`pytest.raises` 块里不能混进"不报错"的语句、`FakeResp` 传了类而不是实例、`yaml.safe_load` 要传文件对象、YAML 用 `key: value` 与 `-` 列表、`parametrize` 的参数名要和函数形参对齐；⑨ **业务函数里 `sys.exit(1)` 会杀死整个 pytest**——`get()` 断网后退出进程，外层 `except` 根本接不住；⑩ `data/cases.yaml` 用相对路径，在 bootcamp 根目录跑 pytest 就 `FileNotFoundError`（收集阶段直接中断）。

明天：11/11，只修三处收尾——`test_a4.py` 改用 `Path(__file__).parent / "data" / "cases.yaml"`、`get()` 把 `sys.exit` 换成让异常上抛、`FakeResp` 传实例并给集成用例补 `check(get(url), 200)`；跑通后提交，再打驾校电话（11:00 前）。

## 11-11

写了：三处收尾全部改完（`Path(__file__)` 定位 yaml、`get()` 去掉 `sys.exit` 让 `RequestException` 上抛、`FakeResp` 传实例 + 集成用例补 `check(get(url), 200)`），`python -m pytest -q` 回到 **14 passed** 并提交（`28e15b2`）；上午做了一次 A1–A4 的口述复述，自己记下 9 个卡点；11:00 后外出，没有写代码。

卡在：① A1 复述时漏了"断言才是通了的证明"，还把 A1 和 A4 的场景搞混（A1 的 URL 是写死的，读文件是 A4）；② A2 把拆分原因说成"不然断言不生效"，真实原因是**可测试性**——`check` 只吃 response，才能用 `FakeResp` 脱离网络；还把 `check` 说成"捕获 RuntimeError"，其实它是**主动 raise**；③ A3 忘了假对象伪造的是 response 不是 URL、忘了集成用例是 `check(get(url), 200)`、忘了断网用 `pytest.skip()`；④ A4 想不起 `@pytest.mark.parametrize` 的名字，讲不出"加用例不改代码"是因为 pytest 逐项遍历注入形参，`case[url]` 少了引号；⑤ 背了 4 天没答出的卡 11（顺序 bug）、卡 12（json API），说明它们还没在代码里被用过。

明天：Day 11（11/12），A5 分层改造——建 `api/` / `common/` / `testcases/`，把 `get` / `check` 挪进对应模块，接 logging 与 `pytest-html`，一条命令出报告；改完用例数仍是 14。

## 11-12

写了：A5 分层重构落地——`api/client.py`（只发请求、异常上抛）、`common/assert_util.py`、`common/logger.py`（双通道写日志）、`testcases/test_github.py`、`conftest.py` 用 `pytest_generate_tests` 钩子读 `data/cases.yaml`；`pytest --html=reports/report.html --self-contained-html` 生成报告（41KB），重构前后都是 **14 passed**；LeetCode 5 最长回文子串 + 56 合并区间；复习 160 / 141 / 21 / 20 四题；卡 11、卡 12 用"举自己的例子"的方式答出来（D+1 与逾期 D+3 一并勾掉）。

卡在：① 搬 `client.py` 时照抄旧 `try/except`，只 print 不 raise，断网返回 `None`，上层直接 `AttributeError`；② 旧 `test_a3.py` / `test_a4.py` 没删，pytest 扫到两份重复用例；③ 搬到 `testcases/` 后 `Path(__file__).parent / 'data'` 失效（少跳一级，或该交给根 `conftest.py`）；④ 想把 fixture 塞进 `parametrize`、想在测试里 `for` 循环遍历；⑤ 把钩子 `pytest_generate_tests` 写成装饰器、手动 `from conftest import`、`conftest.py` 敲成 `contest.py`；⑥ `logger.py` 里试图 `def logging.basicConfig()` 重定义官方函数、`FileHandler` 少个 H、字符串引号没闭合；⑦ 报告参数不识别（解释器没对齐 / `reports/` 目录不存在）；⑧ 链表复习：160 忘了"走到 `None` 才跳另一条链"、141 `while` 写成 `fast != slow` 且漏判 `fast.next`、21 `dummy` 没实例化 / 用 `.next` 比值 / 返回 `[dummy]`、20 右括号匹配的边界（栈空、栈非空）不清。

明天：11/13，A6 —— 建远程仓库并 push，加 `.github/workflows/test.yml` 让 push 自动跑 pytest，补 README 的"A1 项目"一节（怎么跑 / 怎么测 / 目录说明），把日志路径固定到 `reports/`，把 `test_github_cases` 的断网处理统一成 `skip`。

## 11-13

写了：A6 全流程走完——安全外置（`sync_to_mysql.py` 的密码改成 `os.getenv('MYSQL_PWD')`）、`requirements.txt` 补齐（pytest-html / requests / pyyaml）、在 GitHub 建公开仓库 `olso78/python-api-test-framework` 并 push（`git branch -M main` + `remote add` + `push -u`）、`pytest.ini` 注册 `integration` 标记、`.github/workflows/test.yml` 让每次 push 自动跑 `-m "not integration"`、README 置顶加 CI 徽章与"怎么跑 / 怎么测 / 目录"三块；本地 `pytest -q -m "not integration"` = **11 passed, 3 deselected**，全量仍是 14。LeetCode 121 买卖股票 + 136 只出现一次的数字，复习 5 / 56 / 20 三题。

卡在：① 日志用相对路径，`run.log` 散落在不同目录，最后用 `Path(__file__)` 锚定；② `pytest.ini` 建到了上级 `project` 目录——pytest 能往上找，但不合工程规范；③ `test_github_cases` 断网时 `fail`，而 `test_github_api` 是 `skip`，同一项目两种行为；④ **`@pytest.mark.intergration` 拼错**：只给一句 `Unknown mark` 警告、程序照跑，于是 `-m "not integration"` 过滤不到它，CI 真的去连 GitHub API，触发 403 频控把套件打红——拼写错导致的静默失效；⑤ 密码明文硬编码，公开仓库前必须外置；⑥ 5 最长回文：辅助函数漏 `while`、漏返回切片 `s[l+1:r]`、把函数当方法调 `s1.expand_around_center(...)`、循环条件写成 `while left >= 0 or right <= len(s)-1`、最优比较放在循环外只保留最后一个中心；⑦ 56 合并区间：`sort()` 记成要赋值、`key` 位置写错、用 `range(len())` 拿索引、漏 `if not res`、重叠时直接覆盖右边界没用 `max`、`=<` 这种非法运算符；⑧ 20 有效括号：右括号分支忘了先判栈空、忘了 `pop()` 比对、忘了最后 `return not stack`。

明天：11/14，提前进 W3 —— 简历 v0.5（用 `03_简历/简历诊断与岗位对照.xlsx` 的改稿骨架 + 我整理的"事实清单"填一页纸），并准备两段项目的 STAR 讲法。

## 11-14

写了：简历一天推了四版——v0.5（首版排版）→ v0.6 → v1.0 → **v1.1 定型**：单页、单栏、无照片，大创压成一行进「实习与其他经历」，删掉纪念馆那行把页面拉回一页；导出 `简历_v1.1.pdf` 并复制成 `徐高强_软件测试实习_南京.pdf` 供投递；另做了 `排版沙盒.html` 对比版式、`简历面试准备.md`（三问答案 + 两段口述稿）、`简历交接包_20261114.zip`；我把大创项目的架构与 8 个面试问题过了一遍，出 `大创项目_架构与可讲清单.md`（结论：只写一行"参与"，不写独立开发）。

卡在：① 版式反复，Word 导出 PDF 在本机卡死，最后改走浏览器打印 HTML，末行落在 801/842，只剩约 5pt 余量；② 大创 8 问里"能答 4 / 半答 3 / 答不出 1（Cypher 为什么用 Union all）"，所以措辞只能写"参与"；③ 想再加一个"作业批改统计脚本"进简历，页面预算不够——必须先删掉词频项目整段（约 −96pt）才塞得下（+77pt），而且这个项目今天还没建。

明天：11/15，做 `hw-stats`（作业批改统计脚本）——独立仓库、模拟数据、pandas 分组出班级周报/缺交名单/错题 TOP5、3 条 pytest；必须实测"同一件事手工 vs 脚本"的两个耗时，再出简历 v1.3。

## 11-15

写了：`hw-stats` 从零到上线——`generate_data.py` 造 3 班 × 4 周共 120 条模拟数据（姓名用占位、README 声明"非真实学生信息"）；`report.py` 用 `csv` + `argparse` 出班级周报（提交率 / 平均正确率）、缺交名单、错题 TOP5；统计逻辑抽成纯函数 `generate_stats`，文件读写与计算分离；`test_report.py` 3 条用例（正常周 / 全班缺交 / 空数据）**3 passed**；独立仓库 `olso78/hw-stats` 已 push。实测"同一件事"：Excel 手工汇总 17 分 29 秒 → 脚本 0.1 秒。简历出 **v1.3**：删掉词频整段、加入 hw-stats 四条，仍是一页（末行 785/842）。

卡在：① `writerow` 传整句字符串，数据全挤一列（它要的是列表）；② 缺交学生仍随机生成 `correct_questions`，造出"交白卷得 8 分"的荒谬数据；③ `"{i:03d}"` 忘了 `f` 前缀，学号全是字面量；④ `parser.parse_args()` 写在模块级，pytest 一导入就 `SystemExit`；⑤ CSV 读出的 `'3'` 直接和整数 3 比，循环进不去；⑥ `csv.DictReader(f)` 没 `list()`，`len()` 报错且第二遍遍历为空；⑦ 缺交的 `total_questions` 被算进分母，正确率算出 40%；⑧ `print` 写在循环里打了 120 次、`avg_accuracy` 定义在分支里导致空数据 `UnboundLocalError`；⑨ 测试写在测试函数内部扫不到、参数顺序传反、断言用中文冒号对英文键、`return` 里防了零但 `print` 里没防。

明天：11/16，把 v1.3 定稿（导出 `徐高强_软件测试实习_南京.pdf`）并开始首投 3–5 家；投递记录写进 `简历诊断与岗位对照.xlsx` 的「投递对照表」。

## 11-16

写了：简历按"自制表格模板"重排——`简历_v1.4_表格版.docx`，由 `tools/build_resume_table.py` 复制 `简历_模板.docx` 生成（原件不动）：三个项目统一成"技术栈 / 开发工具 / 项目描述 / 成果"四段，大创进项目经历、写成"参与问答链路"，删掉「实习经历」一节、把助教场景并进 hw-stats 的项目描述，新增「自我评价」；按"少用符号、多用文字"把加号、箭头、括号的写法全部改成叙述句；一页（末行 651/842）。顺手把 16 个废案简历归到 `_archive`（约 1.3MB）。`hw-stats` 补了 `--md` 导出、加 `.gitignore` 清掉 `__pycache__`，仓库已同步。

卡在：① 表格模板自带大行距，同一份内容 9.5pt 会溢出到两页、9.2pt 又只剩七成七，必须靠调字号与"删一节/加一行"反复试才落在一页；② 给项目加"开发工具"一行时，差点把没用过的 Postman 直接写上去——被点破：投测试岗却一个测试工具都没用过，这是硬伤，工具必须先真用过再写；③ 模板是六列合并单元格，脚本不能按列号写，得按"合并后的单元格对象"定位，否则会写错格。

明天：11/17，Postman 实操——建 Collection、环境变量、Tests 断言状态码与字段、Runner 跑用例、导出 collection JSON 提交进仓库；用真用过的工具回填简历，再投 3 家测试岗。

## 11-17

写了：Postman 全流程走通——用"Continue without an account"进本地工作区（不绑文件夹，避免污染仓库）；建 `GitHub API` 集合与环境变量 `base_url`；两条请求分别断言 200 与 404（`pm.test` + `to.have.status`、`to.have.property`）；Collection Runner 批量跑出 2 passed / 0 failed；导出 Collection v2.1 存进 `A1_project/postman/` 并提交（`ddcf27b`）。简历「开发工具」加回 Postman（这次是真用过），导出投递版 PDF `徐高强_软件测试实习_南京.pdf`（一页，末行 666/842）。

卡在：① 新版把"跳过登录"藏在页面最底部，只有一行 `Continue without an account`；② 环境变量是表格视图，把 `https://api.github.com` 填进了变量名列，触发 duplicated key 警告；③ Runner 第一次报 `Empty request URL`——改完请求没点 Save，Runner 抓到的还是空 URL；④ 导出时先选了 Environment 而不是 Collection，重导一次才拿到 v2.1 的集合文件。

明天：11/18，计划是 JD 采样（30 条）＋ Playwright 安装。

## 11-18

写了：没有代码产出。仓库无提交、文件无变更，当天只有站内科目一提醒。

卡在：连续几天高强度后停了一天。停一天不是问题，但要有"重新启动"的动作，否则容易停成三天：下次开工先用一条最小命令把循环接回来（跑一遍 `pytest -q`），再开新内容。

明天：11/19，Allure 接入。

## 11-19

写了：Allure 报告接入——`pip install allure-pytest`、`npm install -g allure-commandline`；`pytest --alluredir=reports/allure-raw` 收集原始 JSON，`allure generate ... --clean` 编译静态 HTML，`allure open` 起本地预览；给用例加 `@allure.title` 中文标题，报告里能看到参数化数据、耗时与通过状态；`.gitignore` 补 `reports/`，提交 `fecf52e`。顺手验证了 `pytest -m "not integration"` 的输出：2 passed / 3 deselected。

卡在：① `--alluredir = reports/allure-raw` 等号两边带空格，pytest 不认识这个参数；② 直接 `python test_github.py` 会 `ModuleNotFoundError`——测试必须由 pytest 驱动，它才注入 `sys.path`、加载 conftest；③ `allure open` 是起本地服务、占端口，要 Ctrl+C 才退出。

明天：11/20，Playwright 装环境（`pip install pytest-playwright` + `playwright install chromium`）＋ 第一个 UI 用例（saucedemo 登录）；下午 JD 采样 30 条跑 `jd_scan.py`。


