"""
+---------------------------------------+
|      Pyleap Course: Task 11           |
|      Title: Archer Game       |
|      Author: Tashi Dorji Tamang       |
|      School: Buli Central School      |
+---------------------------------------+
"""

from pyleap import *
from random import randint

window.set_size(w=720, h=600) 
window.set_caption("Archer Balloon Shooter")   


background = Rectangle(0, 0, window.w, window.h, color="#008000")
header = Rectangle(0, 510, window.w, window.h, "#010216")
title = Text('Balloon Shooter', 25, 540, 25, '#FAFAFA', font_name='Consolas')
game_over_image = Sprite("assets/img/game_over.png", x=350, y=380)
game_over_image.scale = 0.7
score_txt = Text('Score:', 480, 555, 20, '#FFE205', font_name='Consolas')
final_score_txt = Text('Final Score: 5', 245, 300, 20, '#FFFFFF', font_name='Consolas')
arrow_left_txt = Text('Arrow Left:', 480, 525, 20, '#E83D38', font_name='Consolas')

player = Sprite("assets/img/player.png", 70, 70)
player.scale = 0.4
player.opacity = 1

arrow_pulled = Sprite("assets/img/arrow_pulled.png", 70, 400)
arrow_pulled.scale = 0.4
arrow_pulled.opacity = 0 

arrow = Sprite("assets/img/arrow.png")
arrow.scale = 0.7
arrow.opacity = 0 

balloon = Sprite("assets/img/balloon.png", 680, 625)
balloon.scale = 0.4

# sounds for balloon burst and game_over 
pop_sound = Audio("assets/sound/pop.mp3")
game_over_sound = Audio("assets/sound/over.wav")

arrow_count = 10
score = 0

def game(dt):
    global score, arrow_count
    background.draw()
    header.draw()
    title.draw()
    score_txt.draw()
    arrow_left_txt.draw()


    arrow_pulled.draw()
    player.draw()
    arrow.draw()
    
    balloon.draw()
    balloon.y -= 2

    if balloon.y < 0:
        balloon.y = 600
        
    if arrow.opacity == 1:
        arrow.x += 3
        if arrow.x > window.w:
            arrow.opacity = 0
        
    if arrow.x > window.w:
        arrow_count -= 1
        arrow_left_txt.src = 'Arrow Left:'+ str(arrow_count)
        arrow_left_txt.draw()
        arrow.x = player.x+15 
        arrow.y = player.y+30

    if arrow_count == 0:
        game_over_sound.play()
        game_over_image.draw()
        final_score_txt.src = 'Final Score: '+str(score)
        final_score_txt.draw()
        stop(game)

    if arrow.collide(balloon):
        pop_sound.play()
        balloon.y = 600
        score += 1
        score_txt.src = 'Score:'+ str(score)
        score_txt.draw()
         
def pullArrow():
    arrow_pulled.opacity = 1
    player.opacity = 0
    arrow.opacity = 0
    

def releaseArrow():
    arrow_pulled.opacity = 0
    player.opacity = 1
    arrow.opacity = 1
    arrow.x = arrow_pulled.x+15
    arrow.y = arrow_pulled.y+30
    
      
def movePlayer():
    player.y = mouse.y
    arrow_pulled.y = mouse.y


def restart():
    arrow_pulled.opacity = 0
    player.opacity = 1
    arrow.opacity = 0
    arrow_count = 10
    score = 0
    repeat(game)
    
    
mouse.on_move(movePlayer)
mouse.on_press(pullArrow)
mouse.on_release(releaseArrow)

repeat(game)
run()


