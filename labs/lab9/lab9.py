"""
Name: Trent Varnes
lab9.py
"""
import math

from graphics import GraphWin, Circle

def addTens(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc += acc + nums[i]
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def writeSumOfSquares():
    ifn = input("enter")
    infile = open(ifn, "r")
    outfile = open("output.txt", "w+")
    for line in infile:
        line = line.split()
        toNumbers(line)
        squareEach(line)
        line = sumList(line)
        outfile.write("Sum of squares = " + str(line))


def starter():
    weights = eval(input("enter players weight: "))
    numWins = eval(input("enter number of wins: "))
    if 150 <= weights < 160 and numWins >= 5:
        print("You're a starter!")
    elif weights > 199 or numWins > 20:
        print("You're a starter!")
    else:
        print("You suck!")


def leapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year + "is a leap year!")
    else:
        print(year + "is not a leap year!")


def circleOverlap():
    win = GraphWin("CircleShift", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2)
    circle1 = Circle(p1, radius1)
    circle1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p4.getX() - p3.getX())**2 + (p4.getY() - p3.getY()) ** 2)
    circle2 = Circle(p3, radius2)
    circle2.draw(win)

    distance = math.sqrt((p3.getX() - p1.getX())**2 + (p3.getY() - p1.getY()) ** 2)

    if distance <= radius1 + radius2:
        print("it over laps")
    else:
        print("it does not over lap")

    win.getMouse()
    win.close()


def main():
    # add other function calls here
    addTens()
    squareEach()
    sumList()
    toNumbers()
    writeSumOfSquares()
    starter()
    leapYear()
    circleOverlap()
    pass


main()
