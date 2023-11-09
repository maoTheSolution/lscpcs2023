import turtle as tt
import random as rd

window = tt.Screen()
window.bgcolor("white")
window.screensize(600, 600)
pen = tt.Turtle()

# print(tt.screensize())
# print(tt.pos())

for each in range(10):
    xPos = rd.randint(-250, 250)
    yPos = rd.randint(-250, 250)
    tt.penup()
    tt.goto(xPos, yPos)
    tt.pendown()

    xTemp = abs(window.screensize()[0]/2) - abs(xPos)
    yTemp = abs(window.screensize()[1]/2) - abs(yPos)

    if xTemp > yTemp:
        tt.circle(yTemp/2)
    elif xTemp < yTemp:
        tt.circle(xTemp/2)
    else:
        tt.circle(yTemp/2)


tt.done()
