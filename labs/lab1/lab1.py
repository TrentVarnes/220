"""
Name: Trent Varnes
lab1.py

Problem: This function calculates the area of a rectangle
"""

def calc_rec_area():
    length = eval(input("enter the length: "))
    width = eval(input("enter the width: "))
    area = length * width
    print("area =", area)

def calc_volume():
    length = eval(input("enter the length: "))
    width = eval(input("enter the width: "))
    height = eval(input("enter the height: "))
    volume = length * width * height
    print("volume =", volume)

def shooting_percentage():
    total_shots = eval(input("enter total shots here: "))
    shots_made = eval(input("enter shots made here: "))
    shooting_percentage = shots_made / total_shots * 100
    print("shooting_percentage =", shooting_percentage)

def coffee():
    coffee = 10.50
    shipping = 0.86
    fixed_cost = 1.50
    coffee_purchased = eval(input("enter amount of coffee purchased: "))
    total_cost = coffee_purchased * coffee + coffee_purchased * shipping + fixed_cost
    print("total_cost =", total_cost)

def kilometers_to_miles():
    kilometers_driven = input(eval("enter kilometers driven: "))
    kilometers_to_miles = kilometers_driven / 1.61
    print("kilometers_to_miles =", kilometers_to_miles)








