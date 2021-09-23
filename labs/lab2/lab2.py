"""
Trent Varnes
Lab2.py
"""

def sum_of_threes(n):
    res = 0;
    for i in range(1, n + 1):
        if (i % 3 == 0):
            res += 1;
    return res;
    print(sum_of_threes(9))

if __name__ == 'sum_of_threes':
        sum_of_threes()