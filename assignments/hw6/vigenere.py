"""
Trent Varnes
vigenere.py
I certify this is my work
"""

from graphics import *


def code(message, keyword):
    win = GraphWin("Vigenere", 500, 400)
    win.getMouse()

    messages = Text(Point(125, 50), "Message to Code")
    messages.draw(win)
    key1 = Text(Point(125, 100), "Enter Keyword")
    key1.draw(win)

    message_box = Entry(Point(290, 50), 20)
    message_box.draw(win)
    keyword_box = Entry(Point(250, 100), 10)
    keyword_box.draw(win)

    button_text = Text(Point(250, 150), "Encode")
    button_outline = Rectangle(Point(200, 175),  Point(300, 125))
    button_text.draw(win)
    button_outline.draw(win)

    win.getMouse()
    button_text.undraw()
    button_outline.undraw()

    #cipher
    message1 = message
    message1 = message1.upper()
    new_mess = "".join(message1.split())
    keyword1 = keyword
    key1 = keyword1.upper()
    key_int = [ord(i) for i in key1]
    key_length = len(key1)
    message_int = [ord(i) for i in new_mess]
    acc = ""
    for i in range(len(message_int)):
        value = (message_int[i] + key_int[i % key_length]) % 26
        acc += chr(value + 65)

    # output
    result_message = Text(Point(250, 250), "Resulting Message")
    result = Text(Point(250, 275), acc)
    close_message = Text(Point(250, 380), "Click Anywhere to Close Window")
    result_message.draw(win)
    result.draw(win)
    close_message.draw(win)

    win.getMouse()
    win.close()
def main():
    code("this program will be great", "python")

main()
