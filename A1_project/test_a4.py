import pytest
import yaml
from a2_get import get,check
import requests
from pathlib import Path
CASES = Path(__file__).parent / 'data' / 'cases.yaml'
with CASES.open(encoding='utf-8') as f:
    list1 = yaml.safe_load(f)
@pytest.mark.parametrize('case',list1)
def test_github_cases(case):
    url = case['url']
    code = case['code']
    resp = get(url)
    check(resp,code)
