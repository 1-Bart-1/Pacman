#MAIN

from random import randint
from time import sleep, time
from sense_hat import SenseHat
from random import randint

from Player import movement
from Player import player_position
from Player import direction

from Food import food, food_color, food_positions, eat_food

from Ghost import ghost_direction
from Ghost import ghost_movement
from Ghost import ghost_position


sense = SenseHat()

 

#------
eaten_foods = []

score = 0

direction = "still"
player_color = [239,231,11]         # Setter spiller farge til blå
food_color = [50,50,50]
green = [0,100,0]
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
sense.clear()



def collision_enemy_player(player_position, ghost_position):
    if player_position == ghost_position:
        return True
    return False


def get_score():
    try:
        file = open("score.txt", "r")
    except:
        file = ""
    try:
        score = int(''.join([n for n in file.read() if n.isdigit()]))
    except:
        score = 0
    return score


def draw(food_positions, score):
    sense.set_pixels(start_screen)
    sense.set_pixel(player_position[0], player_position[1], background_color)
    
    movement(direction)
    sense.set_pixel(player_position[0], player_position[1], player_color)

    for food_position in food_positions:
        if player_position == food_position and food_position not in eaten_foods:
            eaten_foods.append(food_position)

    for food_position in food_positions:
        if food_position not in eaten_foods:
             sense.set_pixel(food_position[0], food_position[1], food_color)
    
    sense.set_pixel(ghost_position[0], ghost_position[1], ghost_color)
    score = len(eaten_foods)
    return score

highscore = get_score()

running = True
playing = False
gameOver = False
last_click_time = time()

while running:
    rotation = sense.get_gyroscope_raw()

    for event in sense.stick.get_events():
        direction = event.direction
    
        print(time()-last_click_time)
        if direction == "middle" and time()-last_click_time > 1:
            playing = not playing
            last_click_time = time()
            break
    if abs(rotation['x']) > 2 and time()-last_click_time > 1:
        playing = not playing
        last_click_time = time()
        break

    if playing:
        if collision_enemy_player(player_position, ghost_position):
            playing = False
            running = False
            break

        score = draw(food_positions, score)
        eat_food(food, player_position)

        ghost_direction()
        ghost_movement()

        sleep(0.5) # determines the speed of the game

    if not playing: # instead of if else for better readability
        if direction=="down" and time()-last_click_time > 1:
            running = False
            break
        print_score(score)
        sleep(0.1) # sleep shorter for better sensor detection
            
print_score(score)
sleep(1)
sense.set_pixels([
y, g, g, g, g, g, y, y,
g, g, g, g, g, g, g, y,
g, y, y, g, y, y, g, y,
g, g, g, g, g, g, g, y,
g, g, g, y, g, g, g, y,
y, g, g, g, g, g, y, y,
y, g, y, g, y, g, y, y,
y, y, y, y, y, y, y, y
])
sleep(0.5)
sense.clear()