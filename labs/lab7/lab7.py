"""
Name: Trent Varnes
Partner:
lab7.py
"""
import math


def main():
    this = input("")


def cash_conversion():
    pre_dollar = eval(input("enter a integer: "))
    print("{:2f}".format(pre_dollar))


def encode():
    message = input("enter message here: ")
    k_value = eval(input("enter key value here: "))
    acc = ""
    for c in message:
        i = ord(c)
        added = k_value + i
        c = chr(added)
        acc += c
    print(acc)


def sphere_area(radius):
    area = 4 * math.pi * radius**2
    return area


def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume


def sum_n(n):
    acc = 0
    for i in range(n):
        acc += i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc += i**3
    return acc


def encode_better():
    message = input("enter some message: ")
    key = input("enter some key: ")
    acc = ""
    for i in range(len(message)):
        c = message[i]
        key1 = key[i % len(key)]
        c = ord(c)
        key2 = ord(key1) - 97
        add = key2 + c
        c = chr(add)
        acc += c
    print(acc)


    pass
if __name__ == '__main__':
    #encode()
    #print(sphere_area(3))
    #print(sphere_volume(5))
    #sum_n()
    #sum_n_cubes()
    encode_better()
    main()
