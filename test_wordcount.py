from day03_wordcount import split_words, count_words

def test_split_lowercase():
    # TODO: "Hello HELLO" 应该变成 ["hello", "hello"]
    ...
    assert split_words(('Hello HELLO')) == ['hello', 'hello']
def test_split_ignores_punct():
    # TODO: "a,b.c" 应该变成 ["a", "b", "c"]
    ...
    assert split_words(('a,b.c')) == ["a", "b", "c"]
def test_count_top_n():
    # TODO: ["a","a","b"] 取前 1 个，应该是 [("a", 2)]
    ...
    assert count_words(["a","a","b"]) == [("a", 2)]
def  test_empty_text():
    # TODO: 空字符串应该返回空列表
    ...
    assert count_words([]) == []
