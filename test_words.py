from words import load, cmd_add
def test_load_missing_file(tmp_path):
    fake_path = tmp_path / 'not_exist.json'
    assert load(fake_path) == {}
def test_add_then_load(tmp_path):
    fake_path = tmp_path / 'test.json'
    cmd_add(fake_path,'apple','苹果')
    data = load(fake_path)
    assert data == {'apple':'苹果'}

# 11.7
"""
一、 测试代码本身的坑（test_words.py 里的错误）
在测试里用 sys.argv（脱离终端环境）
现象：运行 pytest 时报 IndexError: list index out of range。
原因：sys.argv 只有在终端手动执行 python words.py add ... 时才有值。pytest 是在后台自动跑的，它的 sys.argv 里只有测试框架自己的参数，根本没有你要的单词。
避坑：测试函数必须自给自足。需要什么参数，直接在测试代码里硬编码传入（如 cmd_add(fake_path, 'apple', '苹果')）。
把目录当文件传给了函数（误用 tmp_path）
现象：报 PermissionError: [Errno 13] Permission denied。
原因：tmp_path 是一个文件夹路径。你直接写了 load(tmp_path)，相当于让 open() 去打开一个文件夹，系统当然拒接。
避坑：一定要用 / 拼接具体的文件名，比如 fake_path = tmp_path / 'not_exist.json'，然后再传 fake_path。
写了没用上，且忘了 assert（假动作）
现象：测试虽然显示 PASSED，但其实毫无意义。
原因：你算出了路径却没赋值，并且没用 assert 去比对结果。没有 assert 的测试函数，只要不抛异常，pytest 就会给它发绿牌。
避坑：测试的灵魂是断言。必须用 assert 实际结果 == 预期结果。
"""