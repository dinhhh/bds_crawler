import time

# driver = webdriver.Chrome()
# import undetected_chromedriver as uc  # TODO: https://github.com/ultrafunkamsterdam/undetected-chromedriver/issues/955
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from crawler import bds_crawler
from exporters import console_exporter
from exporters import json_exporter
from utils import bypass, logger

# random_port = get_random_port() # uncomment to use random port
from gologin import GoLogin

if __name__ == '__main__':
    gl = GoLogin({
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjBjMjk2OWUzZjI2NmJjYzM2NzRhYzkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NjBjMmFiYjQ0YjI2MGUxZDhhOWE4MWYifQ.98w7gKjAN1PPCBVZbz2LlYZALR_gr5-fkSpJCQJefbc",
        "profile_id": "660c296ae3f266bcc3674b1b",
        # "port": random_port
    })
    debugger_address = gl.start()
    s = Service(r"C:\Users\dinh\PycharmProjects\bds_scrapy\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920,1200")
    driver = webdriver.Chrome(service=s, options=options)
    # driver = uc.Chrome(headless=True, use_subprocess=False, driver_executable_path=r"C:\Users\dinh\PycharmProjects\bds_scrapy\chromedriver.exe")
    # url = "https://batdongsan.com.vn/ban-can-ho-chung-cu-duong-huynh-van-nghe-phuong-sai-dong-prj-le-grand-jardin-sai-dong/cdt-brg-group-mo-ban-quy-hang-l1-l2-view-chiet-khau-cao-nhat-thi-truong-qua-tang-khung-pr39395998"
    # driver.get("https://batdongsan.com.vn/ban-nha-rieng-duong-dai-lo-thang-long-xa-van-con/chinh-chu-ban-4-tang-tai-song-phuong-hoai-duc-ha-noi-km-13-ng-pr35559367")

    # Todo: uncomment to run

    for page in range(1, 10):
        domain = "https://batdongsan.com.vn"
        url = f"https://batdongsan.com.vn/nha-dat-ban-ha-noi/p{page}"
        driver.get(url)
        logger.get_logger().info(f"Driver get page {page}")
        bypass.avoid_bot_detection(driver=driver)
        # exporter = console_exporter.ConsoleExporter()
        exporter = json_exporter.JsonExporter()
        # crawler = bds_crawler.BdsCrawler(driver=driver, exporter=console_exporter)
        # crawler.crawl()
        detail_bds_xpath = '//*[contains(concat( " ", @class, " " ), concat( " ", "js__card-title", " " ))]'
        links = driver.find_elements(By.XPATH, detail_bds_xpath)
        for index, link in enumerate(links):
            try:
                loop_links = driver.find_elements(By.XPATH, detail_bds_xpath)
                loop_links[index].click()
                # print(f"{domain}/{link}")
                # driver.get(f"{domain}/{link}")
                bypass.avoid_bot_detection(driver=driver)
                crawler = bds_crawler.BdsCrawler(driver=driver, exporter=exporter)
                crawler.crawl()
                driver.execute_script("window.history.go(-1)")
                time.sleep(5)
            except Exception as e:
                logger.get_logger().error(str(e))
    gl.stop()

    """
    url = f"https://batdongsan.com.vn/ban-shophouse-nha-pho-thuong-mai-duong-huu-nghi-xa-phu-chan-prj-vsip-bac-ninh/can-tien-ban-nh-ndt-can-3-tang-centa-vi-tri-dep-pr39253323"
    driver.get(url)
    post_info = driver.find_elements(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "js__pr-config", " " ))]')
    print("hjx")
    """