from a2_get import check,get
import pytest
import requests
def test_check_pass():
    class FakeResp: status_code = 200
    check(FakeResp(),200)


def test_check_error():
    class FakeResp: status_code = 200
    with pytest.raises(RuntimeError):
        check(FakeResp(),404)

def test_github_api():
    url = 'https://api.github.com/repos/psf/requests'
    try:
        check(get(url),200)
    except requests.RequestException:
        pytest.skip("网络异常，跳过集成测试")
