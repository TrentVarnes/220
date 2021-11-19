"""
Trent Varnes
threedoorgame.py
I certify this is my work
"""

from button import Button
from graphics import *
import random

def main():
    win = GraphWin("ThreeDoorGame", 500, 400)
    win.setCoords(0, 0, 12, 10)

    imes = Text(Point(6, 9), "I have a secret door ")
    imes.draw(win)

    message = Text(Point(6, 1), "click to choose my door")
    message.draw(win)

    p1 = Point(1, 7)
    p2 = Point(3, 3)
    shape = Rectangle(p1, p2)
    label = "Door1"
    door1 = Button(shape, label)
    door1.draw(win)

    p3 = Point(5, 7)
    p4 = Point(7, 3)
    shape2 = Rectangle(p3, p4)
    label2 = "Door2"
    door2 = Button(shape2, label2)
    door2.draw(win)

    p5 = Point(9, 7)
    p6 = Point(11, 3)
    shape3 = Rectangle(p5, p6)
    label3 = "Door3"
    door3 = Button(shape3, label3)
    door3.draw(win)

    my_list = [door3, door2, door1]
    button = random.choice(my_list)

    pt = win.getMouse()
    imes.undraw()
    message.undraw()
    won_top = Text(Point(6, 9), "You Won!")
    won_bot = Text(Point(6, 1), "Click to Close")
    lost_top = Text(Point(6, 9), "You Lost!")
    lost_bot = Text(Point(6, 1), button.get_label() + " is my secret door")
    if button.is_clicked(pt):
        button.color_button("green")
        button.set_label("green")
        won_bot.draw(win)
        won_top.draw(win)
    elif door3.is_clicked(pt):
        door3.color_button("red")
        door3.set_label("red")
        lost_bot.draw(win)
        lost_top.draw(win)
    elif door2.is_clicked(pt):
        door2.color_button("red")
        door2.set_label("red")
        lost_bot.draw(win)
        lost_top.draw(win)
    elif door1.is_clicked(pt):
        door1.color_button("red")
        door1.set_label("red")
        lost_bot.draw(win)
        lost_top.draw(win)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
