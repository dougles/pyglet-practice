
import pyglet
from pyglet import gl
from pyglet.gl import *
from random import randint
import math

window = pyglet.window.Window(width=800, height=600, caption='Normal INI', resizable=True)

n = 300
rpts = [(math.cos(2 * math.pi * (i / n)), math.sin(2 * math.pi * (i / n))) for i in range(n)]
pts = [[randint(100, 500), randint(100, 500)] for _ in range(100)]
cpts = [[0,0] for _ in range(100)]
rsteps = [randint(0, 20) for _ in range(100)]
step = 0

def draw_points_gl():
    glBegin(GL_POINTS)
    for p in cpts:
        glVertex2f(p[0], p[1])
    glEnd()
  

@window.event
def on_draw():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    draw_points_gl()

def calculate():
    global step
    for i, _ in enumerate(cpts):
       cpts[i][0] = pts[i][0] + rpts[step][0] * 10.0 #rsteps[i]
       cpts[i][1] = pts[i][1] + rpts[step][1] * 10.0 #rsteps[i]   
       step =  step + 1 if step < 299 else 0


def update(dt):
    calculate()   


pyglet.clock.schedule_interval(update, 5 / 60.0)
pyglet.app.run()
