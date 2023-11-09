import turtle
import random


pen = turtle.Turtle()
window = turtle.Screen()
window.screensize(600, 600)

# pen.penup()
# x = random.randint(-300, 300)
# y = random.randint(-300, 300)
# pen.goto(x, y)
# pen.down()


# while(True):
#     length = random.randint(0, 600)
#     xPos = pen.pos()[0]
#     yPos = pen.pos()[1]
#     l01 = 0
#     l02 = 0
#     if xPos < 0:
#         l01 = abs(xPos) + window.screensize()[0]/2
#     else:
#         l01 = window.screensize()[0]/2 - xPos

#     if yPos < 0:
#         l02 = window.screensize()[1]/2 + yPos
#     else :
#         l02 = window.screensize()[1]/2 + yPos

#     if length <= l01 and length <= l02:
#         break

# for each in range(4):
#     pen.forward(length)
#     pen.left(90)

for each in range(50):

    pen.penup()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    pen.goto(x, y)
    pen.down()


    while(True):
        length = random.randint(0, 600)
        xPos = pen.pos()[0]
        yPos = pen.pos()[1]
        l01 = 0
        l02 = 0
        if xPos < 0:
            l01 = abs(xPos) + window.screensize()[0]/2
            l02 = window.screensize()[1]/2 + yPos
        else:
            l01 = window.screensize()[0]/2 - xPos
            l02 = window.screensize()[1]/2 + yPos

        if length <= l01 and length <= l02 and (yPos + length) <= window.screensize()[1]/2:
            break

    for each in range(4):
        pen.forward(length)
        pen.left(90)

turtle.exitonclick()