'''
Project: Helicopter of Bhutan
Author: Kinzang Jigdra
Class: 9 'A'
School: Buli Central School
'''

from pyleap import *

window.set_size(1000,640)
window.set_caption("Helicopter of Bhutan")

music = Audio("heli.mp3")

blue_bg = Rectangle(0,50,1000,640,"#00bfff")
green_bg = Rectangle(0,0,1000,300,"green")
body1 = Ellipse(500,300,200,50,"red")
body1.line_width=15
body2 = Ellipse(500,315,200,50,"red")
body2.line_width=15
tail = Polygon(116,302,324,284,326,339,155,324,146,367,116,367,116,302,"red")
R1 = Rectangle(479,360,35,30,"red")
E1 = Ellipse(495,390,300,10,"black")
glass1=Polygon(404,304,686,304,619,340,404,340,404,304,"white")
frontleg=Line(601,259,608,223,10,"black")
backleg=Line(393,259,390,223,10,"black")
baseleg=Line(362,223,645,223,10,"black")
door=Rectangle(515,259,50,78,"black")
door.line_width=5
head = Circle(640,321,5,"black")
part = Ellipse(640,311,7,7,"black")
sun = Circle(665,600,25,"yellow")
ground=Ellipse(494,127,400,75,"brown")
L1=Rectangle(359,145,275,15,"white")
L2=Rectangle(359,90,275,15,"white")
L3=Rectangle(477,100,15,50,"white")
name = Text("Bhutan Heli - Call 113",160,300,font_name="Bahnschrift Condensed",color="black",font_size=20)
backfan=Circle(133,346,15,"#00bfff")
backcircle=Circle(133,346,5,"black")
mill1=Line(133,346,133,360,4,"black")
mill2=Line(133,346,145,340,4,"black")
mill3=Line(133,346,122,338,4,"black")

def draw(dt):
    window.clear()
    music.play()
    blue_bg.draw()
    
    green_bg.y -=1
    if green_bg.y > 100:
       green_bg.y = 0
    green_bg.draw()
    
    body1.draw()
  
    body2.draw()
   
    tail.draw()
    
    R1.draw()
   
    E1.draw()
    E1.x += 5
    if E1.x > 499:
        E1.x = 489
    E1.y += 3
    if E1.y > 392:
        E1.y =388
   
    glass1.draw()  
    frontleg.draw()
    backleg.draw()
    
    ground.draw()
    ground.y -=1
    if ground.y > 127:
       ground.y = 50
    
    baseleg.draw()    
    door.stroke()   
    head.draw()    
    part.draw()
    sun.draw()
       
    L2.draw()
    L2.y -=1
    if L2.y>90:
       L2.y =50
       
    L3.draw()
    L3.y -=1
    if L3.y>100:
       L3.y =50

    L1.draw()
    L1.y -=1
    if L1.y>145:
       L1.y =50

    name.draw()
    backfan.draw()
    backcircle.draw()
    mill1.draw()
    mill1.set_anchor(133,346)
    mill1.rotation -=50
    
    mill2.draw()
    mill2.set_anchor(133,346)
    mill2.rotation -=50
    
    mill3.draw()
    mill3.set_anchor(133,346)
    mill3.rotation -=50 

repeat(draw)
run()
