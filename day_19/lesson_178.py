from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def forwards():
    tim.forward(10)

def back():
    tim.backward(10)

def left():
    tim.left(10)

def right():
    tim.right(10)

def clear():
    tim.reset()
    


screen.listen()
screen.onkey(key="w",fun=forwards)
screen.onkey(key="s",fun=back)
screen.onkey(key="d",fun=right)
screen.onkey(key="a",fun=left)
screen.onkey(key="c",fun=clear)


screen.exitonclick()