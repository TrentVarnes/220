"""
Trent Varnes
bumper.py
I certify this is my work
"""

from random import randint
from graphics import *
import math
import time

def bumper():
    win = GraphWin("Bumpers", 500, 400)
    win.setBackground("green")
    p1 = win.getMouse()
    radius = 25
    ball = Circle(p1, radius)
    ball.setFill("red")
    ball.draw(win)
    dx = randint(-5, 5)
    dy = randint(-5, 5)

    p2 = win.getMouse()
    radius2 = 25
    ball2 = Circle(p2, radius2)
    ball2.setFill("blue")
    ball2.draw(win)

    yFloor = radius
    yCeiling = win.getHeight() - radius
    xFloor = radius
    xCeiling = win.getWidth() - radius

    yFloor1 = radius2
    yCeiling1 = win.getHeight() - radius2
    xFloor1 = radius2
    xCeiling1 = win.getWidth() - radius2

    dx1 = randint(-5, 5)
    dy1 = randint(-5, 5)

    distance = math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2)

    while True:
        update(60)
        #time.sleep(.001)
        ball.move(dx, dy)
        ball2.move(dx1, dy1)
        if ball.getCenter().getY() <= yFloor or ball.getCenter().getY() >= yCeiling:
            dy = -dy
        elif ball.getCenter().getX() <= xFloor or ball.getCenter().getX() >= xCeiling:
            dx = -dx
        elif ball2.getCenter().getY() <= yFloor1 or ball2.getCenter().getY() >= yCeiling1:
            dy1 = -dy1
        elif ball2.getCenter().getX() <= xFloor1 or ball2.getCenter().getX() >= xCeiling1:
            dx1 = -dx1
        elif win.checkMouse() != None:
            break

    win.close()
def main():
    bumper()
    pass

if __name__ == '__main__':
    main()
