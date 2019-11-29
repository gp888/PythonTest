#!/usr/bin/env python3   
# -*- coding: utf-8 -*-

#第一行是告诉Linux/OS X，windows会忽略
#第二行(UTF-8 without BOM)

##Python是一种相当高级的语言

##网络应用，包括网站、后台服务等等
#缺点就是运行速度慢，和C程序相比非常慢，因为Python是解释型语言
#跨平台的
#官方版本的解释器：CPython

4个空格缩进

CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令

age = input('please enter your name: ')
age 是 str
int(age) 转换 int

# 转义\" \' \n \t \\
#用r''表示''内部的字符串默认不转义
#多行内容 '''...'''

'''line1
line2
line3'''

r'''hello,\n
world'''

True、False

and、or和not

变量大小写英文、数字和_的组合，且不能用数字开头

空值 None

任何数据都是对象

变量本身类型不固定的语言称之为动态语言

用全部大写的变量名表示常量

/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数

//，称为地板除，两个整数的除法仍然是整数，只取结果的整数部分

整数的地板除//永远是整数，即使除不尽。要做精确的除法，使用/就可以

Python的整数没有大小限制
浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）

x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向

##字符编码

GB2312两个字节表示一个汉字

Unicode用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）

ASCII编码是1个字节，而Unicode编码通常是2个字节

如果写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间

“可变长编码”UTF-8编码

UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，
常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。
如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间

ASCII编码实际上可以被看成是UTF-8编码的一部分

计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码


Python3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
ord('A') ord('中')

还可以用十六进制这么写str '\u4e2d\u6587' == '中文'


字符串类型是str，在内存中以Unicode表示
一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes

bytes类型的数据用带b前缀的单引号或双引号表示 x = b'ABC'

注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

str通过encode()方法可以编码为指定的bytes

 'ABC'.encode('ascii') == b'ABC'

 '中文'.encode('utf-8') == b'\xe4\xb8\xad\xe6\x96\x87'

 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes

从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()

b'ABC'.decode('ascii') == 'ABC'

b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') == '中文'

b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore') == '中'#忽略错误的字节

len('ABC')#字符数

len(b'ABC')#字节数 len('中文'.encode('utf-8'))

格式化方式和C语言是一致的，用%实现 'Hi, %s, you have $%d.' % ('Michael', 1000000)
%x  十六进制整数，%f    浮点数
print('%2d-%02d' % (3, 1))
%s永远起作用
转义%%来表示一个%
'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)


##list

list是一种可变有序的集合s = []
len(s)，s[2],获取最后一个s[-1],倒数第二s[-2]
s.append('Adam')末尾追加
s.insert(1, 'Jack')插入
s.pop()删除末尾
s.pop(i)删除指定位置
s[1] = 'Sarah'替换元素
list里面的元素的数据类型可以不同，元素可以是另一个list(二维)
s = ['python', 'java', ['asp', 'php'], 'scheme']
L = []
len(L) == 0

s.sort()排序

##tuple
元组：tuple。list非常类似，但是tuple一旦初始化就不能修改
t = ('Michael', 'Bob', 'Tracy')
定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = ()空tuple
t = (1,)一个元素

可变tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
t
('a', 'b', ['X', 'Y'])

指向不变
tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，
指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
二维数组最后一个L[-1][-1]

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('your age is', age)

if x:
    print('True')
x是非零数值、非空字符串、非空list等，就判断为True，否则为False

##循环

一种是for...in循环，依次把list或tuple中的每个元素迭代出来
for name in names:
    print(name)

range(5)生成的序列是从0开始小于5的整数
通过list()函数可以转换为list
list(range(5)) == [0, 1, 2, 3, 4]

另一种：while n > 0:


##dict & set

dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
 d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
 d['Michael']

 在list中查找元素的方法，list越大，查找越慢
 dict查找速度都非常快，不会随着字典大小的增加而变慢
 缺点：需要占用大量的内存，内存浪费多。dict是用空间来换取时间的一种方法

d['Adam'] = 67放入

 'Thomas' in d 判断key是否存在

 d.get('Thomas') key存在返回None
 d.get('Thomas', -1)
d.pop('Bob')删除键值对


dict的key必须是不可变对象

通过key计算位置的算法称为哈希算法（Hash）

set和dict类似，也是一组key的集合，但不存储value。在set中，无重复的key。无序

要创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
add(key)添加
remove(key)删除
&|并集交集操作

同样不可以放入可变对象

