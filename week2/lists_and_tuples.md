###### tags: `tutorials`

# lists and tuples
## why we need that?

有時候我們想要做像這樣的事情...
```python
name1 = 'wub_wub'
name2 = 'theelous3'
name3 = 'RubyPinch'
name4 = 'go|dfish'
name5 = 'Nitori'

name = input("Enter your name: ")
if name == name1 or name == name2 or name == name3 or name == name4 or name == name5:
    print("I know you!")
else:
    print("Sorry, I don't know who you are :(")
```

如果能夠把五個名字都存到一個變數中，那事情應該比較容易
這時候我們可以使用list，就像下面這樣
`names = ['wub_wub', 'theelous3', 'Nitori', 'RubyPinch', 'go|dfish']`

上面的程式可以改成如下，我們用`[]`來代表lists
```python
names = ['wub_wub', 'theelous3', 'Nitori', 'RubyPinch', 'go|dfish']
name = input("Enter your name: ")

if name in names:
    print("I know you!")
else:
    print("Sorry, I don't know who you are :(")
```

### lists operations

回顧我們上一章的strings opearation，我們可以對lists做類似的事

```python
>>> names = ['wub_wub', 'theelous3', 'RubyPinch', 'go|dfish', 'Nitori']
>>> len(names)   # len 是 length的縮\寫, 這個list中有五個名字
5
>>> names + ['Akuli']  
['wub_wub', 'theelous3', 'RubyPinch', 'go|dfish', 'Nitori', 'Akuli']
>>> ['theelous3', 'RubyPinch'] * 2    # repeating
['theelous3', 'RubyPinch', 'theelous3', 'RubyPinch']
>>>
```

### slicing
就跟strings的操作一樣
```python
>>> names[:2]    # 前兩個名字
['wub_wub', 'theelous3']
>>> names[0]     # 第一個名字
'wub_wub'
>>>
```

### in and not in 

check 某個值是否存在lists中，非常直觀!!!
```python
>>> 'lol' in names
False
>>> 'RubyPinch' in names
True
>>>
```

### some useful methods

```python
>>> names
['wub_wub', 'theelous3', 'RubyPinch', 'go|dfish', 'Nitori']
>>> names.remove('theelous3')  # sorry theelous3
>>> names.remove('go|dfish')   # and sorry go|dfish
>>> names
['wub_wub', 'RubyPinch', 'Nitori']
>>> names.append('Akuli')    # let's add me here
>>> names
['wub_wub', 'RubyPinch', 'Nitori', 'Akuli']
>>> names.extend(['go|dfish', 'theelous3'])  # wb guys
>>> names
['wub_wub', 'RubyPinch', 'Nitori', 'Akuli', 'go|dfish', 'theelous3']
>>>
```

請注意`remove`只會移除第一個match到的值

```python
>>> names = ['theelous3', 'go|dfish', 'theelous3']
>>> names.remove('theelous3')
>>> names    # the second theelous3 is still there!
['go|dfish', 'theelous3']
>>>
```

```python
>>> a = [1, 2, 3]
>>> b = a
>>> b.append(4)
>>> a    # a所指向的值也被改動了
[1, 2, 3, 4]
```

這裡的情況跟之前的int、string不太一樣
如果把圖畫出來會長這樣...
![](https://i.imgur.com/pYVTpn8.png)

那如果我希望a跟b的list是**獨立**的，意思是a的改動不影響b
我們可以用下面的寫法...
```python
>>> a = [1, 2, 3]
>>> b = a.copy()
>>> b is a
False
>>> b.append(4)
>>> b
[1, 2, 3, 4]
>>> a
[1, 2, 3]
```
用圖形表示如下

![](https://i.imgur.com/mjTHJVX.png)

## Tuples

tuples其實跟lists很像，差別在於tuples是**immutable**(不可變的)，我們用`()`來代表tuples

```python
>>> thing = (1, 2, 3)
>>> thing
(1, 2, 3)
>>> thing = ()
>>> thing
()
>>>
```

如果我們只想建立只包含一個項目的tuple，我們需要寫成`(item,)`，因為`(item)`會被視為普通運算的括號
```python
>>> (3)
3
>>> (3,)
(3,)
>>> (1 + 2) * 3
9
>>> (1 + 2,) * 3
(3, 3, 3)
>>>
```
:::info
tuples沒有像是`append()`、`extend()`、`remove()`這些方法，因為他們是不可變的
:::

## summary

- lists能讓一個變數儲存多個值的資料結構
- lists中的值能夠更動，tuples則否
- slicing會回傳一個新的list，indexing會回傳一個值
- `thing = another_thing` 不會複製一份 `another_thing`

## Exercise
1. Fix this program:
```python
namelist = ('wub_wub', 'RubyPinch', 'go|dfish', 'Nitori')
namelist.append('pb122')
if 'pb122' in namelist:
    print("Now I know pb122!")    
```
2. Fix this program.
```python
namelist = ['wub_wub', 'RubyPinch', 'go|dfish', 'Nitori']
namelist = namelist.extend('theelous3')
if input("Enter your name: ") in namelist:
    print("I know you!")
else:
    print("I don't know you.")
```
3. 給定已排序數列`[1,12,14,21,23,36,43,48,56,78,89,102,126,147,168,171,199,222,256,348,729]`，試求中位數
5. 給定已排序數列
`[1,12,14,21,23,36,43,48,56,78,89,102,126,147,168,171,199,222,256,348]`，試求中位數