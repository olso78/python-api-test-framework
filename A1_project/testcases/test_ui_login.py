import pytest

# CI 里没有浏览器依赖：整份用例在缺 playwright 时整体跳过（而不是收集阶段报错）
pytest.importorskip("playwright")
pytest.importorskip("pytest_playwright")

import allure
from playwright.sync_api import expect
from pathlib import Path


@pytest.mark.ui
@pytest.mark.parametrize("username,should_pass",[
    ("standard_user",True),
    ("locked_out_user",False),
    ("problem_user",True),
])
def test_login(page,username,should_pass):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", username)
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    if should_pass:
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    else:
        expect(page.locator("h3[data-test='error']")).to_be_visible()
    page.wait_for_timeout(3000)

# def test_login_success(page):
#     page.goto("https://www.saucedemo.com/")
#     page.fill("#user-name", "standard_user")
#     page.fill("#password", "secret_sauce")
#     page.click("#login-button")
#     expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
#
#
# @pytest.mark.ui
# def test_login_locked_user(page):
#     page.goto("https://www.saucedemo.com")
#     page.fill("#user-name", "locked_out_user")
#     page.fill("#password", "secret_sauce")
#     page.click("#login-button")
#     # 断言:验证页面上出现了红色的报错提示
#     expect(page.locator("h3[data-test='error']")).to_be_visible()
#

