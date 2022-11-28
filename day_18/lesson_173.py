import turtle as turtle_module
import random

turtle_module.colormode(255)

rgb_list = [(155, 85, 51), (196, 153, 110), (50, 106, 145), (148, 21, 42), (152, 59, 79), (15, 44, 72), (62, 120, 94), (237, 244, 241), (73, 29, 43), (57, 38, 23), (136, 160, 176), (194, 79, 99), (203, 93, 71), (188, 143, 155), (173, 131, 55), (133, 161, 149), (18, 60, 126), (83, 153, 126), (24, 54, 35), (13, 96, 71), (62, 152, 170), (219, 175, 184), (106, 120, 154), (119, 39, 36), (7, 89, 103), (81, 75, 41), (221, 178, 171)]
width = 10
height = 1
number_of_dots = width * height

tim = turtle_module.Turtle()
tim.speed(0)

def move():
    tim.penup()
    tim.forward(50)
    tim.pendown()
    tim.dot(20)


for i in range(0, number_of_dots):
    tim.color(random.choice(rgb_list))              
    if i < width:        
        tim.dot(20)        
        tim.penup()        
        tim.pendown()
        if width - i != 1:
            tim.penup()
            tim.forward(50)
    elif ((i % width == 0) and ((i / width) % 2 != 0)):        
        tim.left(90)
        move() 
        tim.left(90)        
    elif (i % width == 0) and ((i / width) % 2 == 0): 
        tim.right(90)
        move() 
        tim.right(90)    
    else:        
        move()        

screen = turtle_module.Screen()
screen.exitonclick()