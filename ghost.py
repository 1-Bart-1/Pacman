from random import random, randint

obstacles = {
1 : [5,0], 2 : [1,1], 3 : [2,1], 4 : [3,1], 5 : [7,1], 6 : [5,2], 7 : [7,2], 8 : [0,3], 9 : [1,3], 
10 : [3,3], 11 : [4,3], 12 : [5,3], 13 : [7,3], 14 : [0,4], 15 : [1,4], 16 : [3,5], 17 : [4,5], 18 : [6,5], 19 : [7,5],
20 : [0,6], 21 : [2,6], 22 : [3,6], 23 : [4,6], 24 : [7,6], 25 : [1,7], 26 : [6,7], 27 : [7,7],
}


global not_possible_direction


# List for the ghost matrix movement
ghost_speed = [1, 1] 

# Ghost position in a list, containing the startposition
ghost_position = [6,6]  

# Stating the moving direction as an int
ghost_move_direction = int

def ghost_cant_move(not_possible_direction):
    x = 0

    
    for i in range(1, 27):
        ghost_position[1] += ghost_speed[1]
        if ghost_position == obstacles[i]:
            ghost_position[1] -= ghost_speed[1]
            x += 1
            not_possible_direction[x] = "down"
        else:
            ghost_position[1] -= ghost_speed[1]


    for i in range(1, 27):
        ghost_position[0] -= ghost_speed[0]
        if ghost_position == obstacles[i]:
            ghost_position[0] += ghost_speed[0]
            x += 1
            not_possible_direction[x] = "left"
        else:
            ghost_position[0] += ghost_speed[0]
    


    for i in range(1, 27):
        ghost_position[0] += ghost_speed[0]
        if ghost_position == obstacles[i]:
            ghost_position[0] -= ghost_speed[0]
            x += 1
            not_possible_direction[x] = "right"
        else:
            ghost_position[0] -= ghost_speed[0]



    for i in range(1, 27):
        #print(ghost_position[1])
        ghost_position[1] -= ghost_speed[1]
        #print(ghost_position[1])

        if ghost_position == obstacles[i]:
            print(obstacles[i])
            ghost_position[1] += ghost_speed[1]
            x += 1
            not_possible_direction[x] = "up"
        else:
            ghost_position[1] += ghost_speed[1]



        



    print(not_possible_direction)
    return not_possible_direction




def ghost_movement(not_possible_direction):
    print("move", not_possible_direction)
    ghost_random_direction = randint(0 ,3 - len(not_possible_direction))
    possible_direction = ["left", "right", "up", "down"]
    for i in not_possible_direction:
        for n in possible_direction:
            if not_possible_direction[i] == n:
                possible_direction.remove(n)
            else:
                pass
    #print(possible_direction)
    #print(not_possible_direction)


    if possible_direction[ghost_random_direction] == "left":
            if 0 <= ghost_position[0] - ghost_speed[0] <= 7:
                    ghost_position[0] -= ghost_speed[0] 
                    not_possible_direction = {}       


    if possible_direction[ghost_random_direction] == "up":
            if 0 <= ghost_position[1] - ghost_speed[1] <= 7:
                ghost_position[1] -= ghost_speed[1]
                not_possible_direction = {}
      

    if possible_direction[ghost_random_direction] == "right":
            if 0 <= ghost_position[0] + ghost_speed[0] <= 7:
                ghost_position[0] += ghost_speed[0]
                not_possible_direction = {}


    if possible_direction[ghost_random_direction] == "down":
            if 0 <= ghost_position[1] + ghost_speed[1] <= 7:
                ghost_position[1] += ghost_speed[1]
                not_possible_direction = {}

    return ghost_position



        

                                        
        








