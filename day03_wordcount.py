# -*- coding: utf-8 -*-
"""
Day 3：统计文本词频，打印出现次数最多的前 N 个词，用log代替print。

规则：
  - 只用标准库（re / collections），不要 import 第三方
  - 允许查文档、允许问 AI 解释报错，不允许让 AI 直接把这个文件写完

跑通的标准（终端里看到类似输出）：
    1. the      12
    2. python    9
    ...
"""
import logging
import re
import sys
from collections import Counter
from pathlib import Path


def read_text(path):
    """TODO 1：读取文件并返回字符串。

    提示：用 with open(path, encoding='utf-8') as f
    返回：文件内容字符串
    """
    return Path(path).read_text(encoding='utf-8')

def split_words(text):
    """TODO 2：把文本切成单词列表。

    规则：
      - 英文按非字母切分（正则 r"[A-Za-z]+"）
      - 统一转小写
      - 中文暂时不管（Day 2 再处理）

    提示：re.findall(pattern, text)
    返回：list[str]
    """
    return re.findall(pattern=r"[A-Za-z]+",string=text.lower())

def count_words(words,n = 10):
    """TODO 3：统计词频并返回出现次数最多的前 10 个。

    提示：Counter(words).most_common(10)
    返回：list[tuple[str, int]]，例如 [('the', 12), ('python', 9)]
    """
    return Counter(words).most_common(n)

def print_result(pairs):
    """TODO 4：按 “序号 + 词 + 次数” 对齐打印。

    期望格式：1. the 12
    提示：enumerate(pairs, 1)，用 f-string
    """
    for i ,(w,n) in enumerate(pairs,1):
        print(f"{i}. {w:<10} {n}")


def main():
    """TODO 5：把上面四个函数串起来。

    步骤：read_text -> split_words -> count_words -> print_result
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(name)s - %(message)s',
        handlers=[
            logging.FileHandler('wordcount.log', encoding='utf-8'),
            logging.StreamHandler()
            # StreamHandler()作用是：把日志输出到控制台
        ]
    )
    log = logging.getLogger(__name__)
    # 给logging.getLogger(__name__)赋值给log

    # 11.5
    # logging.basicConfig()抄的速查表，一开始不知道它是什么
    # format抄的过程中，%(message)s中 % 和 (message)s中间加了空格导致报错

    if len(sys.argv) < 2:
        print("用法: python day03_wordcount.py <文件> [N]")
        return
    path = sys.argv[1]
    try:
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    except ValueError:
        print("N必须是数字")
        return
    try:
        rt = read_text(path)
        log.info("读取文件成功")
    except FileNotFoundError:
        log.error(f"文件不存在：{path}")
        return
    cw = count_words((split_words(rt)),n)
    print_result(cw)

    assert len(cw) <= n, f"最多有{n}条，实际是{len(cw)}"
    assert cw[0][1] >= cw[-1][1],"没有按次数排序"

if __name__ == "__main__":
    main()


# ============================================================
# TODO 6（顺手练手，不算在 2 小时里）：
#   a) 把停用词去掉（the / a / is / and ...），写在 STOP_WORDS 里
#   b) 打印前 10 改成打印前 N，N 从命令行参数取（Day 2 会正式做）
#   c) 统计总词数和不同词数，一起打印
# ============================================================
