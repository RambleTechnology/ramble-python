import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # 控制台输出
        logging.FileHandler("script.log", mode='a', encoding='utf-8')  # 文件输出
    ]
)

def close_issue_status(driver, url, cookies):
    logging.info("开始设置 cookies 并访问工作时间页面")
     # 访问目标页面，确保 cookies 的域名与页面一致
    driver.get(url)
    logging.info(f"已访问页面: {url}")
    # 设置 cookies
    for cookie in cookies:
        driver.add_cookie(cookie)
        logging.info(f"已添加 cookie: {cookie['name']}")

    # 访问工作时间页面
    driver.get(url)
    logging.info(f"访问页面: {url}")

    try:
        # 等待页面加载并确保问题表格存在
        logging.info("等待页面加载完成...")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table//td/select")))
        logging.info("页面加载完成，开始处理状态下拉框")

        # 找到 id 为 time_input_table 的 table 元素
        table = driver.find_element(By.ID, "time_input_table")

        # 找到该 table 下所有 class 为 wt_iss_link 的 a 标签
        links = table.find_elements(By.CLASS_NAME, "wt_iss_link")
        # 遍历所有链接并打印其文本或执行其他操作
        for link in links:
            logging.info(link.text)  # 打印链接文本
            data_issue_value = link.get_attribute("data-issue")  # 获取 data-issue 属性的值
            logging.info(data_issue_value)  # 打印 data-issue 的值

    
    
    except Exception as e:
        logging.error(f"操作过程中出现错误: {e}")
        raise  # 如果发生异常，抛出异常以便在外层处理

def main():
    # Edge WebDriver 路径
    edge_driver_path = 'D:\\Application\\edgedriver_win64_131\\msedgedriver.exe'

    # 设置 Microsoft Edge WebDriver 服务
    service = Service(executable_path=edge_driver_path)
    driver = webdriver.Edge(service=service)

    # 设置 cookies
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
    
    try:
        # 调用封装的函数
        close_issue_status(driver, "http://demo.nghinsights.com:1234/redmine/work_time/index?day=29&month=11&prj=447&user=122&year=2024", cookies)
    finally:
        driver.quit()  # 关闭浏览器
        logging.info("浏览器已关闭")

if __name__ == "__main__":
    main()
