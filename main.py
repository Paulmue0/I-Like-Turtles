from TurtleApp import TurtleApp

def exercise1(turtle):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

def draw_circle(turtle):
    turtle.circle(100)

def draw_rectangle(turtle):
    for i in range (4):
        turtle.forward (100)
        turtle.right (90)    

# Add functions that should be accessible in the GUI App
app = TurtleApp([exercise1, draw_circle, draw_rectangle])
