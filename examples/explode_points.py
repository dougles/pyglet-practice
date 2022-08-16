import pyglet
from pyglet import gl
from pyglet.gl import *
import math
from random import randint, random

gray = (0.5, 0.5, 0.5)
window = pyglet.window.Window(width=800, height=600, caption='Points', resizable=True)
# background color
gl.glClearColor(0, 0, 0, 1)
d = 0.1


def sphere_points(n):
    pts = []
    for i in range(n):
        u = math.pi * 2.0 * random()
        v = math.pi * 2.0 * random()
        x = math.sin(v) + math.cos(u)
        y = math.sin(v) * math.sin(u)
        z = math.cos(v)
        pts.append((z, y, x))

    return pts


pts = sphere_points(150)


class ViewPoint:
    def __init__(self):
        # translation and rotation values
        self.x = self.y = 0
        self.z = -50  # heightmap translation
        self.rx = self.ry = self.rz = 0  # heightmap rotation


vp = ViewPoint()


def translate_rotate():
    gl.glLoadIdentity()
    gl.glTranslatef(vp.x, vp.y, vp.z * 3)
    gl.glRotatef(vp.rx - 40, 1, 0, 0)
    gl.glRotatef(vp.ry, 0, 1, 0)
    gl.glRotatef(vp.rz - 40, 0, 0, 1)


def edges():
    glBegin(GL_LINES)
    d = 100
    gl.glColor3f(0.1, 0.1, 0.1)
    glVertex3f(-d, 0, 0)
    glVertex3f(d, 0, 0)
    gl.glColor3f(0.1, 0.1, 0.1)
    glVertex3f(0, -d, 0)
    glVertex3f(0, d, 0)
    gl.glColor3f(0.8, 0.8, 0.8)
    glVertex3f(0, 0, -d)
    glVertex3f(0, 0, d)
    glEnd()


def draw_arc():
    global d
    glBegin(GL_POINTS)
    k = 10.0 - 0.3 * math.exp(3.5 - d * 0.2)
    for pt in pts:
        c = (10 - d) / 10
        gl.glColor3f(c, c, c)
        glVertex3f(k * pt[0], k * pt[1], k * pt[2])
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
    #edges()
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
    global d
    d += 0.1
    if d > 10:
        d = 0.1


pyglet.clock.schedule_interval(update_frame, 0.05)
pyglet.app.run()
