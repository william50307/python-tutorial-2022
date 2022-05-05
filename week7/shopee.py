from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://shopee.tw/search?keyword=%E9%9B%BB%E8%85%A6%E8%9E%A2%E5%B9%95")
time.sleep(2)

height = driver.execute_script("return document.documentElement.scrollHeight")
window_height = driver.execute_script("return window.innerHeight")
current_height = 0
while True:
    if current_height < height:
        driver.execute_script("window.scrollTo(0, arguments[0]);", current_height+window_height)
        current_height += window_height
        time.sleep(2)
    else:
        break 

# remember to escape the special character
titles = driver.find_elements(By.CSS_SELECTOR, "div.ie3A\+n.bM\+7UW.Cve6sh")
print(len(titles))

