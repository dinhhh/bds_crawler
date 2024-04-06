import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from crawler import bds_crawler
from exporters import json_exporter
from utils import bypass, logger

from gologin import GoLogin
import config_parser

gl = GoLogin({
    "token": config_parser.get_config()['gologin']['token'],
    "profile_id": config_parser.get_config()['gologin']['profile_id'],
    # "port": random_port
})
def crawl_pages(start: int, end: int):
    debugger_address = gl.start()
    service = Service(rf"{config_parser.get_config()['chrome_driver_path']}")
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920,1200")
    driver = webdriver.Chrome(service=service, options=options)
    for page in range(start, end):
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

def crawl_page(url: str):
    debugger_address = gl.start()
    logger.get_logger().info(f'Start crawl page {url}')
    service = Service(rf"{config_parser.get_config()['chrome_driver_path']}")
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920,1200")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    exporter = json_exporter.JsonExporter()
    crawler = bds_crawler.BdsCrawler(driver=driver, exporter=exporter)
    crawler.crawl()
    logger.get_logger().info('Crawl page done')
    gl.stop()
