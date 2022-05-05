from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests as rq


driver = webdriver.Firefox()
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")

# click the button
button = driver.find_element(By.CSS_SELECTOR, 'button.btn-big').click()

# set cookie on webdriver
#cookie = {'name' : 'over18', 'value' : '1'}
#driver.add_cookie(cookie)
#driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")


# using reqeusts
# res = rq.get('https://www.ptt.cc/bbs/Gossiping/index.html', cookies={'over18':'1'})
# print(res.text)



