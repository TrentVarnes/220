"""
Trent Varnes
weighted_average.py
I certify this is my work
"""


def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    for line in infile:
        seperated = line.split(":")
        grades = seperated[1]
        weights = seperated[1]
        grades = grades.split()
        weights = weights.split()
        grade_list = grades[1::2]
        weights_list = weights[0::2]
        multi_list = []
        for i in range(0, len(grade_list)):
            grade_list[i] = int(grade_list[i])
            for i in range(0, len(weights_list)):
                weights_list[i] = int(weights_list[i])
        added = 0
        for e in range(0, len(weights_list)):
            added = added + weights_list[e]
        for num1, num2 in zip(weights_list, grade_list):
            multi_list.append(num1 * num2)
        total = 0
        for i in range(0, len(multi_list)):
            total = total + multi_list[i]
        new_total = round(total / 100, 1)
        if added < 100:
            outfile.write(seperated[0] +"'s average: " + "Error: The weights are less than 100." + "\n")
        elif added > 100:
            outfile.write(seperated[0] + "'s average: " + "Error: The weights are more than 100." + "\n")
        else:
            outfile.write(seperated[0] + "'s average: " + str(new_total) + "\n")


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == '__main__':
    main()