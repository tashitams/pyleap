from pyleap import *
import random
import time

window.set_size(w=610, h=400) 
window.set_caption("Dinosaur Game")   

# static variables
background = Rectangle(0, 0, window.w, window.h, color="#F7F7F7")
title = Text("Dinosaur Game - T-Rex Run!", x=85, y=350, color="#111111", font_size=22, font_name="Consolas") 
label = Text("Press SPACE to start the game. Press Arrow(↑) key to jump", x=50, y=310, color="#2b2b2b", font_size=12, font_name="Consolas") 
ground = Sprite("assets/img/ground.png", x=610, y=35)
game_over_image = Sprite("assets/img/game_over.png", x=300, y=250)
game_over_image.scale = 0.7
score_txt = Text('Your score', 190, 200, 18, 'green', font_name='Consolas') 
restart_game_txt = Text('Restart Game', 225, 165, 18, 'red', font_name='Consolas') 

# dynamic variables
score = 0 

# declare and scale Cacti images
cactus_small = Sprite("assets/img/cacti_small.png", x=610, y=40)
cactus_big = Sprite("assets/img/cacti_big.png", x=630, y=40)
cactus_small.scale = 0.45
cactus_big.scale = 0.45

# declare and scale dinosaur images
dino = Sprite("assets/img/dino.png", x=30, y=45)
dino_run_up = Sprite("assets/img/dino_1.png", x=30, y=45)
dino_run_down = Sprite("assets/img/dino_2.png", x=30, y=45)

dino.scale = 0.4
dino_run_up.scale = 0.4
dino_run_down.scale = 0.4

dino_run = [dino_run_up, dino_run_down]



# sounds for jump, game_over and game_start
jump_sound = Audio("assets/sound/start.wav")
game_start_sound = Audio("assets/sound/start.wav")
game_over_sound = Audio("assets/sound/over.wav")


@key.SPACE.on_press
def jump():
    random.choice(dino_run).y += 40
    jump_sound.play()

"""@key.SPACE.on_release
def moveDown():
    random.choice(dino_run).y -= 40
    jump_sound.play() """


def game(dt):
    global score
    if random.choice(dino_run).collide(cactus_small) or random.choice(dino_run).collide(cactus_big):
        game_over_sound.play()
        game_over_image.draw()
        score_txt.src = 'Your score is '+str(score)
        score_txt.draw()
        restart_game_txt.draw()
        stop(game)
        return

    else:
        score += 1


    window.clear() 
    background.draw()
    title.draw()
    label.draw()
    
    ground.x -= 4.5
    if ground.x <-50:
        ground.x = 610
    ground.draw()

    random.choice(dino_run).draw() #dino.draw()

    score_txt.src = 'Your score is '+str(score)
    score_txt.draw()

    cactus_small.x -= 4
    if cactus_small.x < 50:
        cactus_small.x = random.randint(610, 620)
    cactus_small.draw()

    cactus_big.x -= 3
    if cactus_big.x < 0:
        cactus_big.x = random.randint(608, 635)
    cactus_big.draw()

def restart():
    ground.x = 610
    cactus_small.x = 610
    cactus_big.x = 610
    repeat(game)
    
restart_game_txt.on_press(restart)

repeat(game)
run()


