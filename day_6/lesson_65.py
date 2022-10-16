def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if not wall_on_right() and wall_in_front():
        turn_right()
        move()
    elif (not wall_on_right()) and (not wall_in_front()):
        move()
    elif wall_on_right() and (not wall_in_front()):
        move()
    else:
        turn_left()
