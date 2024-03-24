import time
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
    url = "https://batdongsan.com.vn/ban-can-ho-chung-cu-duong-huynh-van-nghe-phuong-sai-dong-prj-le-grand-jardin-sai-dong/cdt-brg-group-mo-ban-quy-hang-l1-l2-view-chiet-khau-cao-nhat-thi-truong-qua-tang-khung-pr39395998"
    # driver.get("https://batdongsan.com.vn/ban-nha-rieng-duong-dai-lo-thang-long-xa-van-con/chinh-chu-ban-4-tang-tai-song-phuong-hoai-duc-ha-noi-km-13-ng-pr35559367")
    driver.get(url)
    address = driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "js__pr-address", " " ))]').text
    html_from_page = driver.page_source
    contact = contact_parser.parse(html_from_page)
    address = address_parser.parse(address)
    cus_attrs = driver.find_elements(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "re__pr-specs-content-item", " " ))]')
    project = project_parser.parse(driver=driver)
    desc = driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "js__tracking", " " ))]').text
    l = []
    for attr in cus_attrs:
        txt = attr.text
        i = txt.index("\n")
        key = txt[0:i]
        value = txt[i + 1:len(txt)]
        l.append({key: value})
    bds = objs.Bds()
    bds.title = driver.title
    bds.contact = contact
    bds.address = address
    bds.cus_attr = l
    bds.link = url
    bds.project = project
    bds.desc = desc
    print(bds)

    # assert "Python" in driver.title
    # driver.close()
    # time.sleep(3)
    # gl.stop()

