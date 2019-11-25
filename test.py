#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##Python是一种相当高级的语言

##网络应用，包括网站、后台服务等等
#缺点就是运行速度慢，和C程序相比非常慢，因为Python是解释型语言
#跨平台的
#官方版本的解释器：CPython


name = input('please enter your name: ')

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


def quadratic(a,b,c):
	 n1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
	 n2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
	 return n1,n2

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



import functools

import time

# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
def metric(fn):
    @functools.wraps(fn)
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