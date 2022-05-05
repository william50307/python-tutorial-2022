from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.get("https://shop.pxmart.com.tw/v2/official/SalePageCategory/255?sortMode=Sales")
#time.sleep(3)
#products = driver.find_elements(By.CSS_SELECTOR, "div.sc-fzXfNM")
element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.sc-fzXfNM"))
    )
print(len(element))