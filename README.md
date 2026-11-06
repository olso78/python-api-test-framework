# 词频统计小工具

> Python 7 天练习项目 · Day 1–5 已完成 · 运行时不依赖第三方库

读一个文本文件，切出英文单词、统一小写、统计词频，打印出现次数最多的前 N 个，过程写进日志。

这个项目不是为了"有用"，是为了把一个小程序从**能跑**推到**像个项目**：先跑通 → 再加命令行参数 → 再让报错说人话 → 再把日志落盘 → 再用 git 把每一次改动留下来 → 最后用测试把行为钉住。

## 文件都在哪

```
bootcamp/
├─ day01_wordcount.py    第一版：四个函数，结果打印到屏幕
├─ day02_wordcount.py    第二版：sys.argv 传文件与 N，文件不存在不崩
├─ day03_wordcount.py    第三版（当前）：加 logging、pathlib、N 非数字的兜底
├─ test_wordcount.py     pytest 用例（4 个）
├─ sample.txt            英文样本文本（24 个不同词）
├─ wordcount.log         运行日志（已在 .gitignore 里，不进仓库）
├─ journal.md            每天三行的学习日志
└─ README.md             本文件
```

## 怎么跑

```bash
cd D:\python\project\bootcamp

python day03_wordcount.py sample.txt 10    # 前 10 个高频词
python day03_wordcount.py sample.txt 20    # 前 20 个
python day03_wordcount.py                  # 缺参数：打印用法后退出
python day03_wordcount.py nope.txt         # 文件不存在：提示后退出，不抛堆栈
python day03_wordcount.py sample.txt abc   # N 不是数字：提示 "N必须是数字"
```

参数：`<文件> [N]`，N 缺省 10。

- **结果走 stdout**（`print`）：那是给人看的结果；
- **过程与异常走 `wordcount.log`**（UTF-8、带时间戳与级别）：那是给自己排障用的。

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

同时 `wordcount.log` 里会多一行：

```
2026-11-05 20:09:26,501 [INFO] __main__ - 读取文件成功
```

## 怎么测

```bash
python -m pytest -v
# 4 passed in 0.06s
```

用 `python -m pytest` 而不是裸 `pytest`：前者保证用的是**当前这个解释器**装的那个 pytest，环境错乱时不会骗你。

| 用例 | 测什么 | 期望 |
|---|---|---|
| `test_split_lowercase` | 大小写归一 | `"Hello HELLO"` → `["hello", "hello"]` |
| `test_split_ignores_punct` | 标点被切掉 | `"a,b.c"` → `["a", "b", "c"]` |
| `test_count_top_n` | 取前 N 的语义 | `["a","a","b"]` 取 1 条 → `[("a", 2)]` |
| `test_empty_text` | 空输入不炸（这一层） | 空文本 → `[]` |

**看红比看绿重要**：随便改一行断言 → `python -m pytest -v` → 读 `assert 实际 == 期望` 那两个值 → 再改回来。你现在知道"红"长什么样，面试问"你怎么写测试"才有的说。

## 数据库练习（W2 内容提前做的）

```sql
create database bootcamp default charset utf8mb4;
use bootcamp;

create table words (
    id         int primary key auto_increment,
    word       varchar(50) not null,
    freq       int not null,
    created_at datetime default current_timestamp
);
```

增删改查各一条：

```sql
insert into words (word, freq) values ('python', 4), ('is', 4), ('the', 8);
select * from words where freq > 2;
update words set freq = 1 where word = 'the';
delete from words where word = 'the';
select word, freq from words order by freq desc limit 10;
```

表结构（`desc words`）：

| Field | Type | Null | Key | Default | Extra |
|---|---|---|---|---|---|
| id | int | NO | PRI | NULL | auto_increment |
| word | varchar(50) | NO | | NULL | |
| freq | int | NO | | NULL | |
| created_at | datetime | YES | | CURRENT_TIMESTAMP | DEFAULT_GENERATED |

两个当时没注意到的点：
- `words` 上没有 `unique(word)`，所以只能 `update` 改，不能一条语句搞定"有就更新、没有就插入"；
- 字符串用单引号是标准写法（双引号在默认 SQL 模式下也能用，但换数据库就未必）。

## 代码怎么长成这样（git 历史）

| 提交 | 改了什么 | 为什么 |
|---|---|---|
| `day1` | 四个函数：read / split / count / print | 先跑通，别的都往后放 |
| `day2` | 命令行传文件与 N；`FileNotFoundError` 兜底 | 换文件不用改代码；报错要说人话 |
| `day3` | `logging` 双通道（文件 + 控制台） | 事后能查"哪次运行、读了哪个文件" |
| `chore` | 修 `.gitignore` 拼写，忽略 `wordcount.log` / `__pycache__` | 日志和缓存不该进仓库 |
| `refactor` | `read_text` 改用 `pathlib` | 三行变两行，语义更直白 |
| `docs` | README 重写 + journal 归档 | 项目要能给别人看 |
| `tests` | 补 `test_wordcount.py` 四个用例 | 行为钉住，改代码时敢动手 |
| `fix` | 空输入判空、`count_words` 默认值改回 10、`.gitignore` 补 venv | 第一次提交只加了用例没动代码，第二次才真修——commit 信息要经得起 `git show` |

`git log --oneline` 就能复现这条演进线——面试问"你怎么做版本管理"，指着它讲。

## 已知限制

- **只认英文**：正则 `[A-Za-z]+`，中文整段被丢弃。
- **没去停用词**：`is` / `a` 会占前排，看结果时心里要有数。
- **空输入的兜底是最小实现**：`main()` 里用 `if not cw: return` 挡住 `cw[0]` 越界，但空文件是**静默退出**（没有任何提示），算"不崩"，还不算"处理好"。。
- **没有 CI**：测试只在本机跑，没接 GitHub Actions。

## 环境

Python 3.13.9（项目内 `.venv`），pytest 9.2.0。运行时不依赖第三方库。

## 进度

- [x] Day 1：打印词频前 10
- [x] Day 2：命令行参数 + 文件不存在不崩
- [x] Day 3：`wordcount.log` 里有 INFO 与 ERROR
- [x] Day 4：`git log` 六次以上提交 + README 重写
- [x] Day 5：`pytest` 四个用例，先红后绿
- [x] 数据库：建库建表 + CRUD（W2 提前）
- [ ] Day 6–7：命令行单词本 `add` / `list` / `search` / `delete`

## 三条规矩（给自己）

1. 不许让 AI 生成整个文件——只让它解释报错、review 我写的 20 行。
2. 每段 AI 给的代码，删一行再跑一次，看它怎么坏。
3. 每天在 `journal.md` 写三行：写了什么 / 卡在哪 / 明天第一件事。
