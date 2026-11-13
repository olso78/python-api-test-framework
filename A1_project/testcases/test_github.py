from api.client import get
from common.assert_util import check
import pytest
import requests
from common.logger import logger

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
        resp = get(url)
        check(resp,200)
        logger.info(f"GET {url} -> {resp.status_code}")
    except requests.RequestException:
        pytest.skip("网络异常，跳过集成测试")

def test_github_cases(case):
    url = case['url']
    code = case['code']
    try:
        resp = get(url)
        check(resp,code)
        logger.info(f"GET {url} -> {resp.status_code}")
    except requests.RequestException as e:
        pytest.skip(f"网络异常，跳过集成测试: {e}")
