###### tags: `tutorials`

# csv file

這章我們會學一下怎麼用python來讀寫檔案


## writing csv file


### 逐行輸入
```python
import csv

with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    
    writer = csv.writer(csvfile)
    
    # 寫入一行資料
    writer.writerow(['商品', '價錢', '登記時間']) 
    writer.writerow(['水壺', '120', '2021-09-01'])
    writer.writerow(['鍵盤', '1200', '2021-09-01'])
    writer.writerow(['耳機', '2400', '2021-09-04'])

```

:::info 
這裡在開啟 csv 檔案時加上了 newline='' 參數，這是為了讓資料中包含的換行字元可以正確被解析，所以建議在讀取 csv 檔案時都固定加入這個參數。
:::

### 以字典形式寫入

```python
with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    
    fieldnames = ["商品", "價錢", "登記時間"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()

    writer.writerow({"商品" : "水壺", "價錢" : "120", "登記時間" : "2021-09-01"})
    writer.writerow({"商品" : "鍵盤", "價錢" : "1200", "登記時間" : "2021-09-01"})
    writer.writerow({"商品" : "耳機", "價錢" : "2400", "登記時間" : "2021-09-04"})
```



## reading csv file 

### 逐行讀取

```python
with open('products.csv', 'r', newline='', encoding='utf-8') as csvfile:
    
    rows = csv.reader(csvfile)

    # 取得每一行的資料
    for row in rows:
        print(row)
```


### 以字典形式讀取

```python
with open('products.csv', 'r', newline='', encoding='utf-8') as csvfile:
    
    rows = csv.DictReader(csvfile)

    for row in rows:
        print(row)
```


## practice


取得該網站中所有台股資訊 [link](https://histock.tw/stock/rank.aspx?&p=1&d=1)，最後輸出成一個[csv檔](https://github.com/william50307/python-tutorial-2022/blob/main/week8/stock.csv)


