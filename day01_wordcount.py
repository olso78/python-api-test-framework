# -*- coding: utf-8 -*-
"""
Day 1（约 2 小时）：统计文本词频，打印出现次数最多的前 10 个词。

规则：
  - 只用标准库（re / collections），不要 import 第三方
  - 允许查文档、允许问 AI 解释报错，不允许让 AI 直接把这个文件写完

跑通的标准（终端里看到类似输出）：
    1. the      12
    2. python    9
    ...
"""

import re
import sys
from collections import Counter


def read_text(path):
    """TODO 1：读取文件并返回字符串。

    提示：用 with open(path, encoding='utf-8') as f
    返回：文件内容字符串
    """
    with open(path,encoding='utf-8') as f:
        return f.read()
# 11.3
    # 没头绪，看解释才知道咋写

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
#11.3
    # 没头绪，要是没提示我估计都不知道怎么写
    # 看了提示，才知道有 re.findall，但不知道是什么，怎么用，效果是什么
    # 光看提示也会出问题，还真只是提示啊

def count_words(words):
    """TODO 3：统计词频并返回出现次数最多的前 10 个。

    提示：Counter(words).most_common(10)
    返回：list[tuple[str, int]]，例如 [('the', 12), ('python', 9)]
    """
    return Counter(words).most_common(10)
# 11.3
    # 这个只知道 counter 是计数，其他的包括counter怎么用都不知道
    # 返回list[tuple[str, int]]说的简单，但我真不会啊
    # 这答案我不可能想到

def print_result(pairs):
    """TODO 4：按 “序号 + 词 + 次数” 对齐打印。

    期望格式：1. the 12
    提示：enumerate(pairs, 1)，用 f-string
    """
    for i ,(w,n) in enumerate(pairs,1):
        print(f"{i}. {w:<10} {n}")
# 11.3
    # 这个完全不知道怎么写
    # enumerate、pairs不知道啥意思
    # for循环这种用法还是第一次知道，不看资料真不知道能把(words,count)这种东西放到for循环里[次数都忘记是count]
    # 查资料才知道 f-string 是print(f"{}")格式
    # 打印输出咋空格啊
    # words是列表不能随便用
    # 光加宽度不行，还得实际调整每个{}后加空格

def main():
    """TODO 5：把上面四个函数串起来。

    步骤：read_text -> split_words -> count_words -> print_result
    """

    rt = read_text('sample.txt')
    sw = split_words(rt)
    cw = count_words(sw)
    print_result(cw)

    assert len(cw) == 10, f"一定有10条，实际是{len(cw)}"
    assert cw[0][1] >= cw[-1][1],"没有按次数排序"
# 11.3
    # 断言是啥意思啊，作用是啥，关键我写一次我也记不住咋整 --> 断言格式：assert 条件, "失败提示"
    # 为啥运行后的时候断言的内容没打印出来
    # 改了most_common(3)才知道这个断言是用在报错里面的

if __name__ == "__main__":
    main()


# ============================================================
# TODO 6（顺手练手，不算在 2 小时里）：
#   a) 把停用词去掉（the / a / is / and ...），写在 STOP_WORDS 里
#   b) 打印前 10 改成打印前 N，N 从命令行参数取（Day 2 会正式做）
#   c) 统计总词数和不同词数，一起打印
# ============================================================
# 11.3
    # 这个TODO 6 看了题目还是无从下手咋办，就直接不管吗？
