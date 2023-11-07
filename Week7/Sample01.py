import turtle 
import random


pen = turtle.Turtle()
win = turtle.Screen()
win.screensize(600, 600)

def square(t, length):
    # drawing first side
    t.forward(length) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree
 
    # drawing second side
    t.forward(length) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree
 
    # drawing third side
    t.forward(length) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree
 
    # drawing fourth side
    t.forward(length) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree


for each in range(10):
    xPos = random.randint(-300, 300)
    yPos = random.randint(-300, 300)
    pen.penup()
    pen.goto(xPos, yPos)
    # print("X : ", pen.pos()[0], ",  Y : ", pen.pos()[1])
    pen.pendown()
    # HW
    length = random.randint(10, 600)
    if pen.pos()[0] < 0:
    else :
        
        if win.screensize()[0]/2 - pen.pos()[0] < 0:
            
    
    
    square(pen, length)




turtle.exitonclick()





