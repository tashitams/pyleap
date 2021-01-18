from pyleap import *

window.set_size(700,700)
window.set_caption("Time is Money")

clock = Circle(350,350,150,"black")
second_hand = Rectangle(348,350,4,130,"white")
second_hand.set_anchor(350,350)

minute_hand = Rectangle(348,350,4,100,"white")
minute_hand.set_anchor(350,350)


center = Circle(350,350,10,"white")
text_1= Text("12",338,480,font_size=18,color="white",font_name="Bauhaus 93")
text_2= Text("6",349,205,font_size=18,color="white",font_name="Bauhaus 93")
text_3= Text("3",485,340,font_size=18,color="white",font_name="Bauhaus 93")
text_4= Text("9",205,340,font_size=18,color="white",font_name="Bauhaus 93")
text_5= Text("2",463,410,font_size=18,color="white",font_name="Bauhaus 93")
text_6= Text("1",410,460,font_size=18,color="white",font_name="Bauhaus 93")
text_7= Text("4",463,270,font_size=18,color="white",font_name="Bauhaus 93")
text_8= Text("5",410,225,font_size=18,color="white",font_name="Bauhaus 93")
text_9= Text("11",275,460,font_size=18,color="white",font_name="Bauhaus 93")
text_10= Text("10",225,410,font_size=18,color="white",font_name="Bauhaus 93")
text_11= Text("8",225,270,font_size=18,color="white",font_name="Bauhaus 93")
text_12= Text("7",275,225,font_size=18,color="white",font_name="Bauhaus 93")
text_13 = Text("Time",260,520,font_size=50,color="red",font_name="Cooper Black")
text_14 = Text("'Is Money'.", 260,160,font_size=28,color="red",font_name="Cooper Black")
text_15 = Text("– Benjamin Franklin", 220,120,font_size=18,color="black",font_name="Cooper Black")

bg = Rectangle(0,0,window.w,window.h,'#D0D5D2')
clock_tick = Audio("assets/sound/clock.mp3", loop=True)


def draw(dt):
    global speed
    window.clear()
    clock_tick.play()
    bg.draw()
    clock.draw()
    second_hand.draw()
    second_hand.rotation -= 0.2
    
    minute_hand.draw()
    minute_hand.rotation -=0.0027
    
    center.draw()
    text_1.draw()
    text_2.draw()
    text_3.draw()
    text_4.draw()
    text_5.draw()
    text_6.draw()
    text_7.draw()
    text_8.draw()
    text_9.draw()
    text_10.draw()
    text_11.draw()
    text_12.draw()
    text_13.draw()
    text_14.draw()
    text_15.draw()
   
    
repeat(draw)
run()
    
    
