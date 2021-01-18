"""''''''''''''''''''''''''''''''''
+++++++++++++++++++++++++++++++++++
|         Thukten Norzang         |
|           Class 9D              |
|       Buli Central School       |
+++++++++++++++++++++++++++++++++++
''''''''''''''''''''''''''''''''"""

from pyleap import*

window.set_caption("Beatiful Chorten")
window.set_size(600,600)

base_rect = Rectangle(96,0,300,40,"white")
rect1 = Rectangle(120,41,250,20,"white")
rect2 = Rectangle(130,62,230,20,"white")
rect3 = Rectangle(140,83,210,20,"white")
rect4 = Rectangle(160,104,165,60,"white")
rect5 = Rectangle(140,165,205,20,"white")
rect6 = Rectangle(130,186,226,20,"white")
rect7 = Rectangle(143,207,198,20,"white")
rect8 = Rectangle(163,228,158,20,"white")
poly_1 = Polygon(180,249,304,249,320,320,160,320,"white")
poly_2 = Polygon(210,321,270,321,255,420,227,420,"white")
elli_1 = Ellipse(241,420,35,15,"yellow")
poly_3 = Polygon(228,421,253,421,248,456,233,456,"yellow")
yellow_circle = Circle(x=241, y=470, r=24, color="yellow")
black_circle = Circle(x=241, y=480, r=16, color="black")
white_circle = Circle(x=241, y=485, r=10, color="white")
white_moon = Circle(x=460, y=503, r=40, color="white")
black_moon = Circle(x=477, y=515, r=33, color="black")

def draw(dt):
    #window.show_axis()
    base_rect.draw()
    rect1.draw()
    rect2.draw()
    rect3.draw()
    rect4.draw()
    rect5.draw()
    rect6.draw()
    rect7.draw()
    rect8.draw()
    poly_1.draw()
    poly_2.draw()
    elli_1.draw()
    poly_3.draw()
    yellow_circle.draw()
    black_circle.draw()
    white_circle.draw()
    white_moon.draw()
    black_moon.draw()

repeat(draw)
run()
