"""
+---------------------------------------+
|      Pyleap Course: Task 12           |
|      Title: Traffic Game              |
|      Author: Tashi Dorji Tamang       |
|      School: Buli Central School      |
+---------------------------------------+
"""

from pyleap import *
from random import randint, choice

window.set_size(w=640, h=520) 
window.set_caption("Traffic Game")   

background = Rectangle(0, 0, window.w, window.h, color="#111111")
left_lane = Rectangle(0, 0, 140, window.h, color="#7AAE0E")
right_lane = Rectangle(500, 0, 140, window.h, color="#7AAE0E")

left_border = Rectangle(140, 0, 20, window.h, color="#FFFFFF")
right_border = Rectangle(480, 0, 20, window.h, color="#FFFFFF")

# Create a list of cars
lane_dividers = [
    Rectangle(310, 20, 30, 80, color="#FFFFFF"),
    Rectangle(310, 120, 30, 80, color="#FFFFFF"),
    Rectangle(310, 220, 30, 80, color="#FFFFFF"),
    Rectangle(310, 320, 30, 80, color="#FFFFFF"),
    Rectangle(310, 420, 30, 80, color="#FFFFFF"),
]

player_car = Sprite("assets/img/player_car.png", 240, 100)
player_car.scale = 0.25

car_1 = Sprite("assets/img/car_1.png", 160, 750)
car_2 = Sprite("assets/img/car_2.png", 250, 800)
car_3 = Sprite("assets/img/car_3.png", 480, 920)
car_4 = Sprite("assets/img/car_4.png", 380, 1300)

# Create a list of cars
cars = [car_1, car_2, car_3, car_4]
for i in cars:
    i.scale = 0.25
    
score_txt = Text('Score:', 10, 300, 16, '#111111', font_name='Consolas')
restart_game_txt = Text('Play Again', 10, 250, 16, '#111111', font_name='Consolas')

crash_sound = Audio("assets/sound/crash_sound.mp3")

score = 0

def game(dt):
    global score
    window.clear()
    background.draw()
    left_lane.draw()
    right_lane.draw()
    left_border.draw()
    right_border.draw()

    # Use loop to draw all the lane dividers
    for i in lane_dividers:
        i.draw()

        i.y -= 5

        if i.y < 0:
            i.y = 520

    # Draw player's car
    player_car.draw()

    # Use loop to draw all the cars at once
    for i in cars:
        i.draw()

        i.y -= 5

        if i.y < 0:
            i.y = randint(600, 1500)
            i.x = randint(150, 500)

        if player_car.collide(i):
            crash_sound.play()
            score_txt.src = 'Score: '+str(score)
            score_txt.draw()
            restart_game_txt.draw()
            stop(game)
        else:
            score += 1
    
           
    
def moveLeft():
    player_car.x -= 50
    if player_car.x < 160:
        player_car.x += 50

def moveRight():
    player_car.x += 50
    if player_car.x > 480:
        player_car.x -= 50

def moveUp():
    player_car.y += 50
    if player_car.y > 480:
        player_car.y -= 50

def moveDown():
    player_car.y -= 50
    if player_car.y < 60:
        player_car.y += 50


# reset all the values
# and restart the game
def restart():
    global score
    player_car.x, player_car.y = 240, 100
    car_1.x, car_1.y = 160, 750
    car_2.x, car_2.y = 250, 800
    car_3.x, car_3.y = 480, 920
    car_4.x, car_4.y = 380, 1300
    score = 0
    repeat(game)
    

restart_game_txt.on_press(restart)
key.LEFT.on_press(moveLeft)
key.RIGHT.on_press(moveRight)
key.UP.on_press(moveUp)
key.DOWN.on_press(moveDown)

repeat(game)
run()


