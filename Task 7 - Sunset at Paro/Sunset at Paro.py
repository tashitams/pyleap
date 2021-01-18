"""
+---------------------------------------+
|      Pyleap Course: Task 7            |
|      Title: Sunset at Paro            |
|      Author: Tashi Dorji Tamang       |
|      School: Buli Central School      |
+---------------------------------------+
"""


from pyleap import *

window.set_size(760, 580)
window.set_caption("Task 7 - Sunset at Paro")

night = Rectangle(0,0,window.w, window.h, "black")
background_img = Sprite('img/paro_valley.jpg')

sun = Circle(40, 300, 30, "yellow")


@repeat
def draw(dt):
    #window.show_axis()
    window.clear()
    background_img.draw()
   
    sun.y += 1.75
    night.draw()
    night.opacity += 0.0022
    if sun.y > 510:
        sun.y = 510
        sun.x += 3

        if sun.x > 760:
            exit()
    sun.draw()
run()
