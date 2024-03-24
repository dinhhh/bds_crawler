from object import objs
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from utils import str_cleaner


def parse(driver: webdriver.Chrome) -> objs.Project:
    project_name_element = driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "re__project-title", " " ))]')
    project_name = None
    if project_name_element is not None:
        project_name = project_name_element.text
    html_from_page = driver.page_source
    soup = BeautifulSoup(html_from_page, "html.parser")

    project_investor = None
    icons = soup.find_all(class_='re__icon-office--sm')  # icon before project owner
    if len(icons) > 0:
        tmp = str_cleaner.clean(icons[0].nextSibling.text)
        if tmp is not None and tmp != "Đang cập nhật":
            project_investor = tmp

    project = objs.Project()
    project.name = project_name
    project.investor = project_investor
    return project
