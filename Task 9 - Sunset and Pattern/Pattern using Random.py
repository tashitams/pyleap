from pyleap import *
from random import choice

window.set_size(w=600, h=480) 
window.set_caption("Use of Random")
title_txt = Text('Flower using Random', 180, 350, 18, '#FAFAFA', font_name='Bookman Old Style') 
colors = ["#FF5733", "#5533FF", "#33FF77", "#DA33FF", "#FFF633", "#50504B"]
flower = Circle(300, 240, 50,)
flower.set_anchor(300, 200)
def draw(dt):
    title_txt.draw()
    flower.stroke()
    flower.color = choice(colors)
    flower.rotation += 30 

repeat(draw)
run()
    
