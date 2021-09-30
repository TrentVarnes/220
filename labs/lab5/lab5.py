"""
Name: Trent Varnes
lab5.py
"""
import math

from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    triangle1 = Polygon(p1, p2, p3)
    triangle1.draw(win)
    a = math.sqrt((p1.getX() - p2.getX())**2 + (p1.getY() - p2.getY())**2)
    b = math.sqrt((p2.getX() - p3.getX())**2 + (p2.getY() - p3.getY())**2)
    c = math.sqrt((p1.getX() - p3.getX())**2 + (p1.getY() - p3.getY())**2)
    perimeter = a + b + c
    perimeter_text = Text(Point(200, 390), "The perimeter is: " + str(perimeter))
    perimeter_text.draw(win)
    s = (a + b + c) // 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    area_text = Text(Point(200, 370), "The area is: " + str(area))
    area_text.draw(win)


    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    #all code here
    red_box = Entry(Point(win_height / 2 - 50, win_width / 2 + 40), 5)
    red_box.draw(win)
    green_box = Entry(Point(win_height / 2 - 50, win_width / 2 + 70), 5)
    green_box.draw(win)
    blue_box = Entry(Point(win_height / 2 - 50, win_width / 2 + 100), 5)
    blue_box.draw(win)
    for _ in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    string1 = input("enter a string ")
    print(string1[0])
    print(string1[-1])
    print(string1[2:6])
    print(string1[:])
    print(string1[0:4] * 10)
    for c in string1:
        print(c)
    print(len(string1))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], pt]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[3], float(values[5])]
    print(x)
    x =values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def main():
    target()
    triangle()
    color_shape()
    process_string()
    process_list()
    pass


main()