str,None是不变对象，而list是可变对象
a = 'abc'
a.replace('a', 'A')
'Abc'
a
'abc'

对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回

最常用的key是字符串


##函数
python 内置函数
https://docs.python.org/3/library/functions.html

help(abs)查看abs函数的帮助信息
abs(-100)
max()可以接收任意多个参数，并返回最大的那个

float('12.34') str(1.23) bool('')

a = abs #别名
a(-1) # 所以也可以通过a调用abs函数

hex()函数把一个整数转换成十六进制表示的字符串

定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return

from abstest import my_abs来导入my_abs()

空函数
def nop():
    pass

if age >= 18:
    pass    


import math

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x > 0:
		return x
	else:
		return -x	

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny

返回值是一个tuple()
返回多值其实就是返回一个tuple，而多个参数可以同时接收一个tuple



def quadratic(a,b,c):
    i=b**2-4*a*c
    if i>0:
        x1=(-b+math.sqrt(i))/(2*a)
        x2=(-b-math.sqrt(i))/(2*a)
        print('方程有两个不同的解:' , x1,x2)
        # return x1,x2     
    elif i==0:
        x1=-b/2*a
        print('方程有两个相同的解:', x1,x1)        
    else:
        print('方程无解')


位置参数
必选参数在前，默认参数在后

默认参数必须指向不变对象

可变参，任意多个参数包括0个
参数前面加了一个*号
nums = [1, 2, 3]
calc(*nums)
*nums表示把nums这个list的所有元素作为可变参数传进去
可变参数在函数调用时自动组装为一个tuple

**kw
关键字参数允许你传入0个或任意个含参数名的参数
这些关键字参数在函数内部自动组装为一个dict
person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数
kw获得的dict是extra的一份拷贝

命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)

命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数    


如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


命名关键字参数可以有缺省值，从而简化调用：

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer')


参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的


总结：
*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。


可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。


命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数

def product(*args):

    if args:

        acl = 1

        for i in args:

            acl *= i

        return acl

    else:

        raise TypeError('none types')



##递归

阶乘
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


函数调用是通过栈这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，
栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出   

尾递归是指，在函数返回的时候，调用自身本身
尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的 

尾递归调用时，如果做了优化，栈不会增长


汉诺塔的移动可以用递归函数非常简单地实现

move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法

def hanoi(n, a, b, c):
    # 当n为1时 (递归基础)
    if n == 1:
        print(a, '-->', c) # 将A柱最底层的圆盘移动到C柱
    # 当n大于1时
    else:
        hanoi(n-1, a, c, b) # 借助C柱，将n-1个圆盘从A柱移动到B柱
        print(a, '-->', c) # 将A柱最底层的圆盘移动到C柱
        hanoi(n-1, b, a, c) # 借助A柱，将n-1个圆盘从B柱移动到C柱
        

##Slice

取一个list或tuple的部分元素
L[0:3]取 0，1，2

如果第一个索引是0
L[:3]前三个

L[-2:]后两个

前10个数，每两个取一个：
L[:10:2]

所有数，每5个取一个：
L[::5]

'ABCDEFG'[:3]

str.strip() 去首尾空格

#循环去str首尾空格
while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


##迭代

for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
迭代value ,entity
for value in d.values()    
for k, v in d.items()

from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代

同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

#迭代最大值最小值
def min_max(d):
    min1 = d[0]
    max1 = d[0]
    for i in d:
        if i <= min1:
            min1 = i
        if i >= max1:
            max1 = i
    return (min1, max1)


##列表生成式
[x * x for x in range(1, 11)]
[x * x for x in range(1, 11) if x % 2 == 0]
[m + n for m in 'ABC' for n in 'XYZ']

 import os 
 [d for d in os.listdir('.')] # os.listdir可以列出文件和目录


[k + '=' + v for k, v in d.items()]


L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str) == True]


##生成器

第一种方法很简单，把一个列表生成式的[]改成()
g = (x * x for x in range(10))
next(g)获得generator的下一个返回值

迭代generator
for n in g:
	print(n)

赋值
a, b = b, a + b

#斐波那契 generator
第二种：一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
再次执行时从上次返回的yield语句处继续执行

迭代generator 函数
for n in fib(6):
	print(n)

#杨辉三角
def triangles():
    L = [1]
    while 1:
        yield L
        L = [0] + L + [0]
        L = [L[i] + L[i + 1] for i in range(len(L) - 1)]


##迭代器

可以直接作用于for循环的数据类型：
一类是集合数据类型，如list、tuple、dict、set、str
一类是generator，包括生成器和带yield的generator function

