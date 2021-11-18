"""
Name: Trent Varnes
lab12.py
"""

from random import randint

def find_and_remove_first(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Trent"
    except:
        pass


def read_data(filename):
    file = open(filename, "r")
    data = file.read()
    data.split()
    i = 0
    while i < len(data):
        data[i] = int(data[i])
        i += 1
    return data


def search(lst, value):
    i = 0
    while i < len(lst):
        if value == lst[i]:
            return True
        i += 1
    return False


def good_input():
    x = eval(input("enter num 1-10: "))
    while not (0 < x < 11):
        x = eval(input("enter num 1-10"))
    return x


def num_digits():
    num = eval(input("enter positive integer: "))
    while num > 0:
        digits = 0
        while digits > 0:
            num //= 10
            digits += 1
        print(digits)
        num = eval(input("enter positive integer: "))


def hi_lo_game():
    num = randint(1, 100)
    guesses = 0
    guess = eval(input("enter your guess: "))
    while guesses != 7 and guess != num:
        if guess > num:
            print("guess is too high: ")
        elif guess < num:
            print("guess is too low: ")
        guesses += 1
        guess = eval(input("enter guest"))
    if guess != num and guesses > 7:
        print("you lost the number was " + str(num))
    else:
        print("you won in " + str(guesses) + " guesses the " + "number was " + str(num))



def main():
    # add other function calls here
    hi_lo_game()
    pass


main()
