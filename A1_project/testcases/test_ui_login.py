import allure
import pytest
from playwright.sync_api import expect
from pathlib import Path


@pytest.mark.ui
def test_login_success(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


@pytest.mark.ui
def test_login_locked_user(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    # 断言:验证页面上出现了红色的报错提示
    expect(page.locator("h3[data-test='error']")).to_be_visible()

    # 截图目录固定到项目内，避免受执行目录影响
    report_dir = Path(__file__).parent.parent / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    img_path = report_dir / "login_error.png"
    page.screenshot(path=str(img_path))
    allure.attach.file(str(img_path), name="登录失败截图",
                       attachment_type=allure.attachment_type.PNG)
