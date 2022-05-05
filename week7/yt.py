from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Firefox()
driver.get("https://www.youtube.com/")
time.sleep(1)
buttons = driver.find_elements(By.CSS_SELECTOR, "yt-formatted-string.style-scope.yt-chip-cloud-chip-renderer")

for button in buttons:
    if '音樂' in button.text:
        music = button

music.click()
time.sleep(1)
test = driver.execute_script('return 100')

# scroll to bottom
height = driver.execute_script('return document.documentElement.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight)')
    time.sleep(2)
    newheight = driver.execute_script('return document.documentElement.scrollHeight')
    if newheight == height:
        break
    height = newheight

titles = driver.find_elements(By.CSS_SELECTOR, 'yt-formatted-string#video-title')
print(len(titles))
#for t in titles:
#    print(t.text)