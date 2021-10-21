"""
Name: Trent Varnes
lab8.py
"""


from encryption import encode, encode_better


def number_words(infile_name, outfile_name):
    infile = open(infile_name, "r")
    outfile = open(outfile_name, "w+")
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            outfile.write(str(i) + word + "\n")
            i += 1


def hourly_wages(infile_name, outfile_name):
    infile = open(infile_name, "r")
    outfile = open(outfile_name, "w+")
    for line in infile:
        parts = line.split()
        wage = float(parts[2])
        wage += 1.65
        total = wage * int(parts[3])
        outfile.write(parts[0] + parts[1] + str(total))


def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc += (pos * int(isbn[i]))
    return acc


def send_message(file, friend):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(line)


def send_safe_message(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(encode(line, key))


def send_uncrackable_message(file, friend, pad):
    padkey = open(pad, "r")
    key = padkey.read()
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(encode_better(line, key))


def main():
    number_words("Walrus.txt", "Walrus_out.txt")
    hourly_wages("hourly_wages.txt", "new_hourly.txt")
    calc_check_sum("0072946520")
    send_message("message.txt", "bob")
    send_safe_message("secret_message.txt", "tom", 3)
    send_uncrackable_message("safest_message.txt", "tommy", "pad.txt")
    pass


main()
