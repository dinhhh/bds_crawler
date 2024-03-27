import time
from utils import bypass
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
from gologin import getRandomPort
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from parser import contact_parser, address_parser, project_parser
from object import objs
from crawler import bds_crawler
from exporters import console_exporter
# driver = webdriver.Chrome()

# random_port = get_random_port() # uncomment to use random port

if __name__ == '__main__':
    # gl = GoLogin({
    #     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWZhYzA0Y2ZjOGRmNTFhYWIwODZlN2QiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWZhYzU5Y2RkNWRlMzEyZjUyZmFlMDIifQ.dtJORXH7F6ZiNs3P3GJTfAfsJLHGBrPlkZ2VTDdQd9Y",
    #     "profile_id": "65fac04cfc8df51aab086ec1",
    #     # "port": random_port
    # })

    s = Service(r"C:\Users\dinh\PycharmProjects\bds_scrapy\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920,1200")
    driver = webdriver.Chrome(service=s, options=options)
    # url = "https://batdongsan.com.vn/ban-can-ho-chung-cu-duong-huynh-van-nghe-phuong-sai-dong-prj-le-grand-jardin-sai-dong/cdt-brg-group-mo-ban-quy-hang-l1-l2-view-chiet-khau-cao-nhat-thi-truong-qua-tang-khung-pr39395998"
    # driver.get("https://batdongsan.com.vn/ban-nha-rieng-duong-dai-lo-thang-long-xa-van-con/chinh-chu-ban-4-tang-tai-song-phuong-hoai-duc-ha-noi-km-13-ng-pr35559367")
    for page in range(1, 3):
        url = f"https://batdongsan.com.vn/nha-dat-ban-ha-noi/p{page}"
        driver.get(url)
        bypass.avoid_bot_detection(driver=driver)
        exporter = console_exporter.ConsoleExporter()
        # crawler = bds_crawler.BdsCrawler(driver=driver, exporter=console_exporter)
        # crawler.crawl()
        links = driver.find_elements(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "js__card-title", " " ))]')
        for link in links:
            link.click()
            bypass.avoid_bot_detection(driver=driver)
            crawler = bds_crawler.BdsCrawler(driver=driver, exporter=exporter)
            crawler.crawl()
            driver.execute_script("window.history.go(-1)")
            time.sleep(5)
