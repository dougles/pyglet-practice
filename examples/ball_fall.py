from random import random
from pyglet.gl import *
from pyglet import shapes

window = pyglet.window.Window(900, 700)
glClearColor(0, 0, 0, 1)

x = 50
y = 0
t = 0.0
v = 0
h = 500
fall = True

def draw_ball():
    circle = shapes.Circle(x, y, 5, color=(90, 225, 30))
    circle.draw()


def calculate():
    global t, x, y, fall, h, v
    t = t + 0.2
    x = x + 1 if x < 600 else 50
    vf = 0
    yy = 0

    if fall :
        y = h - 0.5 * 9.81 * t * t        
    else :
        y = v * t - 0.5 * 9.81* t * t
        vf = v - 9.8 * t # to check if final speed is zero   
    
    if y < 1:
        v = 9.81 * t * 0.85 # speed ini when it rises 0.85 -> reduces every time
        fall = False
        t = 0
    if vf < 0 :
        fall = True
        t = 0
        h = y
    

@window.event
def on_draw():
    window.clear()
    draw_ball()


def update(dt):
    calculate()


pyglet.clock.schedule_interval(update, 2 / 60.0)
pyglet.app.run()