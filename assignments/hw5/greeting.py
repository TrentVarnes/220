"""
Trent Varnes
greeting.py
I certify this is my work
"""
import time

from graphics import GraphWin, Point, Polygon, Text, Rectangle



def main():
    width = 400
    height = 400
    win = GraphWin("greeting", width, height)
    a = Point(200, 250)
    b = Point(150, 175)
    c = Point(165, 150)
    d = Point(190, 150)
    e = Point(200, 160)
    f = Point(210, 150)
    g = Point(235, 150)
    h = Point(250, 175)
    shape = Polygon(a, b, c, d, e, f, g, h)
    shape.setFill("red")
    win.getMouse()
    shape.draw(win)

    message = Text(Point(200, 380), "Happy Valentines Day!")
    win.getMouse()
    message.draw(win)
    win.getMouse()
    message.undraw()

    win.getMouse()
    p1 = Point(12, 184)
    p2 = Point(9, 180)
    p3 = Point(1, 180)
    p4 = Point(4, 184)
    p5 = Point(1, 188)
    p6 = Point(9, 188)
    arrow_head = Polygon(Point(175, 188), Point(175, 180), Point(184, 184))
    arrow_tail = Polygon(p1, p2, p3, p4, p5, p6)
    arrow = Rectangle(Point(12, 185), Point(175, 184))
    arrow_tail.draw(win)
    arrow_head.draw(win)
    arrow.draw(win)
    for _ in range(10):
        arrow.move(41, 1)
        arrow_head.move(41, 1)
        arrow_tail.move(41, 1)
        time.sleep(0.1)

    win.getMouse()
    message2 = Text(Point(200, 380), "Click anywhere to close!")
    message2.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
