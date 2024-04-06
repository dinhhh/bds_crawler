from selenium import webdriver
from exporters import console_exporter
from crawler import bds_crawler
from object import objs

if __name__ == '__main__':
    bds = objs.Bds()
    bds.cus_attr = [{"Diện tích":"51 m²"}, {"Mức giá":"2,59 tỷ"}]
    bds_crawler = bds_crawler.BdsCrawler(driver=webdriver.Chrome(), exporter=console_exporter.ConsoleExporter())
    bds_crawler.bds = bds
    bds_crawler.parse_price()
    print(bds_crawler.bds)
