from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from exporters.abstract_exporter import AbstractExporter
from object.objs import Bds
from parsers import contact_parser, address_parser, project_parser
from utils import logger, str_cleaner

# crawl page luu thong tin bat dong san cu the
class BdsCrawler():
    exporter: AbstractExporter
    bds: Bds
    driver: Chrome

    def __init__(self, driver: Chrome, exporter: AbstractExporter):
        self.driver = driver
        self.exporter = exporter
        self.bds = None

    def crawl(self):
        self.parse_bds()
        if self.bds is not None:
            self.exporter.export(self.bds)

    def parse_bds(self):
        try:
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

            post_info = self.driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "js__pr-config", " " ))]').text.split('\n')
            #  post_info có dạng: ['Ngày đăng', '31/03/2024', 'Ngày hết hạn', '10/04/2024', 'Loại tin', 'Tin thường', 'Mã tin', '39253323']
            for index, key in enumerate(post_info):
                if key.upper() == 'Ngày đăng'.upper():
                    bds.created_date = post_info[index + 1]
                if key.upper() == 'Ngày hết hạn'.upper():
                    bds.expire_date = post_info[index + 1]
                if key.upper() == 'Loại tin'.upper():
                    bds.post_category = post_info[index + 1]
                if key.upper() == 'Mã tin'.upper():
                    bds.id = post_info[index + 1]
                    bds.post_id = post_info[index + 1]
            # set to final attribute
            self.bds = bds
        except:
            logger.get_logger().error(f"Error while parse bds at {self.driver.current_url}")
