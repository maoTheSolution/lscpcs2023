# draw color filled circle in turtle 
import random 
import turtle 
  
# creating turtle pen 
t = turtle.Turtle() 

# taking input for the radius of the circle 
# r = int(input("Enter the radius of the circle: ")) 
r = random.randint(1, 250)
# taking the input for the color 
# col = input("Enter the color name or hex value of color(# RRGGBB): ") 
sampleColors = ['Red', 'Green', 'Black', 'Blue']
col = sampleColors[random.randint(0, len(sampleColors)-1)]
  
# set the fillcolor 
t.fillcolor(col) 
  
# start the filling color 
t.begin_fill() 
  
# drawing the circle of radius r 
t.circle(r) 

# Event Handlers
turtle.listen()
  
# ending the filling of the color 
t.end_fill() 

turtle.exitonclick() 