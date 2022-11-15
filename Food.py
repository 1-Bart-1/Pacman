from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

food_color = [50,50,50]
black = (0,0,0)


obstacles = {
1 : [5,0], 2 : [1,1], 3 : [2,1], 4 : [3,1], 5 : [7,1], 6 : [5,2], 7 : [7,2], 8 : [0,3], 9 : [1,3], 
10 : [3,3], 11 : [4,3], 12 : [5,3], 13 : [7,3], 14 : [0,4], 15 : [1,4], 16 : [3,5], 17 : [4,5], 18 : [6,5], 19 : [7,5],
20 : [0,6], 21 : [2,6], 22 : [3,6], 23 : [4,6], 24 : [7,6], 25 : [0,7], 26 : [6,7], 27 : [7,7],
}

food_positions = [
[0, 0], [0, 1], [0, 2], [0, 5], [1, 0], [1, 2], [1, 5], [1, 6], [1, 7], 
[2, 0], [2, 2], [2, 3], [2, 4], [2, 5], [2, 7], [3, 0], [3, 2], [3, 4], [3, 7], 
[4, 0], [4, 1], [4, 2], [4, 4], [4, 7], [5, 1], [5, 4], [5, 5], [5, 6], [5, 7], 
[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 6], [7, 0], [7, 4]
]


food = []

def eat_food(food, player_position):
    if player_position in food: #sjekker om packman er på en mat 
        sense.set_pixels(player_position[0],[1],black)
        food.remove(player_position) #tar vekk maten fra listen
        score += 1

def check_win(food):
    if len(food)==0:
        return True
    else:
        return False

