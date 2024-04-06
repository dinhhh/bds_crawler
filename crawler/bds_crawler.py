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
    CONVERT_FROM_TY_TO_TRIEU = 1000

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
            self.parse_price()
        except:
            logger.get_logger().error(f"Error while parse bds at {self.driver.current_url}")

    def parse_price(self):
        raw_price = str(self.get_cus_attr_by_key('Mức giá'))
        if (not raw_price) or raw_price.upper() == 'THỎA THUẬN':
            return

        price = float(str_cleaner.get_all_num_from_str(raw_price)[0]) if len(str_cleaner.get_all_num_from_str(raw_price)) > 0 else None
        if not price:
            logger.get_logger().error(f"Can not parse price from {raw_price}")
            return

        area = -1
        raw_area = str(self.get_cus_attr_by_key('Diện tích'))
        area = float(str_cleaner.get_all_num_from_str(raw_area)[0]) if len(
                str_cleaner.get_all_num_from_str(raw_area)[0]) > 0 else None
        # for cus_att in self.bds.cus_attr:
        #     if 'Diện tích' in cus_att.keys():
        #         raw_area = cus_att['Diện tích']
                # area = float(str_cleaner.get_all_num_from_str(raw_area)[0]) if len(
                #     str_cleaner.get_all_num_from_str(raw_area)[0]) > 0 else None
                # if not area:
                #     logger.get_logger().error(f"Can not parse price from {raw_area}")
                #     return

        total_price = None
        if 'triệu/m²'.upper() in raw_price.upper():
            total_price = price * area
        elif 'tỷ/m²'.upper() in raw_price.upper():
            total_price = price * area * self.CONVERT_FROM_TY_TO_TRIEU
        elif 'triệu'.upper() in raw_price.upper():
            total_price = price
        elif 'tỷ'.upper() in raw_price.upper():
            total_price = price * self.CONVERT_FROM_TY_TO_TRIEU

        self.bds.total_price = str(total_price)
        self.bds.price_per_m2 = str(total_price / area)

    def get_cus_attr_by_key(self, key: str) -> dict:
        for cus_att in self.bds.cus_attr:
            if key in cus_att.keys():
                return cus_att[key]
