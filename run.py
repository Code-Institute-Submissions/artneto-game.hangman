# Your code goes here.
from random import choice

# Gets a random word from my list_of_words and return the word
# with the word in uppercase.

with open('newords.txt') as file:
    lines = file.read()
    list_of_words = lines.split('\n')

word = choice(list_of_words).upper()

word = choice(list_of_words).upper()
# This function holds the different stages of user guesses 
# and displays the graphic for a hangman.
hang = """
____
    |
    |
    -"""


empty = """
"""

head = """
    0
"""

body = """
    0
    |
"""

left_arm = """
    0
   /|
"""
right_arm = """
    0
   /|\\
"""
left_leg = """
    0
   /|\\
   /
"""
right_leg = """
    0
   /|\\
   / \\
"""


chance_for_man = [empty,
                  head,
                  body,
                  left_arm,
                  right_arm,
                  left_leg,
                  right_leg,
                  ]

win = 0
wrong = 0
letters_rg = ''
letters_wrg = ''

# Displays the welcome prompt and introduces user to the quiz and rules,
# and takes an input from customer to start the quiz.
print('*********************************')
print("Let's Play Hangman!")
print('*********************************')
name = input("Enter your name -> ")
print('Welcome', name, '!')
print(" ----------------------------------------- ")
print("The objective of the Hangman is to guess the secret word.")
print("You will need to try you letter at a time,")
print("but If the word does not contain the suggested letter")
print("the computer will draws one element of a hangman’s gallows")

while win != len(word) and wrong != 7:
    message = ''
# Checking if user input matches the letter in the "secret word".
    for letter in word:
        if letter in letters_rg:
            message += f'{letter} '
        else:
            message += '_ '
    print(hang+chance_for_man[wrong])
    print(message)

    letter = input('please input a letter').upper()

    if letter in letters_rg+letters_wrg:
        print('Wrong guess')
        continue

