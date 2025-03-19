import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # 控制台输出
        logging.FileHandler("script.log", mode="a", encoding="utf-8"),  # 文件输出
    ],
)


def close_issue_status(driver, url, cookies):
    logging.info("开始设置 cookies 并访问工作时间页面")
    driver.get(url)
    logging.info(f"已访问页面: {url}")
    # 设置 cookies
    for cookie in cookies:
        driver.add_cookie(cookie)
        logging.info(f"已添加 cookie: {cookie['name']}")
    driver.get(url)
    logging.info(f"访问页面: {url}")

    try:
        logging.info("等待页面加载完成...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//table//td/select"))
        )
        logging.info("页面加载完成，开始处理状态下拉框")

        # 找到 id 为 time_input_table 的 table 元素
        table = driver.find_element(By.ID, "time_input_table")

        # 找到该 table 下所有 class 为 wt_iss_link 的 a 标签
        links = table.find_elements(By.CLASS_NAME, "wt_iss_link")
        ids=[]
        # 遍历所有链接并打印其文本或执行其他操作
        for link in links:
            # 获取 data-issue 属性的值
            id = link.get_attribute(
                "data-issue"
            )  
            ids.append(id)
        logging.info(f"获取到的任务id的数量为：{len(ids)}")
        logging.info(f"获取到的任务id的数量为：{ids}")
        for  id in ids:
            close_by_id(id ,cookies)
           

    except Exception as e:
        logging.error(f"操作过程中出现错误: {e}")
        raise  # 如果发生异常，抛出异常以便在外层处理


def close_by_id(id, cookies):
    # Edge WebDriver 路径
    webdriver_path = "D:\\Application\\edgedriver_win64_131\\msedgedriver.exe"
    # 设置 Microsoft Edge 浏览器选项
    edge_options = Options()
    edge_options.add_argument("--headless")  # 无头模式（不显示浏览器界面）
    edge_options.add_argument("--disable-gpu")  # 禁用 GPU
    edge_options.add_argument("--no-sandbox")  # 对于 Linux 系统，需要这个选项

    # 设置 WebDriver 路径
    service = Service(webdriver_path)
    driver = webdriver.Edge(service=service, options=edge_options)
    # 访问 Redmine 登录页面
    url = f"http://demo.nghinsights.com:1234/redmine/issues/{id}"
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
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    logging.info(f"正在打开任务页面: {url}")
    # 打开指定的任务页面
    driver.get(url)

    # 显式等待任务页面加载完毕
    logging.info("等待任务页面加载...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "编辑")]'))
    )

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
        submit_button = driver.find_element(
            By.XPATH, '//input[@name="commit" and @value="提交"]'
        )

        # 确保提交按钮可点击
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(submit_button))
        submit_button.click()

        # 等待提交完成
        time.sleep(1)

        logging.info("操作完成！任务状态已更新为关闭。")
    else:
        logging.warning("未找到任何编辑按钮！")
    driver.quit()  # 关闭浏览器


def main():
    # Edge WebDriver 路径
    edge_driver_path = "D:\\Application\\edgedriver_win64_131\\msedgedriver.exe"

    # 设置 Microsoft Edge WebDriver 服务
    service = Service(executable_path=edge_driver_path)
    driver = webdriver.Edge(service=service)

    # 设置 cookies
    cookies = [
        {
            "name": "_redmine_session",
            "value": "S1JXdm8wWjlCNEJKQ2pxRW1BUmFTOXBxVmRpZzFhVFF4SUlQdUFuZWovdDZyNmVUeEhRN3FiNHd5NWFBVFJ1NmRtaUV4K0JFMFp1UmFrWDhZV0o5OENFdHRsbk5Rc2pOTGN3Ni9Ib1BHYUhMR0RRQUYxbUtjZHJoS2JKSHpNWFExTmtOMTBTYmtHZHk2ZkJHMmhNV0JkUXpsR1Y4YVhoTVZkemdMeEJTQ3dEdVUzdUNHcmpSTk4wTDZralNob01sa3FldXpkMnhuR0MzampKaW0yZmEweUo5ZXBiblhwM1dmdkZFNU9UWUNvZklLYWxmV2Y0ZmkvQUsrNnZPL2RJL3pHUXhNS056TENlQlJjM2FYZnlyOGJpd016ZzR3NStjZHNnVjY0MGdDWldUZUphbWYySHFKUFdyTXdZZndIdnB5T1ptdDB5RGNhckcxT2F4bzhjWndkMU5Lc1dCYzQ5c1RGa0RVWlQ5U2M2VEpiNkNlRjQ0UmtWbVBkejRsM0xsby9YbzJ4WVFiNnBLS2Y4WmFaTml0LzgrMzZCemhUVFB2ZUxBQXpOS01TaVVmTkd5ckp0M1F5eHVibjFMRG5CYTZlTS9mY3RXc0ZEb3pnSWNRRnl2MnRHYkZvWnFkYkNZZDU2enBNQ1ZPT3EzUUQ3OGcvUDliOEhXOHNjUktHeHJRWThXQXdpTzc0a1Z6eDI5TW1sYWFidXViOGNIdTY5cmRzR0xxS2hROEt3PS0tMUlFdGlrSERROXRZR3V6ZHBXV1EwUT09--a3e2963f02d7e30a6c74fd5ed8a0fa33f3909ed2",
        },
        {"name": "autologin", "value": "3c2bd6bfce32e6e0292863704c526ce3a9349352"},
    ]

    try:
        # 实景数字地图： http://demo.nghinsights.com:1234/redmine/work_time/index?day=29&month=11&prj=408&user=122&year=2024
        
        # 调用封装的函数
        close_issue_status(
            driver,
            "http://demo.nghinsights.com:1234/redmine/work_time/show/p05029?day=5&month=3&prj=461&user=122&year=2025",
            cookies,
        )

        # 按照id循环修改任务状态为 已关闭
        # list=[32907, 32908]
        # for id in list:
        #     close_by_id(id, cookies)
    finally:
        driver.quit()  # 关闭浏览器
        logging.info("浏览器已关闭")


if __name__ == "__main__":
    main()
