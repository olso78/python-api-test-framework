import pytest
import yaml
import allure
from pathlib import Path
def pytest_generate_tests(metafunc):
    # 1. 判断测试函数是不是需要 "case" 参数
    if 'case' in metafunc.fixturenames:
        # 2.读YAML文件
        cases = Path(__file__).parent / 'data' / 'cases.yaml'
        with open(cases,encoding='utf-8') as f:
            list1 = yaml.safe_load(f)
        # 3.把数据传给parametrize
        metafunc.parametrize("case",list1)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        page = item.funcargs.get("page")
        if page:
            png = page.screenshot()
            allure.attach(png, name="失败截图",
                          attachment_type=allure.attachment_type.PNG)