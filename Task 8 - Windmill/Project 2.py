"""
+---------------------------------------+
|      Pyleap Course: Project 2         |
|      Title: Smoking kills             |
|      Author: Tashi Dorji Tamang       |
|      School: Buli Central School      |
+---------------------------------------+
"""


from pyleap import *
import random

window.set_size(680, 500)
window.set_caption("Project 2 - Smoking Kills")

background = Rectangle(0,0,window.w,window.h, "#FBFBFB")
smoking_txt = Text('SMOKING', x=250, y=400, color="black", font_size=30, font_name="Bookman Old Style")
divider_line = Line(x1=245, y1=385, x2=455, y2=385, line_width=4, color="black")
kill_txt = Text('KILLS', x=310, y=350, color="black", font_size=23, font_name="Bookman Old Style")

cig = Rectangle(x=150, y=185, w=350, h=50, color="white")
cig_bud = Rectangle(x=150, y=185, w=90, h=50, color="#F38D44")
cig_bug_pattern_1 = Circle(170, 200, 5, "#FFC535")
cig_bug_pattern_2 = Ellipse(x=190, y=215, r_x=8, r_y=10, color="#FFC535")
cig_bug_pattern_3 = Ellipse(x=220, y=197, r_x=8, r_y=4, color="#FFC535")
cig_bug_pattern_4 = Ellipse(x=225, y=225, r_x=9, r_y=5, color="#FFC535")

cig_fire = Rectangle(x=495, y=185, w=8, h=50, color="#9C3D14")

colors = ["#d3d3d3", "#708090", "#696969", "#777696", "#343434"]

#blocks = Rectangle(random.randint(495,500), random.randint(185,235), random.randint(1,20), random.randint(1,20), random.choice(colors))
blocks = Circle(500, 235, 5)

line_1 = Line(x1=180, y1=150, x2=180, y2=205, line_width=4, color="black")
line_2 = Line(x1=275, y1=105, x2=275, y2=205, line_width=4, color="black")
line_3 = Line(x1=350, y1=160, x2=350, y2=205, line_width=4, color="black")
line_4 = Line(x1=450, y1=120, x2=450, y2=205, line_width=4, color="black")
  

@repeat   
def draw(dt):
    window.clear()
    window.show_axis()
    background.draw()
    smoking_txt.draw()
    divider_line.draw()
    kill_txt.draw()
    cig.draw()
    cig_bud.draw()
    cig_bug_pattern_1.draw()
    cig_bug_pattern_2.draw()
    cig_bug_pattern_3.draw()
    cig_bug_pattern_4.draw()
    cig_fire.draw()

    line_1.draw()
    line_2.draw()
    line_3.draw()
    line_4.draw()
    
    Text('20 Minutes', x=130, y=120, color="black", font_size=16, font_name="Calibri").draw()
    Text('after quiting', x=130, y=100, color="black", font_size=12).draw()
    
    Text('2 Weeks', x=235, y=75, color="black", font_size=16, font_name="Calibri").draw()
    Text('after quiting', x=235, y=55, color="black", font_size=12).draw()
    
    Text('2 Years', x=325, y=130, color="black", font_size=16, font_name="Calibri").draw()
    Text('after quiting', x=325, y=110, color="black", font_size=12).draw()
    
    Text('5 Years', x=420, y=90, color="black", font_size=16, font_name="Calibri").draw()
    Text('after quiting', x=420, y=70, color="black", font_size=12).draw()

    blocks.y += 2
    if blocks.y > 500:
        blocks.x = random.randint(495,500)
        blocks.y = random.randint(185,235)
        blocks.line_width = random.randint(1,5)
        blocks.color = random.choice(colors)
    blocks.stroke() 

#repeat(smoking)
#repeat(draw)
run()
