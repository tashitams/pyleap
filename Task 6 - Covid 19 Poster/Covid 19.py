"""
+---------------------------------------+
|      Pyleap Course: Task 6            |
|      Title: Covid 19 Poster           |
|      Author: Tashi Dorji Tamang       |
|      School: Buli Central School      |
+---------------------------------------+
"""


from pyleap import *

window.set_size(680, 500)
window.set_caption("Task 6 - Covid 19 Poster")


background = Sprite('img/virus.png', x=620, y=420)
background.scale = 0.25
stop_poly = Polygon(150,350, 200,350, 240,400, 200,450, 150,450, 110,400, "red")
white_line_poly = Polygon(155,360, 198,360, 230,400, 198,440, 155,440, 120,400, "white")
white_line_poly.line_width = 5
covid_19_txt_rect = Rectangle(200, 375, 200, 50, "#0000ff")
covid_logo = Sprite('img/logo.png', x=315, y=405)
covid_logo.scale = 0.5
stop_txt = Text('STOP', x=135, y=390, color="white", font_size=22, font_name="LiSu")
symptom_txt = Text('SYMPTOMS', x=265, y=300, color="white", font_size=22, font_name="Bookman Old Style")

chestpain = Sprite('img/chestpain.png', x=95, y=220)
chestpain.scale = 0.05
chestpain_txt = Text('Chest pain', x=55, y=140, color="white", font_size=14, font_name="Bookman Old Style")

fever = Sprite('img/fever.png', x=250, y=220)
fever.scale = 0.05
fever_txt = Text('Fever', x=230, y=140, color="white", font_size=14, font_name="Bookman Old Style")

headache = Sprite('img/headache.png', x=410, y=220)
headache.scale = 0.05
headache_txt = Text('Headache', x=370, y=140, color="white", font_size=14, font_name="Bookman Old Style")

cough = Sprite('img/cough.png', x=590, y=220)
cough.scale = 0.05
cough_txt = Text('Cough', x=565, y=140, color="white", font_size=14, font_name="Bookman Old Style")

stay_home_rect = Rectangle(200, 30, 300, 50, "#0000ff")
stay_home_txt = Text('STAY HOME, STAY SAFE', x=218, y=47, color="white", font_size=16, font_name="LiSu")



@repeat
def draw(dt):
    #window.show_axis()
    background.draw()
    covid_19_txt_rect.draw()
    stop_poly.draw()
    white_line_poly.stroke()
    covid_logo.draw()
    stop_txt.draw()
    symptom_txt.draw()

    chestpain.draw()
    chestpain_txt.draw()
    
    fever.draw()
    fever_txt.draw()
    
    headache.draw()
    headache_txt.draw()
    
    cough.draw()
    cough_txt.draw()

    stay_home_rect.draw()
    stay_home_txt.draw()
    
    
    

run()
