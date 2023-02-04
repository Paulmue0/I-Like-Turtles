from TurtleApp import TurtleApp

##########################################
### 01 Getting Started
##########################################

def draw_square(turtle):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

def draw_triangle(turtle):
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)

def draw_circle(turtle):
    turtle.circle(50)
    
def draw_star(turtle):
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)

exercise_list = [draw_square, draw_triangle, draw_circle, draw_star]
app = TurtleApp(exercise_list)