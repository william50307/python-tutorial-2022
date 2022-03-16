###### tags: `tutorials`

# loops

迴圈的用途在於我們想要重複執行某件事
python裡面有for與while迴圈，它們的功能類似，也可以互相替代

## while loops

```python
its_raining = True
while its_raining:
    print("Oh crap, it's raining!")
    # print執行完畢後會跳到While判斷式，之後條件符合就再執行prnit
print("It's not raining anymore.")
```
上例是一個無窮迴圈，因為`its_raining`永遠為`True`

```python
>>> its_raining = True
>>> while its_raining:
...     its_raining = False
...     print("It's not raining, but the while loop doesn't know it yet.")
...
It's not raining, but the while loop doesn't know it yet.
>>>
```
迴圈裡的block執行完才會再檢查條件式(`its_raining`)，因此上例會執行print()


我們可以用關鍵字`break`來強制跳出迴圈
```python
while True:
    answer = input("Is it raining? (y=yes, n=no) ")
    if answer == 'y':
        print("It's raining!")
    elif answer == 'n':
        print("It's not raining anymore.")
        break   # end the loop
    else:
        print("Enter y or n.")
```

## for loops

假設我們有個lists，我們要把所有內容印出來，利用while迴圈我們可以寫成:

```python
stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
length_of_stuff = len(stuff)
index = 0
while index < length_of_stuff:
    print(stuff[index])
    index += 1
```

這時候我們可以用for，會讓事情變得更簡單!
```python
stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
for thing in stuff:
    print(thing)

```

`for`不只可以用在list上...
```python
>>> for c in 'abc':
...     print(c)
...
a
b
c
>>> for item in (1,2,3):
...     prnit(item)
...
1
2
3
```
### `range()`
`range()`可以創造一個可遞迴的物件
語法為`range(start,end,step)`，概念跟slicing一樣
```python
for i in range(1,5):
    print(i)
```
output:
```
1
2
3
4
```

## examples
無限重複某件事
```
message = input("What do you want me to say? ")
while True:
    print(message, "!!!")
```

讓使用者輸入5個字串然後全部印出來
```python 
things = []

print("Enter 5 things: ")
while len(things) < 5:
    thing = input("> ")
    things.append(thing)

print("You entered these things:")
for thing in things:
    print(thing)
```

問使用者一連串的問題
```python
questions_and_answers = [
    # [question, answer], ...
    ["What is 2+4? ", "6"],
    ["What is 2-4? ", "-2"],
    ["What is 2*4? ", "8"],
    ["What is 2/4? ", "0.5"],
]

for qa in questions_and_answers:
    while True:
        if input(qa[0]) == qa[1]:
            print("Correct!")
            break
        else:
            print("That's not what I was thinking of... Try again.")
```

## Exercises

1. 這段程式應該要印出`[1, 2, 3, 4, 5, 6]`，請修正所有bugs，請注意不要改動到`before` list
```python
before = [[1, 2], [3, 4], [5, 6]]
after = []
for number in before:
    after.append(number)
print(after)
```

2. 這段程式要將lists中所有項目轉換成整數`int()`，然後計算他們的總和(1+2+3)
```python
input = ['1', '2', '3']

# 請完成程式
...
```

3. 請寫一段程式印出底下的ouput `tips:如果不希望print自動換行，可以加入一個參數print(value, end='')`
```python
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
```

4. 請寫一段程式印出底下的ouput，讓使用者可以輸入想要印出幾個row
```python
1 2 3 4 5 
2 3 4 5 
3 4 5 
4 5 
5 
```
5. Count the total number of digits in a number，例如`56789`總共有**五位數**


## enumerator and zip
 
### unpack
```python
>>> items = [('a', 1), ('b', 2), ('c', 3)]
>>> for pair in items:
...     a, b = pair # 這個動作稱為unpacking
...     print(a, b)
...
a 1
b 2
c 3
```

### enumerator

`enumerator()`會回傳一個tuple，內容包含(value的index, value)，
```python
items = [1, 2, 3, 4, 5]
for index, value in enumerate(items):
    print('位置 :' , index, '值 :', value)
```
output:
```python
位置 : 0 值 : 1
位置 : 1 值 : 2
位置 : 2 值 : 3
位置 : 3 值 : 4
位置 : 4 值 : 5
```

### Exercise

1. Create a program that prints all letters from A to Z and a to z next to each other:
```
A a
B b
C c
...
X x
Y y
Z z
```
請從這兩行開始...
```
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
```



### 進階題...

1. 印出2~100中所有的質數

2. 印出費式數列中第10項

3. 反轉一個整數，例如:輸入3584，輸出485