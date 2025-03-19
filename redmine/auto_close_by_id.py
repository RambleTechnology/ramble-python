import logging
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 配置日志
logging.basicConfig(
    level=logging.INFO,  # 日志级别为 INFO，可以根据需要调整为 DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # 控制台输出
        logging.FileHandler('automation_log.txt', mode='a', encoding='utf-8')  # 日志写入文件
    ]
)

def automate_redmine(url, issue_url, cookies, webdriver_path):
    """
    使用 Edge 浏览器自动化登录 Redmine，并执行一些操作（如编辑任务状态）。
    
    :param url: Redmine 登录页面的 URL
    :param issue_url: 需要操作的任务页面 URL
    :param cookies: 登录所需的 cookies，格式为 [{'name': 'cookie_name', 'value': 'cookie_value'}, ...]
    :param webdriver_path: Edge WebDriver 的路径
    """
    logging.info("启动 Redmine 自动化脚本...")
    
    # 设置 Microsoft Edge 浏览器选项
    edge_options = Options()
    edge_options.add_argument('--headless')  # 无头模式（不显示浏览器界面）
    edge_options.add_argument('--disable-gpu')  # 禁用 GPU
    edge_options.add_argument('--no-sandbox')  # 对于 Linux 系统，需要这个选项

    # 设置 WebDriver 路径
    service = Service(webdriver_path)
    driver = webdriver.Edge(service=service, options=edge_options)

    try:
        logging.info(f"正在访问 Redmine 登录页面: {url}")
        # 访问 Redmine 登录页面
        driver.get(url)
        
        # 设置 cookies
        logging.info("正在设置 cookies...")
        for cookie in cookies:
            driver.add_cookie(cookie)
            logging.debug(f"添加 cookie: {cookie['name']} = {cookie['value']}")

        # 刷新页面，确保 cookies 生效
        logging.info("刷新页面以应用 cookies...")
        driver.refresh()
        
        # 等待页面加载
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        logging.info(f"正在打开任务页面: {issue_url}")
        # 打开指定的任务页面
        driver.get(issue_url)
        
        # 显式等待任务页面加载完毕
        logging.info("等待任务页面加载...")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "编辑")]')))
        
        logging.info("正在查找编辑按钮...")
        # 查找所有编辑按钮
        edit_buttons = driver.find_elements(By.XPATH, '//a[contains(text(), "编辑")]')

        if edit_buttons:
            logging.info("找到多个编辑按钮，选择第一个按钮进行点击...")
            # 选择第一个可点击的编辑按钮
            edit_button = edit_buttons[0]
            
            # 滚动到元素位置，确保它在视口内
            driver.execute_script("arguments[0].scrollIntoView(true);", edit_button)

            # 等待按钮可点击
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(edit_button))

            # 使用 JavaScript 执行点击操作
            logging.info("点击编辑按钮...")
            driver.execute_script("arguments[0].click();", edit_button)

            # 等待编辑页面加载
            time.sleep(2)  # 等待编辑页面加载

            logging.info("正在更改任务状态...")
            # 更改任务状态（假设下拉框 ID 为 'issue_status_id'）
            status_dropdown = driver.find_element(By.ID, "issue_status_id")
            
            # 确保下拉框可点击
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(status_dropdown))
            status_dropdown.click()
            time.sleep(1)
            
            # 假设 "关闭" 选项已经在下拉框中
            status_dropdown.send_keys("已关闭") 

            logging.info("定位并点击正确的提交按钮...")
            # 找到正确的提交按钮: <input type="submit" name="commit" value="提交">
            submit_button = driver.find_element(By.XPATH, '//input[@name="commit" and @value="提交"]')
            
            # 确保提交按钮可点击
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(submit_button))
            submit_button.click()
            
            # 等待提交完成
            time.sleep(3)

            logging.info("操作完成！任务状态已更新为关闭。")
        else:
            logging.warning("未找到任何编辑按钮！")

    except Exception as e:
        logging.error(f"发生错误: {e}", exc_info=True)
    
    finally:
        logging.info("关闭浏览器...")
        driver.quit()  # 关闭浏览器
        logging.info("脚本执行完毕.")

# 调用示例
if __name__ == "__main__":
    # Redmine 登录页面和任务页面 URL
    redmine_url = "http://demo.nghinsights.com:1234/redmine"
    issue_url = "http://demo.nghinsights.com:1234/redmine/issues/32751"
    
    # 登录所需的 cookies
    cookies = [
        {
            "name": "_redmine_session",
            "value": "Z1lnWGRKbG9BV2JiTHhrTjdjd3hWaTl2WUtMOEFJT1ptRUo5eVlzQVBsNnlVSWRidmNGOVpvL1loR3ZWbFdsYVlPdUNGcEppZ3VlRUp3RDRZb3lPNzZKYVpIZlVSK0paTkdqZTRIa2thbnpXQ3l3c3FVVnRuMlBveFA5WEdtaXZuZDVLYzRVMUUwVEZ1WjhvRHNTNnF1M2RCS2pLNTFReEFCYzluVmlwMlVPemlPM1J1U09qMGJYVWNWRzRNOW95Lzhpc0k3R0lYSTBTV3hCRC9VZ1hZNmNURjF2WUU3ZWN2Q1FKNFVORjdWdWFFMk94MFg4T2ZhL3F6c0ViRjFRZWZkV1I5TjM3b1JHZWVPZ3VicE1LNFZuaXJ6c05JL3BMejJIVlFYc3ZWeVJCcXJXZENZdXJwSHFUVE9VVFdZQ0xKV0VSYlZOVVErSXI0RWhrd0VBKzFOVFp2KzFGWUlYT2NzYllYd242Q0lVbG44UEZ4TmZQSmlCMTRIUlgvOXE0WkQwRysxekJLT0I2VEZsL3VpRkVCdHFPVGZPaXo5T3I0NVVzSEtoU2Fpd3pKN2ZaVWViYjJmWHljTVpaNDA5UERSUmw4KzhkaGREaUtORDhSamNyaFc0c2dETVM5OHpFNmg1aFdreHhYTExqSHllRXorNGlONmVTWmtrclV2ZkdQWGhyMHJzdUVmUTFZOVFVcHF6OG16cUY0TU40STJiZVNtT0hQdWE4OVE0PS0tUnJETWl6UmFjalVyN1dZNkV4Y3BMdz09--f9e8e5184f4c70d9d1cf334424b0b978e250402e"
        },
        {
            "name": "autologin",
            "value": "3c2bd6bfce32e6e0292863704c526ce3a9349352"
        }
    ]
    
    # WebDriver 的路径（请根据实际情况修改）
    webdriver_path = "D:\Application\\edgedriver_win64_131\msedgedriver.exe"  # 替换为实际的 msedgedriver 路径
    
    # 调用自动化函数
    automate_redmine(redmine_url, issue_url, cookies, webdriver_path)
