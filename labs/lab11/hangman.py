"""
Name: Trent Varnes
hangman.py
"""

import random

def read_words(file_name):
    file = open(file_name, "r")
    read = file.read()
    read = read.split()
    return read

def pick_word():
    word = random.choice(read_words("wordlist.txt"))
    return word

def guessed_word(char, new_word, blank_list):
    for i in range(len(new_word)):
        if char in new_word:
            index = new_word.index(char)
            blank_list[index] = char

def secret_word_spelled():
    if guessed_word() == pick_word():
        return True
    else:
        return False

def play_game():
    name = input('Enter your name: ')
    name = name.capitalize()
    print('Lets Start Playing {}!'.format(name))
    words = read_words("wordlist.txt")
    words = [i.upper() for i in words]
    words = random.choice(words)
    guessess = ''
    loop = 7
    while loop > 0:
        fail = 0
        for i in words:
            if i in guessess:
                print(i, end=' ')
            else:
                print('-', end=' ')
                fail += 1
        if fail == 0:
            print('\nYou Won!')
            break
        guess = input('\nEnter Your Guess: ')
        guess = guess.upper()
        guessess += guess
        if guess not in words:
            loop -= 1
            if loop == 0:
                print('You Lost,Word: {}'.format(words))
            else:
                print('Wrong Guess,{} round left!'.format(loop))


def main():
    # add other function calls here
    #read_words("wordlist.txt")
    #new_word = pick_word()
    #guessed_word(char, new_word)
    play_game()
    pass


main()
