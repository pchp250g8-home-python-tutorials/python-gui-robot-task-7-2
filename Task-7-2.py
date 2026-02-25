from robot import *

while is_free_left() or is_free_up():
    
    if is_free_left():
        while is_free_left():
            move_left()
    
    if is_free_up():
        while is_free_up():
            move_up()