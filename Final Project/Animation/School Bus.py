from pyleap import *


window.set_caption("School Bus")
window.set_size(900,700)

black_top = Rectangle(0,0,900,200,"black")
bus = Polygon(150,150,850,150,850,345,840,550,230,550,150,350,150,150,"green")

wheel_1 = Circle(270,130,70,"black")
wheel_x = Circle(270,130,60,"black")
wheel_y = Circle(270,130,15,"white")
wheel_z = Circle(270,130,60,"white")
wheel_z.line_width=10
wheel_w = Circle(270,130,40,"white")

spoke_1 = Rectangle(265, 130, 10, 55, "white")
spoke_1.set_anchor(270, 130)
spoke_1.rotation = -0

spoke_2 = Rectangle(265, 130, 10, 55, "white")
spoke_2.set_anchor(270, 130)
spoke_2.rotation = -72

spoke_3 = Rectangle(265, 130, 10, 55, "white")
spoke_3.set_anchor(270, 130)
spoke_3.rotation = -144

spoke_4 = Rectangle(265, 130, 10, 55, "white")
spoke_4.set_anchor(270, 130)
spoke_4.rotation = -218

spoke_5 = Rectangle(265, 130, 10, 55, "white")
spoke_5.set_anchor(270, 130)
spoke_5.rotation = -290

pump = Ellipse(270,160,30,15,"red")
pump.set_anchor(270, 130)


wheel_a = Circle(700,130,70,"black")
wheel_b = Circle(700,130,60,"black")
wheel_c = Circle(700,130,15,"white")
wheel_d = Circle(700,130,60,"white")
wheel_d.line_width=10
wheel_e = Circle(700,130,40,"white")



spoke_6 = Rectangle(695, 130, 10, 55, "white")
spoke_6.set_anchor(700, 130)
spoke_6.rotation = -0

spoke_7 = Rectangle(695, 130, 10, 55, "white")
spoke_7.set_anchor(700, 130)
spoke_7.rotation = -72

spoke_8 = Rectangle(695, 130, 10, 55, "white")
spoke_8.set_anchor(700, 130)
spoke_8.rotation = -144

spoke_9 = Rectangle(695, 130, 10, 55, "white")
spoke_9.set_anchor(700, 130)
spoke_9.rotation = -218

spoke_10 = Rectangle(695, 130, 10, 55, "white")
spoke_10.set_anchor(700, 130)
spoke_10.rotation = -290

pump_1 = Ellipse(700,160,30,15,"red")
pump_1.set_anchor(700, 130)

bus_design = Rectangle(150,165,700,180,"yellow")
bus_design_1 = Circle(180,205,25,"red")
bus_design_2 = Circle(180,260,15,"red")

bus_design_3 = Circle(805,205,35,"red")
bus_design_4 = Circle(805,260,18,"red")
bus_design_5 = Circle(180,315,25,"white")
bus_design_6 = Rectangle(500,330,340,10,"black")
bus_design_7 = Rectangle(500,310,340,10,"black")

door = Rectangle(335,185,150,340,"#fff")
door.line_width = 5

door_2 = Rectangle(410,185,75,340,"#fff")
door_2.line_width = 5

door_1 = Rectangle(335,185,150,340,"#383838")

door_handle = Ellipse(385,355,15,50,"white")
door_handle.line_width = 3

door_handle_hider = Rectangle(387,305,20,100,"#383838")

door_handle_1 = Ellipse(435,355,15,50,"white")
door_handle_1.line_width = 3

door_handle_hider_1 = Rectangle(413,305,20,100,"#383838")

diver_window = Polygon(170,355,320,355,320,525,240,525,170,355,'white')

window_1 = Rectangle(500,355,120,170,"white")
window_1.line_width = 7
window_1_inner = Rectangle(500,355,120,170,"red")

window_2 = Rectangle(640,355,120,170,"white")
window_2.line_width = 7
window_2_inner = Rectangle(640,355,120,170,"red")

roader = Rectangle(25,75,80,30,'white')
roader_1 = Rectangle(155,75,80,30,'white')
roader_2 = Rectangle(285,75,80,30,'white')
roader_3 = Rectangle(415,75,80,30,'white')
roader_4 = Rectangle(545,75,80,30,'white')
roader_5 = Rectangle(675,75,80,30,'white')
roader_6 = Rectangle(805,75,80,30,'white')

