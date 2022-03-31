###### tags: `tutorials`

# Classes 

大家應該有聽過物件導向程式設計(Object-oriented programming)，他是一種開發方式，能夠提高軟體的重用性、擴充性及維護性，在開發大型的應用程式時更是被廣為使用，所以在現今多數的程式語言都有此種開發方式，python當然也不例外。

## Fist class

再python中我們可以利用`type()`來查看他是什麼**類別(Class)**
 
```python
>>> type('')
<class 'str'>
>>> type(0)
<class 'int'>
>>> type([])
<class 'list'>
>>> type({})
<class 'dict'>
>>>
```

每個**物件(Object)** 都會有他的 **屬性(Attribute)** 以及 **方法(Method)**

例如python裡的list就是一種class，我們可以用append()這個方法來操作list `[1,2,3].append(4)`

### 類別之概念

![](https://i.imgur.com/bKp61KE.png)
friut是所有水果的總稱，因此水果就是一個class，而水果又分成
蘋果、橘子等等...，因此我們要詳細的描述他是哪一種水果(給予**屬性**)，

### 建立類別(class)

```python
# 水果類別
class Fruit:
    # 建構式
    def __init__(self, name, color):
        self.name = name  # 顏色屬性
        self.color = color  # 座位屬性
    # 方法(Method)
    def describe(self):
        print(f"{self.name} is {self.color}.")
```

### 實體(instance)、物件(Object)
我們定義出 class 類別後，就會需要把 class 類別實體化，也就是一顆一顆的蘋果以及橘子的概念，這些蘋果跟橘子就稱做instance或object
```python
>>> fruit = Fruit('Apple', 'red')
```

### 屬性(attribute)

可以想像成是物件的特徵
```python
>>> fruit.name
Apple
>>> fruit.color
red
```

### 方法(method)

這個物件能做出的行為

```python
>>> fruit.describe() #跟呼叫函數的寫法類似
Apple is red.  
```

### 建構式(constructor)

每當我們建立一個物件時會自動執行的method

```python
# 建構式
    def __init__(self, name, color):
        self.name = name  # 顏色屬性
        self.color = color  # 座位屬性
```

### self

代表實體物件對於**自己**的參考


## 程序式設計 v.s 物件導向設計

### 程序式設計 (Procedural design)

```python
def main():
    # 建立球的資料
    numBalls = 30
    xs = []    # 位置 x 座標
    ys = []    # 位置 y 座標
    rs = []    # 半徑
    cs = []    # 顏色
    ms = []    # 質量
    es = []    # 彈性係數
    ...       # 其他特性

    for i in range(numBalls):   
        xs.append(...)
        ys.append(...)
        rs.append(...)
        cs.append(...)
        ms.append(...)
        es.append(...)
        ...

    # 處理碰撞
    for i in range(numBalls-1):
        for j in range(i+1, numBalls):
            collision(xs[i], ys[i], xs[j], ys[j], rs[i], rs[j], ms[i], ms[j], es[i], es[j] ...)


def collision(x1, y1, x2, y2, r1, r2, m1, m2, e1, e2...):
    ...
```

###  物件導向設計 (Object-oriented design)

```python
# 球類別
class Ball:
   def __init__(self, x, y, r, c, m, e, ...):
       self.x = x
       self.y = y
       self.r = r
       self.c = c
       self.m = m
       self.e = e
       ...


def main():
    # 建立球的資料
    numBalls = 30
    balls = []
    for i in range(numBalls):   
        balls.append(Ball(...))

    # 處理碰撞
    for i in range(numBalls-1):
        for j in range(i+1, numBalls):
            collision(balls[i], balls[j])


def collision(b1, b2):
    ...
```


### 範例

我們想要定義一個時鐘物件

```python
from time import sleep

class Clock(object):

    def __init__ (self, hour = 0, minute = 0, second = 0): # 初始化
        self._hour = hour           # 時
        self._minute = minute       # 分
        self._second = second       # 秒

    def run(self):
        self._second += 1            # 秒數 + 1
        if self._second == 60:       # 當秒數為 60, 分數 + 1, 秒數變回 0
            self._second = 0
            self._minute += 1
            if self._minute == 60:   # 當分數為 60, 時數 + 1, 分數變回 0
                self._minute = 0
                self._hour += 1
                if self._hour == 24: # 當時數為 24, 時數變為 0
                    self._hour = 0

    def show(self):        # 顯示時間
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

```

運作這個時鐘

```python
clock = Clock(23, 59, 58)
while True:
    print(clock.show())
    # sleep()函數推遲程式運行，單位為 secs 秒數
    sleep(1)        # 推遲進行 1 秒
    clock.run()
```


### 練習題

定義一個class描述平面上的點，並提供兩種method

1. 更改這個點的座標
2. 計算這個點與另外一點的距離

hint : 使用開根號的function `from math import sqrt`

start from here:
```python
class Point():
    def __init__ (self, x = 0, y = 0): # 初始化
        ...
        
    def change (self, x, y): #更改座標
        ...
        
    def distance(self, other): #計算兩點的距離 other是另一個Point物件
        ...
        
```

<!-- from math import sqrt

class Point(object):

    def __init__ (self, x = 0, y = 0): # 初始化 
        self.x = x                # x 座標
        self.y = y                # y 座標

    def move_to (self, x, y):  # 移動到指定位置
        self.x = x            # x 座標
        self.y = y            # y 座標

    def move_by (self, dx, dy):  # 移動指定的增量
        self.x += dx            # x 座標的增量
        self.y += dy            # y 座標的增量

    def distance_to (self, other): # 計算兩點的距離 other：另一個點
        dx = self.x - other.x   
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))

def main():
    p1 = Point(3, 5)
    p2 = Point()      # (0, 0)
    print(p1)
    print(p2)
    p1.move_to(-1, 2)
    p2.move_by(3, 5)
    print(p1)
    print(p2)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main() -->