"""
Trent Varnes
Mean.py
problem:
Certification of authenticity
I certify this is my work
"""

#Program will calculate the RMS average, Harmonic mean, and Geometric mean

import math

def main():
    numb = eval(input("enter the amount of numbers here: "))
    total = 0
    for numb_value in range(numb):
        numb_value = eval(input("enter the value for the numbers here: "))
        total = total + numb_value**2
    rms_average = math.sqrt(total / numb)
    print("rms average", round(rms_average, 3))


    amount = eval(input("enter the amount of numbers here: "))
    total1 = 0
    for value in range(amount):
        value = eval(input("enter the value of the numbers: "))
        total1 = total1 + 1 / value
    har_m = float(amount / total1)
    print("The harmonic mean is", har_m)


    amount_o = eval(input("enter the amount of numbers here: "))
    product = 1
    for value_o in range(amount_o):
        value_o = eval(input("enter the value of the number here: "))
        product = product * value_o
        geo_m = (product)**(1 / amount_o)
    print(round(geo_m, 1))

if __name__ == '__main__':
    main()
