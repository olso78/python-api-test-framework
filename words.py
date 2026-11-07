import json
import sys


def load(path):
    try:
        with open(path,encoding='utf-8') as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        return {}
    except FileNotFoundError:
        return {}
    # 读文件，用JSON模块转成字典
def save(path,data):
    # 写文件，用字典转成JSON字符串写入文件
    with open(path,'w',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=4)
def cmd_add(path,word,meaning):
    # 拿到现有的字典
    data = load(path)
    # 把新单词和释义放入字典
    data[word] = meaning
    # 写回文件
    save(path,data)
    print("添加成功")
def cmd_list(path):
    # 读出来/打印出来
    # 取文件
    data = load(path)
    # 用items方法遍历字典
    for word,meaning in data.items():
        print(f"{word:<10} : {meaning}")
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("python words.py [add|list]")
        sys.exit()
    # 根据用户在终端敲的命令，决定调用哪个函数
    elif sys.argv[1] == 'add':
        if len(sys.argv) < 4:
            print("未输入单词")
            sys.exit()
        else:
            print("格式：python words.py add 单词 释义")
            cmd_add('words.json',sys.argv[2],sys.argv[3])
    elif sys.argv[1] == 'list':
        cmd_list('words.json')

"""
做题时，向ai进行的解释、指导以及踩坑
这个规划非常清晰，完全是“测试驱动开发（TDD）”的标准流程。你先把基础的读和写（I/O）封装好，并且立刻去验证编码问题，这能帮你避开下午写测试时 80% 的坑。

根据你的要求，我提供分步指导和排雷提示，绝对不写完整代码：

第一步：先做 load 和 save（重点在编码和异常）
1. load(path) -> dict

怎么想：用 with open() 读文件，然后用 JSON 模块转成字典。但要注意，第一次跑的时候，words.json 根本不存在。

提示：

用 try...except FileNotFoundError: 来捕获文件不存在的情况，直接 return {}。

读取时用 json.load(f) 即可。

2. save(path, data)

怎么想：把字典转成 JSON 字符串写进文件。

提示：

打开文件时必须是 open(path, 'w', encoding='utf-8')。记得一定要写 w 模式，否则没法写入。

题目要求的核心是 json.dump(data, f, ensure_ascii=False, indent=2)。你在写的时候，体会一下 ensure_ascii=False 怎么把 \u82f9\u679c 变成“苹果”的。

👉 动作：写完这两个后，在底部随便写个测试（比如 save('test.json', {'apple': '苹果'})），去文件夹里点开看一眼，确认中文正常显示且格式是缩进的。

第二步：做 cmd_add（体会“读-改-写”流程）
怎么想：既然有了 load 和 save，cmd_add 就变成了一个流水线作业。

提示：

调 load(path) 拿到现有的字典。
把新单词和释义塞进字典：data[word] = meaning。
调 save(path, data) 存回去。
最后记得 print() 一句成功提示。
第三步：做 cmd_list（复习 f-string）
怎么想：读出来，打印出来。

提示：

调 load(path) 拿到字典。
遍历这个字典的 .items()，用你前几天的知识：for word, meaning in data.items():。
用 f-string 打印，想对齐的话可以用 {word:<15}。
第四步：做 main（复习 sys.argv）
怎么想：根据用户在终端敲的命令，决定调用哪个函数。

提示：

假设用户在终端敲：python card.py add apple 苹果

sys.argv[1] 会是 "add"，sys.argv[2] 是 "apple"，sys.argv[3] 是 "苹果"。

用 if sys.argv[1] == 'add': 来分发。

防呆提示：在做判断之前，记得先检查一下 len(sys.argv)，防止用户什么都不敲直接运行，导致报错 IndexError。

踩过的超级大坑）
这个工具虽然小，但你把所有新手必踩的坑踩了个遍，这波经验极其宝贵：

json.dumps vs json.dump 的区别：

带 s 的（dumps）只能把字典变字符串，你试图直接把文件对象 f 传给它，导致文件被清空但没写进去。

不带 s 的（dump）才是专门用来直接写入文件对象的。

忘记 return 的惨案：

在 load 函数里 json.load(f) 读出了数据，但忘了 return，导致程序拿到的是 None，后面直接报 AttributeError 崩溃。

文件读取的异常双重奏：

你只抓了 FileNotFoundError（找不到文件），漏了 JSONDecodeError（文件是空的或者格式坏了）。

并且，你把 with open() 写在了 try 的外面，导致找不到文件时，try 根本护不住 open()。

sys.argv 的边界防守：

一开始忘了检查 len(sys.argv) < 4，如果用户只输入 add apple（不输释义），程序就会试图取 sys.argv[3]，当场越界报错。

字典键值写反：

把 data[word] = meaning 写成了 data[meaning] = word，差点变成“通过苹果查英文”。
"""