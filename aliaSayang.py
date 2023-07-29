import turtle
import math
import random
import time

wn = turtle.Screen()
wn.bgcolor('OrangeRed')

aku = turtle.Turtle()
aku.hideturtle()
aku.speed(0)
aku.color('white')

rotate = int(360)

def drawCircles(t, size):
    for i in range(10):
        t.circle(size)
        size = size - 4

def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)

drawSpecial(aku, 100, 50)

kamu = turtle.Turtle()
kamu.hideturtle()
kamu.speed(0)
kamu.color('OrangeRed')

rotate = int(90)

def drawCircles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 10

def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)

drawSpecial(kamu, 100, 20)

kita = turtle.Turtle()
kita.hideturtle()
kita.speed(0)
kita.color('gold')

rotate = int(80)

def drawCircles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 5

def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)

drawSpecial(kita, 100, 20)

akan_terus = turtle.Turtle()
akan_terus.hideturtle()
akan_terus.speed(0)
akan_terus.color('Pink')

rotate = int(90)

def drawCircles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 19

def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)

drawSpecial(akan_terus, 100, 20)

sayang_selamanya = turtle.Turtle()
sayang_selamanya.hideturtle()
sayang_selamanya.speed(0)
sayang_selamanya.color('OrangeRed')

rotate = int(90)

def drawCircles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 20

def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)

drawSpecial(sayang_selamanya, 100, 20)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.goto(-190, 180)
t.pendown()
t.color("White")

sentence = "alia sayang.."
font_size = 12
font_family = "Arial"
delay = 0.5

for i in range(1, len(sentence) + 1):
    t.write(sentence[:i], font=(font_family, font_size, "normal"))
    time.sleep(delay)

turtle.done()