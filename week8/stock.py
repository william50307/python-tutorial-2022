import csv
import requests as rq
from bs4 import BeautifulSoup
import time 

url = 'https://histock.tw/stock/rank.aspx?&p={}&d=1'
# 總頁數
pages = 43
headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

with open('stock.csv', 'w', newline='', encoding='utf-8') as csvfile:
    
    writer = csv.writer(csvfile)
    
    # get fieldnames
    res = rq.get(url.format(1))
    soup = BeautifulSoup(res.text, 'html.parser')
    fields = soup.select('table.gvTB > tr:nth-child(1) div:not([class])')
    writer.writerow([f.text for f in fields])
    

    for i in range(1,pages+1):
        res = rq.get(url.format(i), headers=headers)
        if res.status_code != 200:
            print('error in page', i)
            break
        soup = BeautifulSoup(res.text, 'html.parser')
        trs = soup.select('table.gvTB > tr')
        for tr in trs:
            row = [t.text.replace('\n', '') for t in tr.select('td')]
            if row:
                print(row)
                writer.writerow(row)
        time.sleep(1)