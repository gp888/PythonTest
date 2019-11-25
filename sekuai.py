from turtle import *
from random import *
Screen().bgcolor("yellow")
colormode(255)#设置颜色模式
speed(0)
#画方块函数drawRect参数依次为 坐标x、坐标y、边长、颜色、旋转角度
def drawRect(x,y,l,col,angle):
    penup()
    goto(x,y)
    fillcolor(col)
    begin_fill()
    right(angle)
    circle(l,360,4)
    end_fill()
    left(angle)
    pendown()
for i in range(36):
    #下面三行设置RGB颜色
    r=0
    g=randint(160,255)
    b=randint(160,255)
    color1=(r,g,b)
    drawRect(0,0,120,color1,i*10)
for i in range(36):
    r=0
    g=randint(160,255)
    b=randint(160,255)
    color1=(r,g,b)
    drawRect(0,0,120-i*3,color1,i*10)