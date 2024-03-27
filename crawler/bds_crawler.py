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

    def __init__(self, driver: Chrome, exporter: AbstractExporter):
        self.driver = driver
        self.exporter = exporter

    def crawl(self):
        self.parse_bds()
        self.exporter.export(self.bds)

    def parse_bds(self):
        address = self.driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "js__pr-address", " " ))]').text
        html_from_page = self.driver.page_source
        contact = contact_parser.parse(html_from_page)
        address = address_parser.parse(address)
        cus_attrs = self.driver.find_elements(By.XPATH,
                                         '//*[contains(concat( " ", @class, " " ), concat( " ", "re__pr-specs-content-item", " " ))]')
        project = project_parser.parse(driver=self.driver)
        desc = self.driver.find_element(By.XPATH,
                                   '//*[contains(concat( " ", @class, " " ), concat( " ", "js__tracking", " " ))]').text
        custom_attrs = []
        for attr in cus_attrs:
            txt = attr.text
            i = txt.index("\n")
            key = txt[0:i]
            value = txt[i + 1:len(txt)]
            custom_attrs.append({key: value})
        bds = Bds()
        bds.title = self.driver.title
        bds.contact = contact
        bds.address = address
        bds.cus_attr = custom_attrs
        bds.link = self.driver.current_url
        bds.project = project
        bds.desc = desc
        self.bds = bds