统称可迭代对象：Iterable

from collections import Iterable
是否是可迭代对象
isinstance((x for x in range(10)), Iterable)


生成器不但可以作用于for循环，还可以被next()函数不断调用
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

from collections import Iterator

生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator

变成Iterator：iter('abc')

Iterator对象表示的是一个数据流。可以把这个数据流看做是一个有序序列，
但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据
Iterator表示一个惰性计算的序列

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

Python的for循环本质上就是通过不断调用next()函数实现的

it = iter([1, 2, 3, 4, 5])
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

##高阶函数map()和reduce()

map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
并把结果作为新的Iterator返回

Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list

list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
['1', '2', '3', '4', '5', '6', '7', '8', '9']

reduce接收两个参数，把一个函数(这个函数必须接收两个参数)作用在一个序列[x1, x2, x3, ...]上，
结果继续和序列的下一个元素做累积计算

from functools import reduce

求和函数sum()可以接受一个list并求和


#str转换为int的函数 功能和int()一样
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

str.capitalize('uRRH') 首字母大写
'SJIISOA'.lower()/.upper()
name[0].upper() + name[1:].lower()#首字母大写


str[::-1] 反向str
#str to float
return reduce(lambda x,y:x*10+y,map(int,s.split(".")[0])) 
+(reduce(lambda x,y:x/10+y,map(int,s.split(".")[1][::-1])))/10



filter()也接收一个函数和一个序列。filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素


filter()函数返回的是一个Iterator，也就是一个惰性序列。需要用lst()获得所有结果并返回list

计算素数的一个方法是埃氏筛法
从3开始的奇数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

Iterator是惰性计算的序列
可以用Python表示“全体自然数”，“全体素数”这样的序列

筛选回数
def is_palindrome(n): 
    sn = str(n)
    return sn[::] == sn[::-1]

output = filter(is_palindrome,range(1,1000))


##排序

sorted()函数就可以对list进行排序

sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
sorted([36, 5, -12, 9, -21], key=abs)
key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序


默认情况下，对字符串排序，是按照ASCII的大小比较的，
由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面

忽略大小写排序str
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

忽略大小写，反向排序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

成绩和名称排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L,key=lambda L0 : L0[0])
成绩从高到低
L2 = sorted(L,key=lambda L1 : -L1[1])



##函数作为返回值
我们在函数中又定义了函数，并且，内部函数可以引用外部函数的参数和局部变量，
当外部函数返回内部函数时，相关参数和变量都保存在返回的函数中
闭包（Closure）


返回函数不要引用任何循环变量，或者后续会发生变化的变量

如果一定要引用循环变量就再创建一个函数，用该函数的参数绑定循环变量当前的值


#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    def counter():
        n=0
        while True:
            n=n+1
            yield n
    x=counter()
    def fext():
        return next(x)
    return fext





##匿名函数
lambda x: x * x


## 装饰器

函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数

函数对象有一个__name__属性，可以拿到函数的名字


def now():
	print('2015-3-25')
f = now
f()


在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

decorator就是一个返回函数的高阶函数


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')


@log放到now()函数的定义处，相当于执行了语句：
now = log(now)

log()是一个decorator

调用now()将执行新函数，即在log()函数中返回的wrapper()函数

wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用







def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2019-11-25')

3层嵌套
now = log('execute')(now)




import functools

import time

# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def metric(fn):
    @functools.wraps(fn) #原始函数的__name__等属性复制到wrapper()函数中
    def wrapper(*args,**kw):
        print('%s executed in %s ms' % (fn.__name__, time.time()))
        return fn(*args,**kw)
    return wrapper    

@metric
def now1():
    print('2019-11-25')





#写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
def log2(test='call'):
    def metric(fn):
        @functools.wraps(fn)
        def wrapper(*args,**kw):
            # print('Begain %s %s()' % (test, fn.__name__))
            # fn(*args,**kw)
            # print('End %s %s()' % (test, fn.__name__))

            # return fn(*args, **kw)

            print('Begain %s %s()' % (test,fn.__name__))
            back = fn(*args,**kw)
            print('End %s %s()' % (test, fn.__name__))

            # # return back

        return wrapper
    return metric

#测试log2
@log2('execute')
def now2():
    print('2019-11-25')


Python除了能支持OOP的decorator外，
直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现



##偏函数
import functools

int('12345')#base=10
int('12345', base=8)
int('12345', 16)

#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
int2 = functools.partial(int, base=2)
int2('10010')
相当于 
kw = { 'base': 2 }
int('10010', **kw)

