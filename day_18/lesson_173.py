from turtle import Turtle, Screen

rgb_list = [(247, 239, 245), (155, 85, 51), (196, 153, 110), (50, 106, 145), (148, 21, 42), (152, 59, 79), (15, 44, 72), (62, 120, 94), (237, 244, 241), (73, 29, 43), (57, 38, 23), (136, 160, 176), (194, 79, 99), (203, 93, 71), (188, 143, 155), (173, 131, 55), (133, 161, 149), (18, 60, 126), (83, 153, 126), (24, 54, 35), (13, 96, 71), (62, 152, 170), (219, 175, 184), (106, 120, 154), (119, 39, 36), (7, 89, 103), (81, 75, 41), (221, 178, 171)]

tim = Turtle()
screen = Screen()
tim.speed(1)

for i in range(0, 24):
    
    if i < 6:
        tim.dot(20)        
        tim.penup()        
        tim.pendown()
        if 6 - i != 1:
            tim.penup()
            tim.forward(50)

        
        

    elif ((i % 6 == 0) and ((i / 6) % 2 != 0)):        
        tim.left(90)
        tim.penup()
        tim.forward(50)
        tim.pendown()       
        tim.dot(20)
        tim.left(90)
        
    elif (i % 6 == 0) and ((i / 6) % 2 == 0): #если чётное    
        tim.right(90)
        tim.penup()
        tim.forward(50)
        tim.pendown()       
        tim.dot(20)
        tim.right(90)    
    else:        
        tim.penup()
        tim.forward(50)
        tim.pendown()
        tim.dot(20)       


screen.exitonclick()