from asciimatics.screen import ManagedScreen
from asciimatics.screen import Screen
from asciimatics.screen import ManagedScreen

import math
from time import sleep
from array import *

with ManagedScreen() as screen:
    xSize = screen.width
    ySize = screen.height

x0 = 0 # Центр
y0 = 0

deg1 = math.pi / 180

def sqr3d(z, dist):
    for i in range(4):
        kx = xSize/2 + d1[0][i]*dist/(z + dist)
        sx.append(kx)
        ky = ySize/2 - d1[1][i]*dist/(z + dist)
        sy.append(ky)
    s.append(sx)
    s.append(sy)
    return s

def sqr(r, angl):
    alpha = 0
    for i in range(4):
        x.append(x0 + r*math.cos((alpha + angl)*deg1))
        alpha += 90
    d1.append(x)

    for i in range(4):
        y.append(y0 + r*math.sin((alpha + angl)*deg1))
        alpha += 90
    d1.append(y)

@ManagedScreen
def sqrRend(xx, yy, screen=None):
    screen.fill_polygon([[(xx[0], yy[0]), (xx[1], yy[1]), (xx[2], yy[2]), (xx[3], yy[3])]])
    screen.refresh()
    sleep(0.2)

l = 0
k = 1
while l < 90:
    d1 = []
    x = []
    y = []
    s = []
    sx = []
    sy = []

    sqr(30, l)
    sqrRend(sqr3d(k, 3)[0], sqr3d(k, 3)[1])
    l += 5
    k += 2
