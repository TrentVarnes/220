"""
Trent Varnes
lab4.py
"""

from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()
    instructions.setText("Click to Close")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    pass
    win = GraphWin("Rectangle", 400, 400)

    p1 = win.getMouse()
    p2 = win.getMouse()
    r = Rectangle(p1, p2)
    r.draw(win)
    length = abs(p1.getX() - p1.getY())
    width = abs(p2.getX() - p2.getY())

    area = length * width
    area_txt = Text(Point(200, 20), "The area is " + str(area))
    area_txt.draw(win)

    perimeter = 2 * (length + width)
    perimeter_txt = Text(Point(200, 40), "The perimeter is " + str(perimeter))
    perimeter_txt.draw(win)

    win.getMouse()
    win.close()


def circle():
    win = GraphWin("circle", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    radius = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    c = Circle(p1, radius)
    c.draw(win)
    radius_txt = Text(Point(200, 390), "The radius is " + str(radius))
    radius_txt.draw(win)
    p1.mo

    win.getMouse()
    win.close()


def pi2():
    n = eval(input("enter terms in series: "))
    sum = 0
    for i in range(n):
        num = 4 * (-1)**i
        den = i *2 + 1
        sum = sum + num / den
    print(math.pi - sum)


def main():
    squares()
    rectangle()

    circle()
    pi2()


main()
