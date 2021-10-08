"""
Trent Varnes
Traffic.py
analyze traffic
I certify this is entirely my own work
"""

def main():
    roads = eval(input("enter the number of roads surveyed: "))
    acc_cars = 0
    total = 0
    for i in range(roads):
        days = eval(input("How many days was road " + str(i + 1) + " surveyed?"))
        for j in range(days):
            cars = eval(input("How many cars traveled on day " + str(j + 1) + "?"))
            acc_cars += cars
        day_average = acc_cars / days
        print("total cars traveled is : " + str(acc_cars))
        total += acc_cars
        acc_cars = 0
        print("road", roads, "average cars per day : ", day_average)
    total_average = total / roads
    print("total number of vehicles: ", total)
    print("average number of cars per road: ", round(total_average, 2))


if __name__ == '__main__':
    main()
