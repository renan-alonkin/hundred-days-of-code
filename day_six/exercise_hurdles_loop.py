# The exercise belongs to reeborg's world,
# and must be executed here: 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
# Hurdle 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def jump_n_obstacles(n):
    for i in range(0, n):
        move()
        jump()
         
jump_n_obstacles(6)

# Hurdle 2 - Defined places
# Using while
def jump_n_obstacles():
    while not at_goal():
        move()
        jump()
         
jump_n_obstacles()


# Hurdle 3 - Random places
# Using while
def jump_random_hurdles_w_random_sizes():
    while not at_goal():
        if not front_is_clear():
            jump()
        else:
            move()
            
jump_random_hurdles_w_random_sizes()

# Hurdle 5 - Random places and Random sizes
def jump_high_enough():
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
    
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()

# Using while
def jump_random_hurdles_w_random_sizes():
    while not at_goal():
        if not front_is_clear():
            jump_high_enough()
        else:
            move()
            
jump_random_hurdles_w_random_sizes()


