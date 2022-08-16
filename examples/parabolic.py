from random import random
from pyglet.gl import *
from math import sin, cos, pi

window = pyglet.window.Window()
glClearColor(0, 0, 0, 1)
x = 0
y = 0
t = 0.0 

a = pi / 3.0
v0 = 60.0
h = 10


def points():
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def calculate():
    global t, x, y
    t = t + 0.1
    x = v0 * cos(a) * t 
    y = 50 + v0 * sin(a) * t - 0.5 * 9.81 * t*t 
    if y < 0 :
        t = 0.0


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    points()


def update(dt):
    calculate()


pyglet.clock.schedule_interval(update, 3 / 60.0)
pyglet.app.run()