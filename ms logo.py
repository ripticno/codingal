import turtle
a=str(input("enter your color "))
turtle.Screen().bgcolor(a)
b=int(input("enter your screen size base "))
c=int(input("enter your screen size hight "))
turtle.Screen().setup(b,c)
a=turtle.Turtle()
a.speed(1)
d=int(input("enter your polygon number of side "))
num_side=d
angle=360/num_side
e=int(input("enter your side lenth "))
side_lenth=e

for i in range(num_side):
    a.fd(side_lenth)
    a.rt(angle)
turtle.done()