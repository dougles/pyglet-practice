import pyglet
from pyglet import gl
from pyglet.gl import *
import numpy as np
import math
from random import randint, random


gray = (0.5, 0.5, 0.5)
window = pyglet.window.Window(width=800, height=600, caption='Points', resizable=True)
# background color
gl.glClearColor(0, 0, 0, 1)
poss = [99]


def arc_points(w, h, ang):
    return [((w + w * math.cos(math.pi * (float(i) / 100.0))) * math.cos(math.pi * ang),
             (w + w * math.cos(math.pi * (float(i) / 100.0))) * math.sin(math.pi * ang),
             h * math.sin(math.pi * (float(i) / 100.0))) for i in range(100)]


arc = arc_points(10, 50, 0.0)
arcs = [arc]

class ViewPoint:
    def __init__(self):
        # translation and rotation values
        self.x = self.y = 0
        self.z = -50  # heightmap translation
        self.rx = self.ry = self.rz = 0  # heightmap rotation


vp = ViewPoint()


def translate_rotate():
    gl.glLoadIdentity()
    #position (move away 3 times the z_length of the heightmap in the z axis)
    gl.glTranslatef(vp.x, vp.y, vp.z * 3)
    #print(vp.x, vp.y, vp.z)
    #rotation
    gl.glRotatef(vp.rx - 40, 1, 0, 0)
    gl.glRotatef(vp.ry, 0, 1, 0)
    gl.glRotatef(vp.rz - 40, 0, 0, 1)


def edges():
    glBegin(GL_LINES)
    d = 100
    nd = -d
    gl.glColor3f(0.1, 0.1, 0.1)
    glVertex3f(nd, 0, 0)
    glVertex3f(d, 0, 0)
    gl.glColor3f(0.1, 0.1, 0.1)
    glVertex3f(0, nd, 0)
    glVertex3f(0, d, 0)
    #gl.glColor3f(0.8, 0.8, 0.8)
    #glVertex3f(0, 0, nd)
    #glVertex3f(0, 0, d)
    glEnd()


def draw_arc():
    global poss
    global arcs

    print(poss)
    if poss[0] < 0:
        poss.pop(0)
        arcs.pop(0)

    glBegin(GL_POINTS)
    for k, p in enumerate(poss):
        pt = arcs[k][p]
        c = float(p+1) / 100.0
        gl.glColor3f(c, c, c)
        glVertex3f(pt[0], pt[1], pt[2])
    glEnd()


@window.event
def on_resize(width, height):
    # sets the viewport
    gl.glViewport(0, 0, width, height)
    # sets the projection
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(45.0, width / float(height), 0.1, 2000.0)
    # sets the model view
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

    return pyglet.event.EVENT_HANDLED


@window.event
def on_draw():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    translate_rotate()
    edges()
    draw_arc()


@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    vp.z -= scroll_y * 2.0


@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    # press the LEFT MOUSE BUTTON to rotate
    if button == pyglet.window.mouse.LEFT:
        vp.ry += dx / 5.0
        vp.rx -= dy / 5.0
    # press the LEFT and RIGHT MOUSE BUTTON simultaneously to pan
    if button == pyglet.window.mouse.LEFT | pyglet.window.mouse.RIGHT:
        vp.x += dx / 10.0
        vp.y += dy / 10.0


def update_frame(dt):
    global poss
    for k, _ in enumerate(poss):
        poss[k] -= 1
    if randint(1, 20) % 3 == 0:
        w = randint(10, 40)
        h = randint(30, 60)
        angle = random() * 2.0
        arcs.append(arc_points(w, h, angle))
        poss.append(99)


pyglet.clock.schedule_interval(update_frame, 0.05)
pyglet.app.run()
