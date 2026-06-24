import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


EDGE_DRIVER_PATH = "D:\\Application\\edgedriver_win64\\msedgedriver.exe"
BASE_URL = "http://demo.nghinsights.com:1234/redmine"
WORK_TIME_URL = (
    f"{BASE_URL}/work_time/index?day=8&month=5&prj=507&user=122&year=2026"
)
COOKIES = [
    {
        "name": "_redmine_session",
        "value": "cDdOVHE1VkZjckkwa0djeXg1V2h5M3hLeGtJcUtNNE1sTzgzU1NNOWxtcUl3RVRkcForeldlSm1XVlRIWmtwaTgvZiszYjlFd2pOQ1d6N0FxYThxbTVRUWFweml1VXBMYmpVbWRmU05ZTHFMTDgrS1FPOHFLU0c4SmhDMWtnTjl3ZkpwWGIvWnN1S2pxbjJEMFREUU1LSGY1b0M2cklvZDZYc3hBR21CaGZaZ0MvV0Z1RkdPcmNXb1RqT0Vwc0JBWFEwY045YkZKZTlCMHA0NHArZWNhWDczbXFGYjJwL2ZzQnRkNXpLbzk3STlzNEhPMWNDcW5JYjdoNkFNU3hGcHI4STV6RUxwVHBYOUZqYmdaakdDaVFVMUNTOEhPYXQ0YlBXa1VVRGJPSEZOeUMzNWR6N3Y3SGpaNVRGeDhZV2haeDR0L2dFR28zYlh4OFNXblAvNEc3RlAxUkloRVRaNEhlWC82dHdJcjVJdmw0cDdUVUFjdmRIRXJmeUpYUWtLaGthMVdvMWZqWVZENEFyUDdER2VIWHozVWlGdHdoV0hhU3VNOHk4WkUwcjhoZkxHa0JrbDZpdERzUC9SRW1JRVc1OGhkelFtbFJOcVEwY3JpM3pwd09xV1dpeXBtUm0xaU9XTGdlNXVKYTR3dlNqcUdZYzR4T1VNdWZENk14R3grYlUxZlZGV3hYZjJMYXMyTENEY0RUQU5hL04vZkNmcVcxTnhyUDZwdVNVPS0tUEx4TEN1MWRZd3FyZzlJdlFBdzRZQT09--cf307c945776ff3e3035b61931174e9ef96f0bbb",
    },
    {"name": "autologin", "value": "585fcf4294c30606de7938c1af2a876886f3c7c2"},
]
WAIT_TIMEOUT = 10


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  # console output
        logging.FileHandler("script.log", mode="a", encoding="utf-8"),  # file output
    ],
)


def create_driver(headless=False):
    edge_options = Options()
    if headless:
        edge_options.add_argument("--headless")
        edge_options.add_argument("--disable-gpu")

    service = Service(executable_path=EDGE_DRIVER_PATH)
    return webdriver.Edge(service=service, options=edge_options)


def apply_cookies(driver, cookies):
    logging.info("Setting cookies...")
    for cookie in cookies:
        driver.add_cookie(cookie)
        logging.debug(f"Added cookie: {cookie['name']}")


def collect_issue_ids(driver):
    WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//table//td/select"))
    )
    table = driver.find_element(By.ID, "time_input_table")
    links = table.find_elements(By.CLASS_NAME, "wt_iss_link")

    ids = []
    for link in links:
        try:
            issue_id = link.get_attribute("data-issue")
            if not issue_id:
                logging.warning("Current link has no data-issue, skipped")
                continue
            ids.append(issue_id)
        except Exception as e:
            logging.error(f"Error processing one link, skipped: {e}")
    return ids


def close_issue_status(driver, url, cookies):
    driver.get(url)
    apply_cookies(driver, cookies)
    driver.refresh()
    logging.info(f"Visiting page: {url}")

    try:
        logging.info("Waiting for page to load...")
        logging.info("Page loaded, start collecting issue ids")
        ids = collect_issue_ids(driver)

        logging.info(f"Collected issue id count: {len(ids)}")
        logging.info(f"Collected issue ids: {ids}")

        for issue_id in ids:
            try:
                close_by_id(issue_id, cookies)
            except Exception as e:
                logging.error(f"Error closing issue ID {issue_id}, skipped: {e}")
                continue

    except Exception as e:
        logging.error(f"Error in close_issue_status: {e}")
        raise


def close_by_id(issue_id, cookies):
    driver = create_driver(headless=True)
    url = f"{BASE_URL}/issues/{issue_id}"
    try:
        driver.get(url)
        apply_cookies(driver, cookies)

        logging.info("Refreshing page to apply cookies...")
        driver.refresh()
        WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        logging.info(f"Opening issue page: {url}")
        driver.get(url)

        logging.info("Waiting for issue page to load...")
        WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "\\u7f16\\u8f91")]'))
        )

        logging.info("Finding edit button...")
        edit_buttons = driver.find_elements(By.XPATH, '//a[contains(text(), "\\u7f16\\u8f91")]')

        if edit_buttons:
            logging.info("Found edit button(s), clicking the first one")
            edit_button = edit_buttons[0]

            driver.execute_script("arguments[0].scrollIntoView(true);", edit_button)
            WebDriverWait(driver, WAIT_TIMEOUT).until(EC.element_to_be_clickable(edit_button))

            logging.info("Clicking edit button...")
            driver.execute_script("arguments[0].click();", edit_button)

            time.sleep(2)

            logging.info("Updating issue status...")
            status_dropdown = driver.find_element(By.ID, "issue_status_id")

            WebDriverWait(driver, WAIT_TIMEOUT).until(EC.element_to_be_clickable(status_dropdown))
            status_dropdown.click()
            time.sleep(1)

            # set status to 已关闭
            status_dropdown.send_keys("\u5df2\u5173\u95ed")

            logging.info("Finding and clicking submit button...")
            submit_button = driver.find_element(
                By.XPATH, '//input[@name="commit" and @value="\\u63d0\\u4ea4"]'
            )

            WebDriverWait(driver, WAIT_TIMEOUT).until(EC.element_to_be_clickable(submit_button))
            submit_button.click()

            time.sleep(1)
            logging.info("Done. Issue status has been updated to closed.")
        else:
            logging.warning("No edit button found.")
    finally:
        driver.quit()


def main():
    driver = create_driver()

    try:
        close_issue_status(driver, WORK_TIME_URL, COOKIES)
    finally:
        driver.quit()
        logging.info("Browser closed")


if __name__ == "__main__":
    main()
