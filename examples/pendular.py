from random import random
from pyglet.gl import *
from pyglet import shapes
from math import sqrt, sin, cos, atan

window = pyglet.window.Window(900, 700)

glClearColor(0, 0, 0, 1)
x = 50
y = 0
t = 0.0
ang0 = 0.7853
g = 9.81
length = 150

def draw_ball():
    circle = shapes.Circle(x, y, 5, color=(90, 225, 30))
    circle.draw()


def calculate():
    global t, x, y 
    t = t + 0.25
    
    ang = ang0 * cos(sqrt(g / length)*t + 1.0)

    x = 200 + length *  sin(ang);
    y = 200 - length *  cos(ang);
    

@window.event
def on_draw():
    window.clear()
    draw_ball()    


def update(dt):
    calculate()


pyglet.clock.schedule_interval(update, 2 / 60.0)
pyglet.app.run()