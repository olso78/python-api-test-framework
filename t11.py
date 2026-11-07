import json
import sys

from pylsp_jsonrpc.exceptions import JsonRpcInternalError


def load(path):
    try:
        with open(path) as f:
            return json(f)
    except JsonRpcInternalError:
        return {}
    except FileNotFoundError:
        return {}
def save(path, data):
    with open(path, 'w') as f:
        return json.dump(data,f,ensure_ascii=False, indent=2)
def cmd_add(path, word, meaning):
    word = word.split().lower()
    meaning = meaning.split()
    data =load(path)
    if word in data:
        print("更新")
    else:
        print("添加")
    data[word] = meaning
    save(path, data)

def cmd_list(path):
    data = load(path)
    for word,meaning in data:
        print(f"{word:<5}:{meaning:>5}")
if __name__ == '__main__':
    if len(sys.argv)<2:
        print("未输入指令")
        print("格式：python t11.py [add|list]")
    elif sys.argv[1] == 'add':
        cmd_add(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'list':
        cmd_list(sys.argv[2])
    else:
        print("指令错误")
