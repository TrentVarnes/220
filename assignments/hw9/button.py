"""
Trent Varnes
"""

from graphics import *


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.label = label
        self.text = None

    def get_label(self):
        return self.label

    def draw(self, win):
        self.text = Text(self.shape.getCenter(), self.label)
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        p1 = self.shape.getP1()
        p2 = self.shape.getP2()
        w = abs(p1.getX() - p2.getX())
        h = abs(p1.getY() - p2.getY())
        x = Point.getX(point)
        y = Point.getY(point)
        xc = (p1.getX() + p2.getX()) / 2
        dx = abs(xc - x)
        yc = (p1.getY() + p2.getY()) / 2
        dy = abs(yc - y)
        if dx <= w/2 and dy <= h/2:
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.label = label
