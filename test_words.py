from words import load, cmd_add
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
