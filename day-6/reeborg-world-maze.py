"""
This code solves the maze problem of the Reeborg's World

Reeborg was exploring a dark maze and the battery in its flashlight ran out.

This program helps Reeborg to find the exit. The secret is to have Reeborg follow 
along the right edge of the maze, turning right if it can, going straight ahead 
if it can’t turn right, or turning left as a last resort.

Defined functions
---------------------
functions: move() and turn_left()
conditions: test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().

For details please visit this site:
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world2.json&url=user_world%3Aproblem_world2.json
"""

def turn_right():
    """Turn the reborg to right using defined function turn_left()"""
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
    else:
        turn_left()
