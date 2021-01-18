"""
+---------------------------------------+
|      Pyleap Course: Task 10           |
|      Title: Mouse & Cheese Game       |
|      Author: Tashi Dorji Tamang       |
|      School: Buli Central School      |
+---------------------------------------+
"""

from pyleap import *
from random import randint

window.set_size(w=700, h=560) 
window.set_caption("Mouse & Cheese Game")   

# static variables
background = Rectangle(0, 0, window.w, window.h, color="#F7F7F7")

score_board = Rectangle(200, 495, 300, 50, "black")
score_txt = Text('Your Score', 260, 512, 18, 'green', font_name='Consolas') 

rat = Sprite("assets/img/mouse.png", 350, 280)
rat.scale = 0.1

cheese = Sprite("assets/img/cheese.png", 300, 200)
cheese.scale = 0.3

# dynamic variables
score = 0 

munch_sound = Audio("assets/sound/munch.mp3")

@repeat
def game(dt):
    global score
    window.clear()
    score_board.draw()
    score_txt.draw()
    rat.draw() 
    rat.x = mouse.x
    rat.y = mouse.y
    cheese.draw()

    if rat.collide(cheese):
        munch_sound.play()
        score += 1
        score_txt.src = 'Your score: '+str(score)
        score_txt.draw()
        cheese.x = randint(20, 650) # make sure the cheese 
        cheese.y = randint(20, 480) # never appears on the edge           
run()


