def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if not wall_in_front() and wall_on_right():
        move()
    elif right_is_clear():
        turn_right()
        move()

    while wall_in_front() and wall_on_right():
        turn_left()
