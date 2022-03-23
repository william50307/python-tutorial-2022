###### tags: `tutorials`

# Dictionaries

我們已經學過了lists and tuples，這邊我們要學一個新的資料結構---字典，字典不同於lists跟tuples，它由**鍵(key)** 和 **值(value)** 的pair所組成，我們必須為每一個值賦予一個**唯一的鍵**，並利用這個 **鍵(key)** 來取 **值(value)**。

## 基本的字典操作

字典建立方式 : 
```python
>>> ages = {'John' : 21, 'Tom':25, 'Amy' : 22}
```

以第一個pair為例，'John'是**key**，而21是**value**
我們可以透過key去取得value
```python
>>> ages['John']
21
```

計算字典有幾組 ```鍵(key):值(value)```
```python
>>> len(ages)     # contains three key:value pairs
3
```

如果我們使用了一個不存在的key會報錯
```python
>>> ages['tommy']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'tommy'
```

我們可以新增 ```鍵(key):值(value)``` 或修改原本的keys

```python
>>> ages['Jacky'] = 45
>>> ages['Jacky']
45
>>> ages['Jacky'] = 33
>>> ages['Jacky']
33
>>> ages
{'John': 21, 'Tom': 25, 'Amy': 22, 'Jacky': 33}
```

還記得`in`的操作嗎 我們可以用它來檢查某個key是否在dictionary中

```python
>>> 'John' in ages
True
```

如果用for loop在一個dictionary上，我們會得到該字典所有的keys

```python
>>> for key in ages:
...   print(key)
...
John
Tom
Amy
Jacky
```

如果想要找出所有的values，也可以用一些function達成...

```python
>>> ages.values()
dict_values([21, 25, 22, 33])

>>> for value in ages.values():
...   print(value)
21
25
22
33
```

我們也可以同時取出`key:value`pair

```python
>>> for key, value in ages.items():
...   print('{} is {} years old.'.format(key, value))
...
John is 21 years old.
Tom is 25 years old.
Amy is 22 years old.
Jacky is 33 years old.
```

字典的values可以是任何東西，例如:

```python
>>> stuff = {'a': [1, 2, 3], 'b': [4, 5, 6]}
>>> stuff
{'a': [1, 2, 3], 'b': [4, 5, 6]}
>>> stuff['a']
[1,2,3]
```


## Exercise
1. 請將下列的list:`[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]` 
整理成下列的dictionary`{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}`

2. 將下列的字典 : `{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}`
整理成下列的list : `
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]`

3. 寫一段程式，計算一個sentence中每個word出現的次數。 Hint:`sentence.split()`

output:
```
Enter a sentence: this is a test and this is quite long because this is a test

'is' appears 3 times in the sentence
'long' appears once in the sentence
'a' appears 2 times in the sentence
'because' appears once in the sentence
'this' appears 3 times in the sentence
'quite' appears once in the sentence
'and' appears once in the sentence
'test' appears 2 times in the sentence
```



# generator expression

假設我要做一個1~100的list該怎麼辦??


用generator expression來寫
![](https://i.imgur.com/bM2cyQJ.png)

![](https://i.imgur.com/kqiWYn1.png)


```python
>>> [i for i in range(1,101)]
[1,2,3,.......,98,99,100]
```

generator不只可以拿來創造list...
```python
>>> { i : i**2 for i in range(1,10)}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

### 加入condition

在generator中加入條件式
![](https://i.imgur.com/Wrdiw8u.png)


```python
>>> [i for i in range(1,101) if i % 2 == 0]
[2,4,6,......,96,98,100]
```

<br>
如果是if-esle則要放到前面

![](https://i.imgur.com/eQYf3R7.png)

```python
>>> [i if i%2==0 else -1 for i in range(1,101)]
[-1,2,-1,4,......,-1,98,-1,100]
```


### exercise
what's the output? `[[n**2 for n in range(10) if n%2==0],[n**3 for n in range(10)  if n%2!=0]]`