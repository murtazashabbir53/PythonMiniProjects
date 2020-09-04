import turtle

pointer = turtle.Turtle()
pointer.width(8)
pointer.color("red")
new = turtle.getscreen()
pointer.speed(4)

new.bgcolor("lightblue")

# PENUP
pointer.left(180)
pointer.penup()
pointer.forward(300)
pointer.right(90)
pointer.forward(100)
pointer.pendown()

# Print H


#  draw it!
pointer.forward(50)
pointer.right(90)
pointer.forward(50)
pointer.left(90)
pointer.forward(50)
pointer.left(90)

pointer.penup()
pointer.forward(50)
pointer.left(90)
pointer.pendown()
pointer.forward(50)
pointer.left(90)
pointer.forward(50)
pointer.right(90)
pointer.forward(50)

# print A

pointer.penup()
pointer.left(90)
pointer.forward(15)
pointer.pendown()
pointer.left(70)
pointer.forward(110)
pointer.right(70)
pointer.right(70)
pointer.forward(110)
pointer.left(180)
pointer.forward(55)
pointer.left(70)
pointer.forward(38)
pointer.left(70)
pointer.penup()
pointer.forward(55)
pointer.left(110)

pointer.forward(100)

# print P

pointer.left(90)
pointer.pendown()
pointer.forward(100)
pointer.right(90)
pointer.forward(50)
pointer.right(20)
pointer.forward(20)
pointer.right(70)
pointer.forward(40)
pointer.right(70)
pointer.forward(20)
pointer.right(20)
pointer.forward(50)
pointer.left(90)
pointer.forward(50)
pointer.left(90)
pointer.penup()
pointer.forward(100)

# print P

pointer.left(90)
pointer.pendown()
pointer.forward(100)
pointer.right(90)
pointer.forward(50)
pointer.right(20)
pointer.forward(20)
pointer.right(70)
pointer.forward(40)
pointer.right(70)
pointer.forward(20)
pointer.right(20)
pointer.forward(50)
pointer.left(90)
pointer.forward(50)
pointer.left(90)
pointer.penup()
pointer.forward(100)

# print Y

pointer.forward(20)
pointer.pendown()
pointer.left(90)
pointer.forward(50)
pointer.left(30)
pointer.forward(60)
pointer.backward(60)
pointer.right(60)
pointer.forward(60)
pointer.backward(60)
pointer.left(30)

# go to Home

pointer.penup()
pointer.home()

pointer.color("yellow")
new.bgcolor("green")


# setting second row

pointer.backward(300)
pointer.right(90)
pointer.forward(60)
pointer.left(180)

# print P


pointer.pendown()
pointer.forward(100)
pointer.right(90)
pointer.forward(50)
pointer.right(20)
pointer.forward(20)
pointer.right(70)
pointer.forward(40)
pointer.right(70)
pointer.forward(20)
pointer.right(20)
pointer.forward(50)
pointer.backward(50)
pointer.left(180)
pointer.right(20)
pointer.forward(20)
pointer.right(70)
pointer.forward(40)
pointer.right(70)
pointer.forward(20)
pointer.right(20)
pointer.forward(50)
pointer.right(90)
pointer.forward(10)

# go to Home

pointer.penup()
pointer.home()

# setting up

pointer.backward(200)
pointer.right(90)
pointer.forward(10)
pointer.left(90)
pointer.pendown()
pointer.forward(20)
pointer.penup()
pointer.home()

# D

pointer.backward(150)
pointer.right(90)
pointer.forward(60)
pointer.pendown()
pointer.backward(100)
pointer.right(90)
pointer.forward(10)
pointer.backward(70)
pointer.left(180)
pointer.right(20)
pointer.forward(20)
pointer.right(70)
pointer.forward(88)
pointer.right(70)
pointer.forward(20)
pointer.right(20)
pointer.forward(70)

pointer.penup()
pointer.home()

# set up for A

pointer.backward(50)
pointer.right(90)
pointer.forward(65)
pointer.left(90)

# print A
pointer.pendown()
pointer.left(70)
pointer.forward(110)
pointer.right(70)
pointer.right(70)
pointer.forward(110)
pointer.left(180)
pointer.forward(55)
pointer.left(70)
pointer.forward(38)
pointer.left(70)
pointer.penup()
pointer.forward(55)
pointer.left(110)

pointer.forward(100)




# print Y
pointer.pendown()
pointer.left(90)
pointer.forward(50)
pointer.left(30)
pointer.forward(60)
pointer.backward(60)
pointer.right(60)
pointer.forward(60)
pointer.backward(60)
pointer.left(30)

# go to Home

pointer.penup()
pointer.home()

# setting up position

pointer.right(90)
pointer.forward(215)
pointer.right(90)
pointer.forward(200)
pointer.right(90)

# color

pointer.color("green")
new.bgcolor("lightblue")






#DESIGNING
# design pattern
pointer.home()
pointer.forward(200)
pointer.pendown()
pointer.color("red")
pointer.width(3)
pointer.speed(0)


def squre(length, angle):
    pointer.forward(length)
    pointer.right(angle)
    pointer.forward(length)
    pointer.right(angle)

    pointer.forward(length)
    pointer.right(angle)
    pointer.forward(length)
    pointer.right(angle)


squre(80, 90)

for i in range(36):
    pointer.right(10)
    squre(80, 90)

turtle.mainl
