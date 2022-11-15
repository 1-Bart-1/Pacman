#MAIN

from random import randint
from time import sleep
from sense_hat import SenseHat
from random import randint

from Player import movement
from Player import player_position
from Player import direction

from Food import food_init
from Food import food_init2
from Food import food_posisions
from Food import food
from Food import eat_food
from Food import check_win

from Ghost import ghost_direction
from Ghost import ghost_movement
from Ghost import ghost_position


sense = SenseHat()

 

#------
eaten_food = {}


direction = "still"
player_color = [239,231,11]         # Setter spiller farge til blå
food_color = [50,50,50]
y = background_color = [0, 0, 0]    # Setter bakgrunnsfargen til svart
g = map_color = [0, 0, 255]         # Setter banefargen til blå

red  = [255, 0, 0]
pink = [255, 184, 255]
blue = [0, 255, 255]
orange = [255, 184, 82]

r_color = randint(0, 3)

if r_color == 0: 
    ghost_color = red
elif r_color == 1: 
    ghost_color = pink
elif r_color == 2:
     ghost_color = blue
elif r_color == 3:
    ghost_color = orange


start_screen = [
y, y, y, y, y, g, y, y,
y, g, g, g, y, y, y, g,
y, y, y, y, y, g, y, g,
g, g, y, g, g, g, y, g,
g, g, y, y, y, y, y, y,
y, y, y, g, g, y, g, g,
g, y, g, g, g, y, y, g,
g, y, y, y, y, y, g, g
]
sense.clear




def collision_enemy_player(player_position, ghost_position):
    if player_position == ghost_position:
        playing = False
        gaveOver = True



def draw(food_posisions):
    sense.set_pixel(player_position[0], player_position[1], background_color)
    for i in range(1,37):
        if player_position == food_posisions[i]:
            print(i)
            eaten_food[i] = player_position
            print(eaten_food)
    movement(direction)
    sense.set_pixel(player_position[0], player_position[1], player_color)




    # for n in range(1,37):
    #     if ghost_position == eaten_food.get(n):
    #             sense.set_pixel(ghost_position[0], ghost_position[1], background_color)


                
        #else:
            #sense.set_pixel(ghost_position[0], ghost_position[1], food_color)
      

sense.set_pixels(start_screen)
food_init()
print(food)
sense.set_pixel(ghost_position[0], ghost_position[1], ghost_color)
sense.set_pixel(player_position[0], player_position[1], player_color)





running = True
playing = True
gameOver = False


while running:


    if playing:

        for event in sense.stick.get_events():
            direction = event.direction

        
        draw(food_posisions)
        eat_food(food, player_position)
        collision_enemy_player(player_position, ghost_position)

        ghost_direction()
        ghost_movement()
        sense.set_pixel(ghost_position[0], ghost_position[1], ghost_color)

 
        sleep(0.5)

    if gameOver:
        sense.show_message("Game Over", text_colour = [255, 0, 0])

