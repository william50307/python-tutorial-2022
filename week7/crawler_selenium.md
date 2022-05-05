###### tags: `tutorials`

# Web crawler

網路爬蟲泛指的是當我們要收集網路上的資料時會使用到的技術

## Basic concept

![](https://i.imgur.com/F7qILv3.png)

當我們要瀏覽網頁內容時，瀏覽器會發送一個http(s) reqeust給server，server會回傳response給client端，渲染在瀏覽器上就是我們所看到的內容
在網頁上我們所看到的東西都是由HTML、CSS、JavaScript這三個語言所呈現


---
當我們對一個web page的頁面點擊右鍵選擇"檢視原始碼"，我們會看到如右半邊的結果。我們所看到的web page就是由這些原始碼產生的。

所以我們想要取得某個網站的資料時就可以從這個地方下手
![](https://i.imgur.com/LIxSBD0.png)



html由許多不同的`<tag></tag>`所組成，每一個tag都有不同的意義。
例如:
- `<div>` : 分組用 ( block )
- `<p>` : 網頁文字
- `<h1>~<h6>` : 網頁標題
- `<a>` : 超連結
- more ...

我們主要會利用ID與class來定位我們要找的元素

![](https://i.imgur.com/Jug8w2n.png)

## 準備開始...

會用到的套件
- requests
- BeautifulSoup
- selenium (下堂課的內容)

範例網站 : https://quotes.toscrape.com/

接下來我們用python notebook 來 Demo。
https://colab.research.google.com/drive/1ZB_KkU1UiCg-0Jmw7NIZdb9G11CIZidc?usp=sharing

### practice

1. 找出在該網站上所出現的所有作者 https://quotes.toscrape.com/

<!--
```python
authors = []
for i in range(1,11):
    url = 'https://quotes.toscrape.com/page/{}/'.format(i)
    html = rq.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    for ele in soup.select('small'):
        authors.append(ele.text)
authors
``` -->

2. 統計該網站上每一個tag所出現的次數 https://quotes.toscrape.com/

<!-- 
```python
tags = {}
for i in range(1,11):
    url = 'https://quotes.toscrape.com/page/{}/'.format(i)
    html = rq.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    for ele in soup.select('div.tags > a.tag'):
        if ele.text not in tags:
            tags[ele.text] = 1
        else:
            tags[ele.text] += 1
tags
```
-->

3. 請搜尋PTT股票板前20頁標題出現過幾次"台積電"，要跳頁請找出儲存在`<a>`中的url  https://www.ptt.cc/bbs/Stock/index.html


<!-- 
```python
count = 0
url = 'https://www.ptt.cc/bbs/Stock/index.html'
base = 'https://www.ptt.cc' 
for i in range(1,21):

    html = rq.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    for ele in soup.select('div.title > a'):
        if '台積電' in ele.text:
            count += 1
    link = soup.select('a.btn.wide')[1]
    link = link['href']
    url = base+link
count
```
-->