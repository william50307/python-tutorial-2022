###### tags: `tutorials`

# functions

function是一段程式的集合，例如我們之前使用的print()、input()都是function，每個function會執行特定的工作，而我們也可以自行定義function...

## define function

要使用函數前，我們要先定義函數，之後才能呼叫它:

```python
def say_hello(): # 定義function
    print('Hello word!')
    
do_nothing()  # 執行這個function
```

這個函數的名稱叫做`say_hello`，呼叫它會執行`print('Hello word!')`這段程式

**output:**
```python
Hello word!
```

## 參數 argument(parameter)

我們可能會需要傳入某個變數到function裡進行運算，方法如下:

```python
def say_something(sentence): #定義函數，並說明這個函數需要傳入一個參數
    print(sentence)

say_something('How are you?')
```

我們定義了一個函數，並且規定這個函數在呼叫時需要傳入一個參數，在上例中，我們把這個變數設為sentence，sentence裡面可以是任何資料型態，例如:string、int、float...。(python不是C/C++ 我們不須規定傳入的data type)，

**output:**
```python
'How are you?'
```

### 再看個範例...
我們想要定義一個function，讓我們輸入直角三角形的兩個邊，並計算出斜邊長度

```python
from math import sqrt #有些函數需要import進來才能使用
def third_len(l1, l2):
    print(sqrt(l1**2 + l2**2))
    
third_len(3,4)
```
outputs:
```
5.0
```

### keyword argument

我們可以為參數設定預設值

```python
def say_something(sentence='Hello'): 
    print(sentence)

say_something()  #不給參數，則取預設值
```
outputs:
```
'Hello'
```

## return 

有時我們會需要function回傳某些值，因此我們會用到`return`

```python
def times_two(num):
    return num * 2

times_two(5)
```
outputs:
```
10
```

`return`的值可以直接進行運算，或assign給別的變數

```python
>>> times_two(5) + times_two(2)
14
>>> value = times_two(12)
>>> value
24
```

`return` 執行完後就會結束function因此下面這個例子不會執行`print`

```python
>>> def return_before_print():
...     return None
...     print("This never gets printed.")
...
>>> return_before_print() #不會執行
>>>
```

## recursive function (補充)

這是一種寫程式的**技巧**，不是python的語法
不過非常好用，之後學資料結構會用到很多...

假設我們要算階層，可以用一個for迴圈解決
```python
>>> x = 5 #計算 5!
>>> result = 1
>>> for i in range(1, x+1):
        result *= i
>>> result
120
```

也可以用recursive function處理...
```python
>>> def factorial(x):
...     if x == 1 : return 1
...     return x * factorial(x-1)
>>> factorial(5)
120
```


來個練習...(其實是政大面試題XD)

```python
def hey(a, b):
	if b>=a : 
        return b+hey(a,b-1)
    else : 
        return 10
```
Question : hey(12, 15) = ?


### Exercise

1. 寫一個function，輸入身高與體重，計算這個人的BMI(記得須回傳結果)

2. 定義一個函數，回傳range(10)裡的第三個奇數