from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time


def avoid_bot_detection(driver: Chrome):
    time.sleep(5)
    # By pass check box
    # https://stackoverflow.com/questions/76575298/how-to-click-on-verify-you-are-human-checkbox-challenge-by-cloudflare-using-se
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(
        (By.XPATH, "//iframe[@title='Widget containing a Cloudflare security challenge']")))
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@class='ctp-checkbox-label']"))).click()

