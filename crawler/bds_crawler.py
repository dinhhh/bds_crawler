from exporters.abstract_exporter import AbstractExporter
from object.objs import Bds
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from parser import contact_parser, address_parser, project_parser


# crawl page luu thong tin bat dong san cu the
class BdsCrawler():
    exporter: AbstractExporter
    bds: Bds
    driver: Chrome

    def __init__(self, url: str, exporter: AbstractExporter):
        self.exporter = exporter

    def crawl(self):
        self.exporter.export(self.bds)

    def parse_bds(self):
        address = driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "js__pr-address", " " ))]').text
        html_from_page = driver.page_source
        contact = contact_parser.parse(html_from_page)
        address = address_parser.parse(address)
        cus_attrs = driver.find_elements(By.XPATH,
                                         '//*[contains(concat( " ", @class, " " ), concat( " ", "re__pr-specs-content-item", " " ))]')
        project = project_parser.parse(driver=driver)
        desc = driver.find_element(By.XPATH,
                                   '//*[contains(concat( " ", @class, " " ), concat( " ", "js__tracking", " " ))]').text
        l = []
        for attr in cus_attrs:
            txt = attr.text
            i = txt.index("\n")
            key = txt[0:i]
            value = txt[i + 1:len(txt)]
            l.append({key: value})
        bds = Bds()
        bds.title = driver.title
        bds.contact = contact
        bds.address = address
        bds.cus_attr = l
        bds.link = url
        bds.project = project
        bds.desc = desc
