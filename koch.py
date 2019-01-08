from turtle import *
print('0から5の数字を入力して下さい｡')
N = int(input())
import turtle
def koch(turtle,length,N):
    if N == 0:
        turtle.forward(length)
    else :
        koch(turtle, length/3, N -1)
        turtle.left(60)
        koch(turtle, length / 3, N - 1)
        turtle.right(120)
        koch(turtle, length / 3, N - 1)
        turtle.left(60)
        koch(turtle,length/3,N-1)
mywin = turtle.Screen()
mykame = turtle.Turtle()
mykame.speed(10)
mykame.penup()
mykame.goto(-300,-200)
mykame.pendown()
k=3
koch(mykame,500,k)
mywin.exitonclick()
