import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def login_to_aliyun(username, password, driver_path='/path/to/your/chromedriver', headless=False):
    """
    使用 Selenium 登录到阿里云开发者平台

    :param username: 登录用户名
    :param password: 登录密码
    :param driver_path: ChromeDriver 路径
    :param headless: 是否启用无头模式（默认 False）
    :return: Selenium WebDriver 实例，登录后的页面
    """
    try:
        # 配置 Chrome 浏览器选项
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument('--headless')  # 无头模式

        logger.info("启动 EDGE 浏览器...")

        # 启动 WebDriver
        driver = webdriver.Edge(executable_path=driver_path, options=options)
        driver.get("https://developer.aliyun.com/")
        logger.info("打开阿里云开发者平台...")

        # 等待页面加载
        time.sleep(3)

        # 点击登录按钮
        logger.info("点击登录按钮...")
        login_button = driver.find_element(By.LINK_TEXT, '登录')
        login_button.click()

        # 等待登录页面加载
        time.sleep(3)

        # 输入用户名和密码
        logger.info("输入用户名和密码...")
        username_input = driver.find_element(By.ID, 'fm-login-id')
        password_input = driver.find_element(By.ID, 'fm-login-password')

        username_input.send_keys(username)
        password_input.send_keys(password)

        # 提交表单
        password_input.send_keys(Keys.RETURN)

        # 等待登录完成
        time.sleep(5)

        # 打印当前页面标题，确认是否成功登录
        logger.info(f"当前页面标题：{driver.title}")

        # 如果页面包含某些特定元素，可以进一步验证登录成功
        if "阿里云" in driver.title:
            logger.info("登录成功！")
        else:
            logger.error("登录失败！请检查用户名、密码或其他问题。")

        return driver

    except Exception as e:
        logger.error(f"发生错误: {e}")
        return None

    finally:
        logger.info("登录过程已完成。")
        # 如果需要关闭浏览器，在此处退出
        # driver.quit()

if __name__ == "__main__":
    # 示例：调用函数进行登录
    username = 'leadingchenml'  # 请替换为你的用户名
    password = 'Naylor123'  # 请替换为你的密码
    driver_path = 'D:\Application\\edgedriver_win64_131\msedgedriver.exe'  # 请替换为你的 chromedriver 路径

    # 执行登录
    driver = login_to_aliyun(username, password, driver_path, headless=False)
    
    # 如果需要，可以继续使用 driver 进行其他操作，例如爬取数据等
    if driver:
        # 示例：获取登录后的页面内容
        logger.info(f"登录后页面的 URL: {driver.current_url}")
