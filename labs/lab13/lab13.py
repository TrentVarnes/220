"""
Name: Trent Varnes
lab13.py
"""


from random import randint


def is_in_binary(search, value):
    mid = len(value) // 2
    while search != value[mid] and len(value) != 1:
        if search >= value[mid]:
            value = value[mid:]
        else:
            value = value[:mid]
        mid = len(value) // 2
    if search == value[mid]:
        return True
    return False


def ss(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for x in range(i, len(values)):
            if values[x] < values[lowest]:
                lowest = values[x]
                pos = x
        values[i], values[pos] = values[pos], values[i]


def get_area(rec):
    return randint(1, 100)


def rect_sort(values):
    d = {}
    areas = []
    for rec in values:
        d[get_area(rec)] = rec
        areas.append(get_area(rec))
    ss(areas)
    for i in range(len(areas)):
        values[i] = d[areas[i]]
    print(areas)


def trades(filename):
    infile = open(filename, "r")
    data = infile.read().split()
    for i in range(len(data)):
        if 500 < int(data[i]) < 830:
            print(i + 1, "warning")
        elif int(data[i]) > 830:
            print(i + 1, "alert")


def main():
    # add other function calls here
    is_in_binary(1, [1, 2, 3])
    trades("trades.txt")
    pass


main()
