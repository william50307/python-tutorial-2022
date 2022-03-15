###### tags: `tutorials`
# if else and elif

## Using if statements

使用if statements的意義在於進行 ```如果...就...```的運算


```python
>>> its_raining = True
>>> if its_raining:
...     print("It's raining!")
...
It's raining!
>>> its_raining = False
>>> if its_raining:
...     print("It's raining!")        # nothing happens
...
>>>
```

## Using else

當if的判斷式不成立，則會執行else底下的statements

```python
its_raining = False
if its_raining:
    print("It's raining!")
else:
    print("It's not raining.")
```
```
It's not raining
```

寫個小程式，讓user輸入密碼，然後檢查密碼是否正確

```python
print("Hello!")
password = input("Enter your password: ")

if password == "secret":
    print("That's correct, welcome!")
else:
    print("Access denied.")
```

```
Hello!
Enter your password: secret
Welcome!
```

```
Hello!
Enter your password: lol
Access denied.
```


## elif 

如果我們有很多種條件要檢查，我們可能會寫成這樣

```python
print("Hello!")
word = input("Enter something: ")

if word == "hi":
    print("Hi to you too!")
else:
    if word == "hello":
        print("Hello hello!")
    else:
        if word == "howdy":
            print("Howdyyyy!")
        else:
            if word == "hey":
                print("Hey hey hey!")
            else:
                if word == "gday m8":
                    print("Gday 4 u 2!")
                else:
                    print("I don't know what", word, "means.")
```

看起來有點亂，這個問題可以用```elif```很好的解決
```elif```其實就是```else if```的縮寫

```python
print("Hello!")
word = input("Enter something: ")  # input function會讓使用者輸入一段字串，然後存到word這個變數中

if word == "hi":
    print("Hi to you too!")
elif word == "hello":
    print("Hello hello!")
elif word == "howdy":
    print("Howdyyyy!")
elif word == "hey":
    print("Hey hey hey!")
elif word == "gday m8":
    print("Gday 4 u 2!")
else:
    print("I don't know what", word, "means.")
```
一些觀念的釐清...

這段程式會印出 hello
```python
if 1 == 1:
    print("hello")
elif 1 == 2:
    print("this is weird")
else:
    print("world")
```

這段程式則會印出hello 和 world

```python
if 1 == 1:
    print("hello")
if 1 == 2:
    print("this is weird")
else:
    print("world")
```


## Exercises

1. copy底下的code然後修正所有的bugs

```python
print(Hello!)
something == input('Enter something: )
print('You entered:' something)
```

2. Fix this program the same way:

```python
print('Hello!')
something = input("Enter something: ")
if something = 'hello':
    print("Hello for you too!")

elif something = 'hi'
    print('Hi there!')
else:
    print("I don't know what," something, "means.")
```

3. 讓使用者輸入一段字串，接著重印出100次該字串，例如使用者輸入```hi```，則印出```hihihihihihihi...```共100次
4. 承上題加一個空格在字與字的中間，例如```hi hi hi hi hi```
