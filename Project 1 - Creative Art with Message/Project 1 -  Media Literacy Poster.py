"""
+--------------------------------------------------------+
|      Pyleap Project 1: Creative Art                    |
|      Title: Media Literacy for Bhutanese Students      |
|      Author: Tashi Dorji Tamang                        |
|      School: Buli Central School                       |
+--------------------------------------------------------+
"""


from pyleap import *

window.set_size(650, 450)
window.set_caption("Media Literacy Poster")

background = Rectangle(0, 0, window.w, window.h, "#F6F6F6")
before_you_txt = Text('Student before you:', x=92, y=335, color="#000000", font_size=20, font_name="LiSu")
social_media = Sprite('C:/Users/Buli-Admin/Desktop/cyber_bulling/social_media.png', 200, 220)
social_media.scale = 0.35
think_txt = Text('Think!', x=400, y=335, color="#2DA639", font_size=20, font_name="LiSu")
is_it_txt = Text('Is it:', x=490, y=335, color="#335599", font_size=20, font_name="LiSu")

# T and True Text
t_poly = Polygon(410,275, 435,300, 410,325, 385,300, "black")
t_txt = Text('T', x=402, y=287, color="white", font_size=20, font_name="LiSu")
true_txt = Text('True?', x=455, y=290, color="#FFA500", font_size=20, font_name="LiSu")

# H and Helpful Text
h_poly = Polygon(410,220, 435,245, 410,270, 385,245, "black")
h_txt = Text('H', x=401, y=235, color="white", font_size=20, font_name="LiSu")
helpful_txt = Text('Helpful?', x=455, y=235, color="#FFA500", font_size=20, font_name="LiSu")

# I and Inspiring Text
i_poly = Polygon(410,165, 435,190, 410,215, 385,190, "black")
i_txt = Text('I', x=407, y=178, color="white", font_size=20, font_name="LiSu")
inspiring_txt = Text('Inspiring?', x=455, y=178, color="#FFA500", font_size=20, font_name="LiSu")

# N and Necessary Text
n_poly = Polygon(410,110, 435,135, 410,160, 385,135, "black")
n_txt = Text('N', x=401, y=125, color="white", font_size=20, font_name="LiSu")
necessary_txt = Text('Necessary?', x=455, y=125, color="#FFA500", font_size=20, font_name="LiSu")

# K and Kind Text
k_poly = Polygon(410,55, 435,80, 410,105, 385,80, "black")
k_txt = Text('K', x=402, y=70, color="white", font_size=20, font_name="LiSu")
kind_txt = Text('Kind?', x=455, y=70, color="#FFA500", font_size=20, font_name="LiSu")


caption_box = Rectangle(100, 55, 210, 50, "#335599")
media_literacy_txt = Text('Media Literacy', x=118, y=70, color="white", font_size=20, font_name="LiSu")




@repeat
def draw(dt):
    window.show_axis()
    background.draw()
    before_you_txt.draw()
    social_media.draw()
    think_txt.draw()
    is_it_txt.draw()

    t_poly.draw()
    t_txt.draw()
    true_txt.draw()

    h_poly.draw()
    h_txt.draw()
    helpful_txt.draw()

    i_poly.draw()
    i_txt.draw()
    inspiring_txt.draw()
    
    n_poly.draw()
    n_txt.draw()
    necessary_txt.draw()
    
    k_poly.draw()
    k_txt.draw()
    kind_txt.draw()

    caption_box.draw()
    media_literacy_txt.draw()
   

run()
