from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Firefox()
driver.get("https://www.google.com.tw/")
time.sleep(1)
search = driver.find_element(By.CLASS_NAME, "gLFyf")
search.send_keys('Selenium tutorial')

# 方法一 直接提交表單
time.sleep(1)
search.submit()
# 方法二 模擬鍵盤輸入enter
#time.sleep(1)
#search.send_keys(Keys.RETURN) 
# 方法三 找button element所在位置
# time.sleep(1)
# button = driver.find_element(By.CLASS_NAME,"gNO89b")
# button.click()


### AactionChains
# ActionChains(driver).move_to_element(search) \
# .send_keys('Hello').pause(3).double_click().pause(3).send_keys('changed').perform()


### execute_script
# time.sleep(1)
# # 捲動到 2500px 位置
# driver.execute_script('window.scrollTo(0, 2500)')
# time.sleep(1)
# driver.execute_script('window.scrollTo(0, 0)')
# exit()

# time.sleep(1)
# titles = driver.find_elements(By.CSS_SELECTOR, 'h3.LC20lb')
# script = '''
#     let first = arguments[0];
#     let last = arguments[1];
#     alert(first+"\\n"+last);
#     '''

# driver.execute_script(script, titles[0].text, titles[-1].text)   # 執行 JavaScript，印出元素
# time.sleep(5)
# Alert(driver).accept()    # 點擊提示視窗的確認按鈕，關閉提示視窗