tree_1 = Rectangle(55,200,20,50,"brown")
tree_2 =  Polygon(10,285,120,285,65,330,"green")
tree_3 =  Polygon(25,310,105,310,65,370,"green")
tree_4 =  Polygon(5,250,125,250,65,340,"green")

name = Text("School Bus", x=500, y=265, font_size=40, color="red", font_name="Cooper Black ")
bg = Rectangle(0,0,900,700,"#63C5DA")

load_pole = Rectangle(280,550,560,10,"gray")
load_pole_1 = Rectangle(280,550,10,60,"gray")
load_pole_2 = Rectangle(830,550,10,60,"gray")
load_pole_3 = Rectangle(280,600,560,10,"gray")
load_pole_4 = Rectangle(460,550,10,60,"gray")
load_pole_5 = Rectangle(660,550,10,60,"gray")

load = Ellipse(560,550,270,75,"orange")

sun = Circle(60,650,30,"yellow")

diver_head = Circle(275,455,20,"black")

bus_sound = Audio("assets/sound/bus.mp3", loop=True)

def draw(dt):
    window.clear()
    window.show_axis()
    bg.draw()
    bus_sound.play()

    sun.x += .09
    if sun.x > 900:
        sun.x = 0
    
    
    sun.draw()

    
    

    tree_1.x += 6
    tree_2.x += 6
    tree_3.x += 6
    tree_4.x += 6

    if tree_1.x > 900:
        tree_1.x = 0
        
    if tree_2.x > 900:
        tree_2.x = 0

    if tree_3.x > 900:
        tree_3.x = 0

    if tree_4.x > 900:
        tree_4.x = 0

    
    tree_1.draw()
    tree_2.draw()
    tree_3.draw()
    tree_4.draw()
    
    black_top.draw()
    load.draw()
    bus.draw()
    bus_design.draw()
    bus_design_1.draw()
    bus_design_2.draw()
    
    bus_design_3.draw()
    bus_design_4.draw()
    bus_design_5.draw()
    bus_design_6.draw()
    bus_design_7.draw()

    

    

    load_pole.draw()
    load_pole_1.draw()
    load_pole_2.draw()
    load_pole_3.draw()
    load_pole_4.draw()
    load_pole_5.draw()


    
    door_1.draw()
    door.stroke()
    door_2.stroke()

    door_handle.stroke()
    door_handle_hider.draw()

    door_handle_1.stroke()
    door_handle_hider_1.draw()

    diver_window.draw()
    
    window_1_inner.draw()
    window_1.stroke()

    window_2_inner.draw()
    window_2.stroke()

   
    roader.x += 5
    roader_1.x += 5
    roader_2.x += 5
    roader_3.x += 5
    roader_4.x += 5
    roader_5.x += 5
    roader_6.x += 5

    if roader_6.x > 900:
        roader_6.x = 0
        
    if roader_5.x > 900:
        roader_5.x = 0

    if roader_4.x > 900:
        roader_4.x = 0
        
    if roader_3.x > 900:
        roader_3.x = 0
        
    if roader_2.x > 900:
        roader_2.x = 0
        
    if roader_1.x > 900:
        roader_1.x = 0

    if roader.x > 900:
        roader.x = 0

    
    
    roader.draw()
    roader_1.draw()
    roader_2.draw()
    roader_3.draw()
    roader_4.draw()
    roader_5.draw()
    roader_6.draw()
    
   
    wheel_1.draw()
    wheel_x.draw()
    wheel_y.draw()
    wheel_z.stroke()
    wheel_w.stroke()

    pump.draw()
    
    spoke_1.draw()
    spoke_2.draw()
    spoke_3.draw()
    spoke_4.draw()
    spoke_5.draw()

    pump.rotation += 5
    spoke_1.rotation += 5
    spoke_2.rotation += 5
    spoke_3.rotation += 5
    spoke_4.rotation += 5
    spoke_5.rotation += 5

    

    wheel_a.draw()
    wheel_b.draw()
    wheel_c.draw()
    wheel_d.stroke()
    wheel_e.stroke()

    pump_1.draw()
    spoke_6.draw()
    spoke_7.draw()
    spoke_8.draw()
    spoke_9.draw()
    spoke_10.draw()

    pump_1.rotation += 5
    spoke_6.rotation += 5
    spoke_7.rotation += 5
    spoke_8.rotation += 5
    spoke_9.rotation += 5
    spoke_10.rotation += 5

    #diver_head.draw()
    
    

    
   
    
    
   

    name.draw()


repeat(draw)
run()



