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
    word = word.strip().lower()
    meaning = meaning.strip()
    # 拿到现有的字典
    data = load(path)
    if word in data:
        print("已更新")
    # 写回文件
    else:
        print("添加成功")
    # 把新单词和释义放入字典
    data[word] = meaning
    save(path, data)

def cmd_list(path):
    # 读出来/打印出来
    # 取文件
    data = load(path)
    # 用items方法遍历字典
    for word,meaning in data.items():
        print(f"{word:<5} : {meaning:>5}")

def cmd_search(path,prefix): # 打印所有以 prefix 开头的词
    results = []
    prefix = prefix.strip().lower()
    data = load(path)
    for word,meaning in data.items():
        if word.startswith(prefix) == True:
            results.append((word,meaning))
    if len(results) == 0:
        print(f"没有以{prefix}开头的词")
    else:
        print(f"找到{len(results)}个，{prefix}开头的词")
        for word,meaning in results:
            print(f"{word:<5}:{meaning}")

def cmd_delete(path,word): # 存在就删，不存在要提示
    word = word.strip().lower()
    data = load(path)
    if word not in data:
        print( "没有这个词")
    else:
        del data[word]
        print("已删除")
    save(path,data)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("python words.py [add|list]")
        sys.exit()
    # 根据用户在终端敲的命令，决定调用哪个函数
    elif sys.argv[1] == 'add':
        if len(sys.argv) < 4:
            print("未输入单词")
            print("格式：python words.py add 单词 释义")
            sys.exit()
        else:
            cmd_add('words.json',sys.argv[2],sys.argv[3])
    elif sys.argv[1] == 'list':
        cmd_list('words.json')
    elif sys.argv[1] == 'search':
        cmd_search('words.json',sys.argv[2])
    elif sys.argv[1] == 'delete':
        cmd_delete('words.json',sys.argv[2])