创建偏函数时，可以接收函数对象、*args和**kw这3个参数


max2 = functools.partial(max, 10)
max2(5, 6, 7)
相当于
args = (10, 5, 6, 7)
max(*args)


当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数



##模块

import sys

' a test module '
任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'gp'

变量sys指向sys模块
args = sys.argv #[main.py]
sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，
因为第一个参数永远是该.py文件的名称

运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael] 



if __name__=='__main__':
    test()
在命令行运行模块文件时，Python解释器把一个特殊变量__name__置为__main__，
而如果在其他地方导入该hello模块时，if判断将失败，因此，
这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

__name__
当模块是被调用执行的，取值为模块的名字；当模块是直接执行的，则该变量取值为：__main__


##一个模块
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()



import hello
运行：hello.test()


正常的函数和变量名是公开的（public），可以被直接引用

__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，
比如__author__，__name__
模块定义的文档注释也可以用特殊变量__doc__访问
_xxx和__xxx这样的函数或变量就是非公开的（private）

Python并没有一种方法可以完全限制访问private函数或变量

外部不需要引用的函数全部定义成private



安装第三方模块，是通过包管理工具pip完成的

安装时勾选了pip和Add python.exe to Path



第三方库都会在Python官方的pypi.python.org网站注册

Python Imaging Library(PIL)非常强大的处理图像的工具库
基于PIL的Pillow支持python3
pip install Pillow

MySQL驱动程序，Web框架Flask,科学计算Numpy

Anaconda，是一个基于Python的数据处理和科学计算平台
内置了许多非常有用的第三方库

模块搜索路径

加载一个模块时，Python会在指定的路径下搜索对应的.py文件
sys.path
添加搜索目录，运行时修改
sys.path.append('/Users/michael/my_py_scripts')




## 类

class Student(object):#object)，表示该类是从哪个类继承下来的

	def __init__(self, name, score):#特殊方法，第一个参数永远是实例变量self
        self.__name = name
        self.__score = score

    def print_score(self):#第一个参数是self
        print('%s: %s' % (self.__name, self.__score)) 
        
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')



bart = Student()
bart.name = 'Bart Simpson'


__init__方法的第一个参数永远是self，表示创建的实例本身

#绑定任何数据
bart = Student('Bart Simpson', 59)
bart.age = 8




实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问
Python解释器对外把__name变量改成了_Student__name，通过_Student__name来访问__name变量


__xxx__，是特殊变量，特殊变量是可以直接访问的
比如_name,请把我视为私有变量，不要随便访问

多态 开闭原则，对扩招开放，对修改关闭

Animal - run() Dog - run() Cat - run()

参数为Animal的函数，Python这样的动态语言来说，
不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了


一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子

file-like object
真正的文件对象，它有一个read()方法，返回其内容
python 中只要有read()方法，都被视为“file-like object“


对象类型：type(对象)
type(None) <class 'NoneType'>
type(abs)


import types
type(fn)==types.FunctionType
type(abs)==types.BuiltinFunctionType
type(lambda x: x)==types.LambdaType
type((x for x in range(10)))==types.GeneratorType
能用type()判断的基本类型也可以用isinstance()判断
isinstance(b'a', bytes)

是否是某些类型中的一种
isinstance([1, 2, 3], (list, tuple))
优先使用isinstance()判断类型


获得一个对象的所有属性和方法，可以使用dir()函数
返回一个包含字符串的list

dir('ABC')


调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
它自动去调用该对象的__len__()方法

len('ABC') == 'ABC'.__len__()



getattr()、setattr()以及hasattr()

setattr(obj, 'y', 19) # 设置一个属性'y'
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
hasattr(obj, 'power') # 有方法'power'吗？



Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，
它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能



class Student(object):
    name = 'Student'
这个属性虽然归类所有，但类的所有实例都可以访问到


实例属性优先级比类属性高 
del s.name # 删除实例的name属性
不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性


from types import MethodType

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

s.set_age = MethodType(set_age, s) # 给实例绑定一个方法

Student.set_score = set_score#给class 绑定一个方法

__slots__

只允许对Student实例添加name和age属性
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的    


not isinstance(value, int)
 if value < 0 or value > 100:

@property装饰器  把一个方法变成属性调用

把一个getter方法变成属性
另一个装饰器@score.setter

只定义getter方法，不定义setter方法就是一个只读属性

##多继承 MixIn

多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系
不需要复杂而庞大的继承链，只要选择组合不同的类的功能