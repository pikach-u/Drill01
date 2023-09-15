import turtle

def moveTurtle():
    turtle.forward(50)
    turtle.stamp()
    
def move_up():
    turtle.setheading(90)
    moveTurtle()
    
def move_down():
    turtle.setheading(-90)
    moveTurtle()
    
def move_left():
    turtle.setheading(-180)
    moveTurtle()
    
def move_right():
    turtle.setheading(0)
    moveTurtle()
    
def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(move_up,'w')
turtle.onkey(move_up,'W')
turtle.onkey(move_down,'s')
turtle.onkey(move_down,'S')
turtle.onkey(move_left,'a')
turtle.onkey(move_left,'A')
turtle.onkey(move_right,'d')
turtle.onkey(move_right,'D')
turtle.onkey(restart, 'Escape')
turtle.listen()
