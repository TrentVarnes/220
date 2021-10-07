"""
Name: Trent Varnes
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("first last")
    name_rev = name.split()
    print(name_rev[1] + "," + name_rev[0])


def company_name():
    company = input("three part name")
    company_split = company.split(".")
    print(company_split[1])


def initials():
    names = eval(input("names in class"))
    for i in range(names):
        first = input("enter first name")
        last = input("enter last name")
        print("initials are " + first[0] + last[0])


def names():
    names = input("list of names first and last separated by commas")
    name_split = names.split(",")
    for name in name_split:
        parts = name.split()
        print(parts[0][0] + parts[1][0])


def thirds():
    sent = eval(input("number of sentences"))
    for _ in range(sent):
        s = input("sentence here")
        print(s[2::3])


def word_average():
    sentence = input("sentence here")
    acc = 0
    x = sentence.split()
    for word in x:
        acc += len(word)
    print(acc / len(x))


def pig_latin():
    x = input("sentence")
    x = x.lower()
    x = x.split()
    for word in x:
        print(word[1:] + word[0] + "ay", end=" ")


def main():
    #name_reverse()
    #company_name()
    #initials()
    #names()
    #thirds()
    #word_average()
    #pig_latin()
    # add other function calls here


main()
