from words import load, cmd_add,cmd_delete,cmd_search
def test_load_missing_file(tmp_path):
    fake_path = tmp_path / 'not_exist.json'
    assert load(fake_path) == {}
def test_add_then_load(tmp_path):
    fake_path = tmp_path / 'not_exist.json'
    cmd_add(fake_path,'apple','苹果')
    data = load(fake_path)
    assert data == {'apple':'苹果'}
def test_add_twice_then_load(tmp_path):
    fake_path = tmp_path / 'not_exist.json'
    cmd_add(fake_path,'apple','苹果')
    cmd_add(fake_path,'Apple',"苹果")
    data = load(fake_path)
    assert data == {'apple':'苹果'}
def test_search_prefix(tmp_path): # 造 3 个词，查 "app" 应该只命中 apple 和 application
    fake_path = tmp_path / 'not_exist.json'
    cmd_add(fake_path,'apple','苹果')
    cmd_add(fake_path,'application','应用程序')
    cmd_add(fake_path,'appetite','食欲')
    data = load(fake_path)
    cmd_search(fake_path, 'app')
    assert data == {'apple':'苹果','application':'应用程序','appetite':'食欲'}
def test_delete_missing(tmp_path):# 删不存在的词，文件内容不能变
    fake_path = tmp_path / 'not_exist.json'
    cmd_delete(fake_path,'fire')
    data = load(fake_path)
    assert data == {}