import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(300,400)
a=turtle.Turtle()
a.speed(1)
num_side=3
angle=180/num_side
side_lenth=100

for i in range(num_side):
    a.fd(side_lenth)
    a.rt(angle)
turtle.done()