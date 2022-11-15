# Importing the necessarry libraries
from time import sleep
from sense_hat import SenseHat
from random import random, randint

# Direction containing the "maze" elements position on the sensehat led matrix
obstacles = {
1 : [5,0], 2 : [1,1], 3 : [2,1], 4 : [3,1], 5 : [7,1], 6 : [5,2], 7 : [7,2], 8 : [0,3], 9 : [1,3], 
10 : [3,3], 11 : [4,3], 12 : [5,3], 13 : [7,3], 14 : [0,4], 15 : [1,4], 16 : [3,5], 17 : [4,5], 18 : [6,5], 19 : [7,5],
20 : [0,6], 21 : [2,6], 22 : [3,6], 23 : [4,6], 24 : [7,6], 25 : [1,7], 26 : [6,7], 27 : [7,7],
}



# Sensehat definition
sense = SenseHat()

# List for the ghost matrix movement
ghost_speed = [1, 1] 

# Ghost position in a list, containing the startposition
ghost_position = [6,6]  

# Stating the moving direction as an int
ghost_move_direction = int


# Function for returning a random direction for the ghost movement
def ghost_direction():
    # Making the variable global
    global ghost_move_direction
    # Assigning a random value to the variable
    ghost_move_direction = randint(0, 3)
    # Returning the variable as an answer to the function call
    return ghost_move_direction

# Function for moving the ghost in the led matrix
def ghost_movement():
    


    """
    If statement checking if the ghost moving direction is 0. 
    Moves the ghost in this direction, as long as it not collides with any game object in that direction
    """

    if ghost_move_direction == 0:
            if 0 <= ghost_position[0] - ghost_speed[0] <= 7:
                ghost_position[0] -= ghost_speed[0]
                for i in range(1, 27):
                    if ghost_position == obstacles[i]:
                        ghost_position[0] += ghost_speed[0]

                    #Else.. continue    
                    else:
                        pass
    """
    If statement checking if the ghost moving direction is 1. 
    Moves the ghost in this direction, as long as it not collides with any game object in that direction
    """
    if ghost_move_direction == 1:
            if 0 <= ghost_position[1] - ghost_speed[1] <= 7:
                ghost_position[1] -= ghost_speed[1]
                for i in range(1, 27):
                    if ghost_position == obstacles[i]:
                        ghost_position[1] += ghost_speed[1]


                    #Else.. continue
                    else:
                        pass   
    """
    If statement checking if the ghost moving direction is 2. 
    Moves the ghost in this direction, as long as it not collides with any game object in that direction
    """       
    if ghost_move_direction == 2:             
            if 0 <= ghost_position[0] + ghost_speed[0] <= 7:
                ghost_position[0] += ghost_speed[0]
                for i in range(1, 27):
                    if ghost_position == obstacles[i]:
                        ghost_position[0] -= ghost_speed[0]


                    #Else.. continue
                    else:
                        pass
    """
    If statement checking if the ghost moving direction is 3. 
    Moves the ghost in this direction, as long as it not collides with any game object in that direction
    """
    if ghost_move_direction == 3:
            if 0 <= ghost_position[1] + ghost_speed[1] <= 7:
                ghost_position[1] += ghost_speed[1]
                for i in range(1, 27):
                    if ghost_position == obstacles[i]:
                        ghost_position[1] -= ghost_speed[1]


                    #Else.. continue
                    else:
                        pass

    # Returning the ghost position as an answer to the function call
    return  ghost_position



