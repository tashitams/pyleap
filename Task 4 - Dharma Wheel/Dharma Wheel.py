'''
Project: Wheel of Dharma using Pyleap
Author: Kinzang Jigdra
Class: 9 'A'
'''
from pyleap import *

window.set_size(500, 500)
window.set_caption("Wheel of Dharma")

inner_circle = Circle(250, 250, 30, '#FFA500')
outer_circle = Circle(250, 250, 80, '#FFCC03')
inner_circle.line_width = 8
outer_circle.line_width = 15

x1_cord=250
y1_cord=250

# Defining variables to store style properties
fontSize=10
fontFamily="FangSong"
lineColor="#FFFFFF"
textColor="#FFFFFF"


@repeat
def draw(dt):
        inner_circle.stroke()
        outer_circle.stroke()

        # We can DRY this code by using loop.
        # But since loop is not yet covered I've statically assigned the x2 and y2 cordinates.
        
        Line(x1_cord, y1_cord, 250, 350, 10, color=lineColor).draw()
        Text("1. Right View", 215, 365, color=textColor, font_size=fontSize, font_name=fontFamily).draw()
        
        Line(x1_cord, y1_cord, 325, 325, 10, color=lineColor).draw()
        Text("2. Right Thinking", 335, 330, color=textColor, font_size=fontSize, font_name=fontFamily).draw()
        
        Line(x1_cord, y1_cord, 350, 250, 10, color=lineColor).draw()
        Text("3. Right Speech", 360, 245, color=textColor, font_size=fontSize, font_name=fontFamily).draw()
        
        Line(x1_cord, y1_cord, 325, 175, 10, color=lineColor).draw()
        Text("4. Right Action", 340, 170, color=textColor, font_size=fontSize, font_name=fontFamily).draw()
        
        Line(x1_cord, y1_cord, 250, 150, 10, color=lineColor).draw()
        Text("5. Right Livelihood", 200, 130, color=textColor, font_size=fontSize, font_name=fontFamily).draw()
        
        Line(x1_cord, y1_cord, 175, 175, 10, color=lineColor).draw()
        Text("6. Right Deligence", 50, 170, color=textColor, font_size=fontSize, font_name=fontFamily).draw()
        
        Line(x1_cord, y1_cord, 150, 250, 10, color=lineColor).draw()
        Text("7. Right Mindfulness", 15, 245, color=textColor, font_size=fontSize, font_name=fontFamily).draw()
        
        Line(x1_cord, y1_cord, 175, 325, 10, color=lineColor).draw()
        Text("8. Right Concentration", 25, 330, color=textColor, font_size=fontSize, font_name=fontFamily).draw()
         
run()
