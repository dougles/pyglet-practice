import pyglet
from pyglet import gl
from pyglet.gl import *
from random import randint

window = pyglet.window.Window(width=800, height=600, caption='Normal INI', resizable=True)

n = 300
pts = [(randint(-100, 600)/1.0, randint(-100, 600)/1.0, randint(1, 100)/1.0) for _ in range(n)]


class ViewPoint:
    def __init__(self):
        self.x = self.y = 0
        self.z = 0
        self.rx = self.ry = self.rz = 50


vp = ViewPoint()


def my_draw():
    pyglet.graphics.draw_indexed(
        4,
        pyglet.gl.GL_TRIANGLES,
        [0, 1, 2, 0, 2, 3],
        ('v2i', (100, 100, 150, 100, 150, 150, 100, 150))
    )
    pyglet.graphics.draw(
        2,
        pyglet.gl.GL_POINTS,
        ('v3f', (10.0, 15.0, 0.0, 30.0, 35.0, 0.0))
    )


def draw_points_gl():
    gl.glLoadIdentity()
    gl.glTranslatef(vp.x, vp.y, vp.z * 3)
    gl.glRotatef(vp.rx - 40, 0, 0, 1)
    gl.glRotatef(vp.ry, 0, 0, 1)
    gl.glRotatef(vp.rz - 40, 0, 0, 1)

    glBegin(GL_LINES)
    d = 600
    nd = -600
    gl.glColor3f(1, 0, 0)
    glVertex3f(nd, 0, 0)
    glVertex3f(d, 0, 0)
    gl.glColor3f(0, 1, 0)
    glVertex3f(0, nd, 0)
    glVertex3f(0, d, 0)
    gl.glColor3f(0, 0, 1)
    glVertex3f(0, 0, nd)
    glVertex3f(0, 0, d)
    glEnd()

    glBegin(GL_POINTS)
    for p in pts:
        gl.glColor3f(0.7, 0.7, 0.7)
        glVertex3f(p[0], p[1], p[2])
    glEnd()


@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    vp.z -= scroll_y / 1.0


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


@window.event
def on_resize(width, height):
    # sets the viewport
    gl.glViewport(0, 0, width, height)

    # sets the projection
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(10.0, width / float(height), 0.1, 100.0)

    # sets the model view
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

    return pyglet.event.EVENT_HANDLED



@window.event
def on_draw():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    draw_points_gl()


pyglet.app.run()
