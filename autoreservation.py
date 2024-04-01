from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\\Program Files (x86)\\chromedriver.exe"

options = Options()

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()

driver.get("https://www.narunoodlebar.com/")


time.sleep(5)

wait = WebDriverWait(driver, 10)
reserve_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://bookings.airmenus.in/eatnaru/order']")))
reserve_button.click()

while True:
    time.sleep(10)

driver.quit()




















