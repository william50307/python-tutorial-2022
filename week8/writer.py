import csv

# 逐行寫入
# with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    
#     writer = csv.writer(csvfile)
    
#     # 寫入一行資料
#     writer.writerow(['商品', '價錢', '登記時間']) 
#     writer.writerow(['鍵盤', '1200', '2021-09-01'])
#     writer.writerow(['水壺', '120', '2021-09-01'])
#     writer.writerow(['耳機', '2400', '2021-09-04'])
#     writer.writerow(['顯示卡', '12000', '2021-09-01'])
#     writer.writerow(['CPU', '7200', '2021-09-01'])

# 使用dictionary方法寫入
# with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    
#     fieldnames = ["商品", "價錢", "登記時間"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     # 寫入第一列的欄位名稱
#     writer.writeheader()

#     # 寫入一行資料
#     writer.writerow({"商品" : "水壺", "價錢" : "120", "登記時間" : "2021-09-01"})
#     writer.writerow({"商品" : "鍵盤", "價錢" : "1200", "登記時間" : "2021-09-01"})
#     writer.writerow({"商品" : "耳機", "價錢" : "2400", "登記時間" : "2021-09-04"})
    


# with open('products.csv', 'r', newline='', encoding='utf-8') as csvfile:
    
#     rows = csv.reader(csvfile)

#     # 逐行讀取
#     for row in rows:
#         print(row)

with open('products.csv', 'r', newline='', encoding='utf-8') as csvfile:
    
    rows = csv.DictReader(csvfile)

    # 逐行讀取
    for row in rows:
        print(row)