from random import random
from pyglet.gl import *

window = pyglet.window.Window()
glClearColor(0, 0, 0, 1)
x = 300
y = 300

def points():
    glBegin(GL_POINTS)
    glVertex2f(x, y)    
    glEnd()

def calculate():    
    global x, y
    rx = round(random())
    ry = round(random())
    x =  x +2 if (rx == 0) else x - 2
    y =  y +2 if (ry == 0) else y - 2   

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    points()


def update(dt):
    calculate()

pyglet.clock.schedule_interval(update, 5 / 60.0)
pyglet.app.run()
