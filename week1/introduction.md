# Introduction
## about me ...
陳智原，資管111(大四)


- 熟悉web、還有一些前後端框架
- 專案做IOT相關，所以略懂
- 修了蠻多machine learnning的課，也會深度學習，做過相關研究
- 很喜歡寫python，如果能用python就絕對不用其他語言 :satisfied:

## What is python?
python是一種易學習的高階語言，是通用型程式語言，意味著其應用不局限於某個領域，因此python可以用在幾乎任何地方，例如:人工智慧、資料分析、自動化程式、遊戲開發、web開發、爬蟲。。。
![](https://i.imgur.com/OVbtj2R.png)

## Why python?
python的設計強調簡潔與可讀性，其優雅的語法讓他快速的成為當前的熱門語言之一，大家之後一定會慢慢感受到python的魅力:grin:
![](https://i.imgur.com/wM0rWIE.png)

# 廢話不用多說，直接開始ㄅ


[下載python](https://www.python.org/)
![](https://i.imgur.com/Yz5EzAR.png)

## 該用甚麼寫?
- Visual studio code
- google colab **(推薦)**
- python intepreter


## Getting started with python
> 先把程式想像成是一個計算機

`+` `-` `*` `/`分別對應加減乘除
```python
>>> 17 + 3
20
>>> 17 - 3
14
>>> 17 * 3
51
>>> 17 / 3
5.66666666667
>>> 2 + 3 * 4
14  #一樣是先乘除後加減!
>>> (2 + 3) * 4
20  #括號會先做，跟你熟知的數學運算一樣
```

不免俗地來一段hello world!
```python
>>> print('hello world!') #這個用''框起來的東西叫字串，之後會再說明
hello world!
```

### Exercise

1. 計算自己的BMI。 (bmi = 體重除以身高平方), hint:次方的符號為`**`
2. 1美金=30台幣，200台幣等於多少美金?

## type
每個值都會有它的type，你可以輸入```type(value)```來查看某個value的type
- 整數(int)
- 浮點數(float)
- 字串(string)
- 布林數(booling)
- 串列(list)
- more...

### Exercise
1. 試輸入"hello" + "world"，how about "hello" * "world"
2. 試輸入"hello" + 3, how about "hello" * 3
3. 試輸入0.5 + 3, how about 0.5 * 3

## 變數 Variables


變數的意義為: **用來帶表某個值(value)**
> `#`這個符號代表了註解，用來說明某一段程式碼的功用

```python
>>> a = 1   # 宣告一個名為a的變數，這個變數指向1，這個動作稱為"賦值"
>>> b = 2   # 同理，創造一個名為b的變數
>>> a       # 接著我們把a這個變數所指向的數值印出來
1
>>> b
2
>>>
```

我們利用這張圖來看變數與值之間的關係

![Variable diagram](https://i.imgur.com/wyocCHg.png)

我們也可以改變某個變數所指向的值

```python
>>> a = 2    # 讓a改成指向2
>>> a
2
>>>
```

現在我們的圖會長這樣...

![Variable diagram](https://i.imgur.com/zVUrVmE.png)


我們可以讓某個變數b指向另一個變數a，則變數b也會指向變數a所指向的值

```python
>>> a = 1
>>> b = a  # 這個動作會讓b擁有a原本的值，也就是1
>>> a = 5
>>> b      # b 的沒有改變，還是1
1
>>>
```

如果我們還沒有宣告某個變數，則會出現錯誤...

```python
>>> thingy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'thingy' is not defined
>>>
```



- 變數永遠指向某個value，**他們永遠不會指向某個變數** 
- 多個不同變數可以指向同一個值，但一個變數不能指向多個值


python中的變數是**case-sensitive**，意思是英文中的大小寫被視為不同的"字"


```python
>>> thing = 1
>>> THING = 2
>>> thIng = 3
>>> thing
1
>>> THING
2
>>> thIng
3
>>>
```

python中有些特殊的**保留字(keywords)**，不能被用來當成變數名稱，例如:`False`、`break`、`if`、`pass`，這些保留字有特殊意義，之後會詳細介紹
> 你可以輸入`help('keywords')`來查看更多python中的保留字


```python
>>> if = 123
  File "<stdin>", line 1
    if = 123
       ^
SyntaxError: invalid syntax
>>>
```
當我們利用`=`賦值時，請注意，`=`的右邊會先執行，這代表我們可以在`=`右邊做一些簡單的運算後再賦值

```python
>>> a = 1
>>> a = a + 1
>>> a
2
>>> a = a * 2
>>> a
4
```

對於變數的運算，底下是一些常見的簡寫

```python
>>> a += 2          # a = a + 2
>>> a -= 2          # a = a - 2
>>> a *= 2          # a = a * 2
>>> a /= 2          # a = a / 2
>>>
```

字串其實也可以做類似的運算

```python
>>> a = 'hello'
>>> a *= 3
>>> a += 'world'
>>> a
'hellohellohelloworld'
>>>
```


### Exercise

```python
>>> a = 5
>>> a += 5
>>> a *= 2
>>> a
?  
```
<!-- 20 -->
```python
>>> a = 'hello'
>>> b = 'world'
>>> a + b
?
```
<!-- 'helloword' -->



## Good and bad variable names

變數可以包含不同字元與數字，通常我們都用小寫，並搭配底線`_`
每個變數都有它代表的**意義**，因此命名變數時要能讓人一看就知道這個變數的用途為何
> **程式是寫給人看的!!!**


```python
>>> magic_number = 123
>>> greeting = "Hello World!"
>>>
```

壞的示範:

```python
>>> magicNumber = 3.14          # looks weird
>>> Greeting = "Hello there!"   # we usually use lowercase 
>>> x = "Hello again!"          # what the heck is x?
>>>
```


## 布林值 Booleans

`True` 跟 `False` 分別代表了 `真` 與 `假`.
`==` 代表比較兩個數， 因此`a == 1` 的意思為 : a是否等於1? 
其結果就會由`True` or `False`呈現

```python
>>> a = 1
>>> a == 1
True
>>> a = 2
>>> a == 1
False
>>>
```

## None

`None`在python中代表`空`、`沒有東西`，它也是一種值
它是某些東西的預設值，之後會再看到它
我們現在只需要知道它代表`空`、`沒有東西`



## 其他跟`比較`有關的運算子

到目前為止我們只認識`==`，而python的世界中還有很多不同的比較形式。
|   usage   | Description                       | True examples         |
|-----------|-----------------------------------|-----------------------|
| `a == b`  | a is equal to b                   | `1 == 1`              |
| `a != b`  | a is not equal to b               | `1 != 2`              |
| `a > b`   | a is greater than b               | `2 > 1`               |
| `a >= b`  | a is greater than or equal to b   | `2 >= 1`, `1 >= 1`    |
| `a < b`   | a is less than b                  | `1 < 2`               |
| `a <= b`  | a is less than or equal to b      | `1 <= 2`, `1 <= 1`    |


我們可以利用 `and` 跟 `or` 連接成更長的運算

| Usage     | Description                               | True example                      |
|-----------|-------------------------------------------|-----------------------------------|
| `a and b` | a is True and b is True                   | `1 == 1 and 2 == 2`               |
| `a or b`  | a is True, b is True or they're both True | `False or 1 == 1`, `True or True` |

`not` 代表相反 

```python
>>> not False
True 
>>> not True
False 
```

### Exercise

What's the output?

```python
>>> 1 != 2 or 2 == 3
?
```
<!-- True -->
```python
>>> 1 != 2 and 3 == 2 or 2 == 1 or True
?
```
<!-- True -->

## Summary

- 變數有它的名字跟值，我們可以宣告變數、或改變變數的值 -> `name = value`
- a += 1 等價於 a = a + 1
- `=`是用來賦值的，而`==`是用來比較的
- 變數命名盡量用小寫，並且用有意義的名稱
- `True` 跟 `False` 是布林值(boolean value)，比較兩個數會產生布林值


[source](https://github.com/Akuli/python-tutorial)