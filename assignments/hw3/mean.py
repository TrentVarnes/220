"""
Trent Varnes
Mean.py
problem:
Certification of authenticity
I certify this is my work
"""

# Program will calculate the RMS average, Harmonic mean, and Geometric mean

import math


def main():
    numb = int(input("enter the amount of numbers here: "))
    har_acc = 0
    geo_acc = 1
    rms_acc = 0
    list_1 = []
    for numb_range in range(numb):
        #rms
        numb_value = float(input("enter the value for the numbers here: "))
        squarer = numb_value**2
        rms_acc += squarer

       #harmonic mean
        division = 1 / numb_value
        har_acc += division
        #geometric mean
        list_1.append(numb_value)
        geo_acc = geo_acc * numb_value

    average = rms_acc / numb
    rms_average = round(math.sqrt(average), 3)
    har_m = round(numb / har_acc, 3)
    geo_m = round(geo_acc ** (1 / numb), 3)

    print(float(rms_average))
    print(float(har_m))
    print(float(geo_m))


if __name__ == '__main__':
    main()
