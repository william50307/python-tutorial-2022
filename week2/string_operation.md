###### tags: `tutorials`
# strings operation

## indention縮排
python利用```空格```縮排，來代表不同的程式區塊
```python=
if something:
    print('123123')
    print('testing')
else:
    print('else something')
    print('same block in testing')
```
在上例，如果if statement成立，則程式會執行第三第四行，因為他們的縮排**一樣**。
同理若esle成立，則會執行第五第六行。


我們已經知道可以利用`+` `*`來操作字串，例如`'hello'+'world'`以及 `'hello' * 3`

## slicing 切割

先看個範例
```python
>>> our_string = 'hello'
>>> our_string[2:5] #從第二個位置取到第四個位置(5-1)
'llo'
>>> our_string[2:5:2] #從第二個位置取到第四個位置，每次跳2格
'lo'
```
為什麼可以這樣????

![](https://i.imgur.com/yxIkqeV.png)


因此我們可以根據特定的**位置**來切割字串
python的語法就會長得像`some_string[start:end:step]`
我們也可以用負數來切割...

```python
>>> our_string = 'Hello World!'
>>> our_string[-5:-2]
'orl'
```

如果不指定start位置，預設為0
如果不指定end位置，預設為字串的最後一個位置
如果不指定step數字，預設為1

```python
>>> our_string[1:]
'ello World!'
>>> our_string[:-1]
'Hello World'
```
:::info
[::-1]會**反轉**字串，這很常用要記住!!!
:::

### Exercise
1. what's the ouput of `"Hello world!"[:6:2]`? 
3. what's the ouput of `"Hello world!"[-5::-1]`? 
4. what's the ouput of `"Hello world!"[3:8:2]`? 

## index
我們已經知道字串裡面每個字都有它代表的位置
所以我們可以直接找出某個特定位置的字
```python
>>> our_string = 'Hello'
>>> our_string[0]
'H'
>>> our_string[1]
'e'
>>> our_string[2]
'l'
>>> our_string[3]
'l'
>>> our_string[4]
'o'
```

## String method
更多的字串操作...
```python
>>> our_string = 'Hello World!'
>>> our_string.upper() # 轉大寫
'HELLO WORLD!'
>>> our_string.lower() # 轉小寫
'hello world!'
>>> our_string.startswith('Hello') # 判斷字串是否以特定字串開始
True
>>> our_string.endswith('World!')  # 判斷字串是否以特定字串開始
True
>>> our_string.endswith('world!')  # Python is case-sensitive
False
>>> our_string.replace('World', 'there') 
'Hello there!'
>>> our_string.replace('o', '@', 1)   # only replace one o
'Hell@ World!'
>>> '  hello 123  '.lstrip()    # left strip
'hello 123  '
>>> '  hello 123  '.rstrip()    # right strip
'  hello 123'
>>> '  hello 123  '.strip()     # strip from both sides
'hello 123'
>>> '  hello abc'.rstrip('cb')  # strip c's and b's from right
'  hello a'
>>> our_string.ljust(30, '-')
'Hello World!------------------'
>>> our_string.rjust(30, '-')
'------------------Hello World!'
>>> our_string.center(30, '-')
'---------Hello World!---------'
>>> our_string.count('o')   # it contains two o's
2
>>> our_string.index('o')   # the first o is our_string[4]
4
>>> our_string.rindex('o')  # the last o is our_string[7]
7
>>> '-'.join(['hello', 'world', 'test'])
'hello-world-test'
>>> 'hello-world-test'.split('-')
['hello', 'world', 'test']
>>> our_string.upper()[3:].startswith('LO WOR')  # combining multiple things
True
>>>
```

### `.format()`

```python
>>> name = 'John'
>>> "Hello {}.".format(name)
"Hello John."
```

### `%s` formating
```python
>>> name = 'John'
>>> "Hello %s." % name
'Hello John.'
>>> "Hello %s, %s, %s." % (name,name,name) # 如果要替換多個string，須加括號
```

### f-string
```python
>>> name = 'John'
>>> f'Hello {name}'
'Hello John'
```

### `in` and `not in` 

我們可以用`in`跟`not in`來判斷一個字串是否存在於另一個字串中
```python
>>> our_string = "Hello World!"
>>> "Hello" in our_string
True
>>> "Python" in our_string
False
>>> "Python" not in our_string
True
```

### `len()`
我們可以利用`len()`這個function來檢查一個字串的長度

```python
>>> our_string = "Hello World!"
>>> len(our_string)   # 12 characters
12
>>> len('')     # no characters
0
>>> len('\n')    # python thinks of \n as one character
1
```

### str()、int()、float()
我們可以在`str`,`int`,`float`之間進行轉換
```python
>>> str(3.14)
'3.14'
>>> float('3.14')
3.14
>>> str(123)
'123'
>>> int('123')
123
```

:::warning
請注意:文字字串無法轉成int或float，例如: int('hello') 會報錯
:::

### exercise
1. 寫一段程式測試一段字串是否為palindrome(回文)，意思是反轉的字串與原字串相同，例如: restser
2. 將'Hello World!'字串中的`'l'`換為`'s'`
3. 將'Hi I am John'根據`' '`空格分割成四個字串
4. 將'testing'轉成大寫