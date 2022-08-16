import pyglet
from pyglet import gl
from pyglet.gl import *
import math
from random import randint

np = 500
pts = [(math.cos(2 * math.pi * (i / np)), math.sin(2 * math.pi * (i / np))) for i in range(np)]

npts = []
for _ in range(200):
    posini = randint(0, (np-1))
    z = randint(1, 100)
    l = 0
    if z > 50:
        l = randint(10, 11+(-6 * z + 600))
    else:
        l = randint(10, 11+(6 * z))
    a = randint(1, 5) + 50 // (1+l)
    npts.append([posini, l, a, z])




def update_frame(x, y):
    n = len(npts)
    for i in range(n):
        npts[i][0] = npts[i][0] + npts[i][2] if npts[i][0] + npts[i][2] < 499 else 0


class Heightmap:
    def __init__(self):
        # translation and rotation values
        self.x = self.y = 0
        self.z = -250  # heightmap translation
        self.rx = self.ry = self.rz = 0  # heightmap rotation

    def draw(self):
        gl.glLoadIdentity()
        # position (move away 3 times the z_length of the heightmap in the z axis)
        gl.glTranslatef(self.x, self.y, self.z * 3)
        print(self.x, self.y, self.z);
        # rotation
        gl.glRotatef(self.rx - 40, 1, 0, 0)
        gl.glRotatef(self.ry, 0, 1, 0)
        gl.glRotatef(self.rz - 40, 0, 0, 1)
        # color


        # draws the primitives (GL_TRIANGLE_STRIP)

        glBegin(GL_POINTS)

        for k, ip in enumerate(npts):
            c = 0.5 + 0.5 * (1 - ip[1] / 300.0)
            gl.glColor3f(c, c, c)
            glVertex3f(ip[1] * pts[ip[0]][0], ip[1] * pts[ip[0]][1], ip[3])
        glEnd()


# colors
black = (0, 0, 0, 1)
gray = (0.5, 0.5, 0.5)

window = pyglet.window.Window(width=800, height=600, caption='Heightmap', resizable=True)

# background color
gl.glClearColor(*black)

# heightmap
height_map = Heightmap()


@window.event
def on_resize(width, height):
    # sets the viewport
    gl.glViewport(0, 0, width, height)

    # sets the projection
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(60.0, width / float(height), 0.1, 1000.0)

    # sets the model view
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

    return pyglet.event.EVENT_HANDLED


@window.event
def on_draw():
    # clears the background with the background color
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    # draws the heightmap
    height_map.draw()


@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    # scroll the MOUSE WHEEL to zoom
    height_map.z -= scroll_y / 1.0


@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    # press the LEFT MOUSE BUTTON to rotate
    if button == pyglet.window.mouse.LEFT:
        height_map.ry += dx / 5.0
        height_map.rx -= dy / 5.0
    # press the LEFT and RIGHT MOUSE BUTTON simultaneously to pan
    if button == pyglet.window.mouse.LEFT | pyglet.window.mouse.RIGHT:
        height_map.x += dx / 10.0
        height_map.y += dy / 10.0


pyglet.clock.schedule(update_frame, 0.05)
pyglet.app.run()
