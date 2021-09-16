"""
Name: Trent Varnes
lab3.py
"""

def average():
    grades = eval(input("enter the number of grades here: "))
    total = 0
    for i in range(grades):
        grade = eval(input("enter the grade here: "))
        total = total + grade
    print(total / grades)

if __name__ == '__average__':
    average()

def tip_jar():
    total_tips = 0
    for i in range(5):
        tip = eval(input("enter the tip here: "))
        total_tips += tip
    print(total_tips)

if __name__ == '__tip_jar__':
    tip_jar()

def newton():
    x = eval(input("enter number here: "))
    refine = eval(input("enter number of refines here: "))
    approx = x/2
    for i in range(refine):
        approx = ((approx + x / approx) / 2)
    print(approx)

if __name__ == '__newton__':
    newton()

def sequence():
    series = eval(input("enter number of terms in a series: "))
    for i in range(series):
        y = 1 + ((i +1) // 2 * 2)
        print(y)
if __name__ == '__sequence__':
    sequence()

def pi():
    n = eval(input("enter value for n: "))
    acc = 1
    for i in range(n):
        x = 2 + (i // 2 * 2)
        y = 1 + ((i + 1) // 2 * 2)
        acc = acc * (x / y)
    print(acc * 2)

if __name__ == '__pi__':
    pi()