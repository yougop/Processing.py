# add Sliders with controlP5 to your processing.py sketches

from controlP5 import ControlP5
from controlP5 import Slider

val_slider = 50; color_slider = 255

def my_listener( my_input ): 
    global val_slider, color_slider
    if my_input.getName() == 'my slider':
        val_slider = int( my_input.getValue() )
        print ("Size: " + str( val_slider ) )
    if my_input.getName() == 'my color':
        color_slider = int( my_input.getValue() )
        print ("Color: " + str( color_slider ) )   

def setup():
    size(700, 400)
    noStroke()    
    
    cp5 = ControlP5(this)  
         
    cp5.addSlider("my slider").setPosition(100,50).setSize(300, 20).setRange(0,255).setValue(100).addListener( my_listener )
    cp5.getController("my slider").setFont(createFont("does not matter", 20))
    
    cp5.addSlider("my color").setPosition(100,100).setSize(125, 10).setRange(0,255).addListener( my_listener )
    
    cp5.addSlider("lorem ipsum").setPosition(100,115).setSize(125, 10).setRange(0,255).addListener( my_listener )
    cp5.getController("lorem ipsum").getValueLabel().align(ControlP5.LEFT, ControlP5.BOTTOM_OUTSIDE).setPaddingX(0)
    cp5.getController("lorem ipsum").getCaptionLabel().align(ControlP5.RIGHT, ControlP5.BOTTOM_OUTSIDE).setPaddingX(0)

def draw():
    global val_slider; color_slider
    background(60)
    fill(255-color_slider, 0, color_slider)
    ellipse(width/3*2, height/3*2-30, val_slider, val_slider)
    
