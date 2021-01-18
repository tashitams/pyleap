"""
+---------------------------------------+
|      Pyleap Course: Final Project     |
|      Title: Save the Ship             |
|      Author: Tashi Dorji Tamang       |
|      School: Buli Central School      |
+---------------------------------------+
"""

from pyleap import *
from random import randint, choice

window.set_size(720, 480)
window.set_caption("Navigate the Spaceship")

score_txt = Text('Score:', 530, 445, 16, '#FAFAFA', font_name='Cooper Black')
level_txt = Text('Level: 1', 530, 415, 16, '#FAFAFA', font_name='Cooper Black')

crash_sound = Audio("assets/sound/crash.mp3")

# Image urls
bg_url = "assets/img/bg.jpg"
direction_url = "assets/img/direction.png"
spaceship_url = "assets/img/spaceship.png"
asteroid_1_url = "assets/img/asteroid_1.png"
asteroid_2_url = "assets/img/asteroid_2.png"
asteroid_3_url = "assets/img/asteroid_3.png"
asteroid_4_url = "assets/img/asteroid_4.png"
asteroid_5_url = "assets/img/asteroid_5.png"
asteroid_6_url = "assets/img/asteroid_6.png"
asteroid_7_url = "assets/img/asteroid_7.png"
play_again_url = "assets/img/play_again.png"

bg = Sprite(bg_url, window.w)

spaceship = Sprite(spaceship_url, 50, 300)
spaceship.scale = 0.2

play_again = Sprite(play_again_url, 360, 250)
play_again.scale = 0.5

direction = Sprite(direction_url, 50, 440)
direction.scale = 0.5
direction_txt = Text('Use following', 115, 445, 16, '#FAFAFA', font_name='Cooper Black')
direction_key_txt = Text('KEYS', 115, 420, 16, '#FAFAFA', font_name='Cooper Black')

asteroid_1 = Sprite(asteroid_1_url, 750, 450)
asteroid_2 = Sprite(asteroid_2_url, 950, 250)
asteroid_3 = Sprite(asteroid_3_url, 1150, 150)
asteroid_4 = Sprite(asteroid_4_url, 1450, 50)
asteroid_5 = Sprite(asteroid_5_url, 1650, 275)
asteroid_6 = Sprite(asteroid_6_url, 1900, 350)
asteroid_7 = Sprite(asteroid_7_url, 1750, 165)

# Create a list of asteroids
asteroids = [asteroid_1, asteroid_2, asteroid_3, asteroid_4, asteroid_5, asteroid_6, asteroid_7]
for i in asteroids:
    i.scale = 0.175

score = 0
speed = 3


def moveUp():
    spaceship.y += 50

def moveDown():
    
    spaceship.y -= 50

def moveLeft():
    spaceship.x -= 50

def moveRight():
    spaceship.x += 50

def game(dt):
    global score, speed
    bg.draw()
    direction.draw()
    direction_txt.draw()
    direction_key_txt.draw()
    spaceship.draw()
    spaceship.x += 1
    spaceship.y -= 1
    score_txt.draw()
    level_txt.draw()


    for i in asteroids:
        i.draw()
        i.x -= speed

        if i.x < 0:
            i.x = randint(750, 3500)
            i.y = randint(0, 480)

        if spaceship.collide(i):
            crash_sound.play()
            score_txt.src = 'Score: '+str(score)
            score_txt.draw()
            play_again.draw()
            stop(game)
            
        else:
            score += 1
            score_txt.src = 'Score: '+str(score)
            score_txt.draw()

    # Show level based on score
    # and increase the speed
    if score < 1000:
        speed = 4
        level_txt.src = 'Level: 1'
        level_txt.draw()
        return speed

    elif score >= 1000 and score <= 3000:
        speed = 5
        level_txt.src = 'Level: 2'
        level_txt.draw()
        
	    
    elif score > 3000 and score <= 5000:
        speed = 6
        level_txt.src = 'Level: 3'
        level_txt.draw()
	    
    elif score > 5000 and score <= 8000:
        speed = 7
        level_txt.src = 'Level: 4'
        level_txt.draw()
	    
    else:
        speed = 8
        level_txt.src = 'Level: 5'
        level_txt.draw()

        
# reset all the values
# and restart the game
def restart():
    global score, speed
    spaceship.x, spaceship.y = 50, 300
    asteroid_1.x, asteroid_1.y = 750, 450
    asteroid_2.x, asteroid_2.y = 950, 250
    asteroid_3.x, asteroid_3.y = 1150, 150
    asteroid_4.x, asteroid_4.y = 1450, 50
    asteroid_5.x, asteroid_5.y = 1650, 275
    asteroid_6.x, asteroid_6.y = 1900, 350
    asteroid_7.x, asteroid_7.y = 2300, 175
    score = 0
    speed = 3
    repeat(game)
    

play_again.on_press(restart)
key.UP.on_press(moveUp)
key.DOWN.on_press(moveDown)
key.LEFT.on_press(moveLeft)
key.RIGHT.on_press(moveRight)

repeat(game)
run()
