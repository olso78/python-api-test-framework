import allure
from playwright.sync_api import expect
from pathlib import Path

# def test_login_success(page):
#     page.goto("https://www.saucedemo.com/")
#     page.fill("#user-name", "standard_user")
#     page.fill("#password", "secret_sauce")
#     page.click("#login-button")
#     expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
#     page.pause()

def test_login_locked_user(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    # 断言:验证页面上出现了红色的报错提示
    expect(page.locator("h3[data-test='error']")).to_be_visible()


    # 定位文件存放的位置
    report_dir = Path(__file__).parent.parent / "reports"
    # 保证文件存在，没有自动创建
    report_dir.mkdir(parents=True,exist_ok=True)
    # 截图保存到文件
    img_path = report_dir / "login_error.png"
    # 验证失败自动截图
    page.screenshot(path=str(img_path))
    # 图片放到Allure报告
    allure.attach.file(str(img_path), name="登录失败截图", attachment_type=allure.attachment_type.PNG)

    page.pause()