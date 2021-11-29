"""
Trent Varnes
Lab2.py
"""


import math


def sum_of_threes():
    upper_bound = eval(input("enter upper bound"))
    upper_three = upper_bound // 3
    sum_three = 3 * upper_three * (1 + upper_three) / 2
    print("The sum is", int(sum_three))


def multiplication_table():
    rows = 10
    columns = 10
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            c = i * j
            print("{:2d} ".format(c), end='')
        print("\n")


def triangle_area(a, b, c):
    s = (a + b + c) / 2
    a = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(a)


def sumSquare():
    lower = eval(input("enter lower range: "))
    upper = eval(input("enter upper range: "))
    acc = 1
    for i in range(lower, upper + 1):
        acc = i * i
        print(acc)


def power():
    base = eval(input("enter base: "))
    exponent = eval(input("enter exponent: "))
    acc = 1
    for p in range(exponent):
        acc = acc * base
        print(acc)


def main():
    sum_of_threes()
    multiplication_table()
    triangle_area(3, 4, 5)
    sumSquare()
    power()


if __name__ == '__main__':
    main()
