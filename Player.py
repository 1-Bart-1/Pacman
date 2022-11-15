#Importerer bibliotek
from time import sleep
from sense_hat import SenseHat

#Setter sense til en variabel av SenseHat
sense = SenseHat()


obstacles = {
1 : [5,0], 2 : [1,1], 3 : [2,1], 4 : [3,1], 5 : [7,1], 6 : [5,2], 7 : [7,2], 8 : [0,3], 9 : [1,3], 
10 : [3,3], 11 : [4,3], 12 : [5,3], 13 : [7,3], 14 : [0,4], 15 : [1,4], 16 : [3,5], 17 : [4,5], 18 : [6,5], 19 : [7,5],
20 : [0,6], 21 : [2,6], 22 : [3,6], 23 : [4,6], 24 : [7,6], 25 : [0,7], 26 : [6,7], 27 : [7,7],
}


player_speed = [1, 1]                 #Setter spillerens hastighet
player_position = [2,2]             #Oppretter en liste for spillerens posisjon
direction = ""



def movement(direction):


    if direction == "left":
            if 0 <= player_position[0] - player_speed[0] <= 7:
                player_position[0] -= player_speed[0]
                for i in range(1, 27):
                    if player_position == obstacles[i]:
                        player_position[0] += player_speed[0]
                    else:
                        pass
                    


    if direction == "up":
            if 0 <= player_position[1] - player_speed[1] <= 7:
                player_position[1] -= player_speed[1]
                for i in range(1, 27):
                    if player_position == obstacles[i]:
                        player_position[1] += player_speed[1]
                    else:
                        pass            



    if direction == "right":             
            if 0 <= player_position[0] + player_speed[0] <= 7:
                player_position[0] += player_speed[0]
                for i in range(1, 27):
                    if player_position == obstacles[i]:
                        player_position[0] -= player_speed[0]
                    else:
                        pass
                

    if direction == "down":
            if 0 <= player_position[1] + player_speed[1] <= 7:
                player_position[1] += player_speed[1]
                for i in range(1, 27):
                    if player_position == obstacles[i]:
                        player_position[1] -= player_speed[1]
                    else:
                        pass

    return player_position




    


