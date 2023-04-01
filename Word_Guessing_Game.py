import random

fruits = ["apple", "banana", "cherry", "orange", "mango"]
animals = ["elephant", "giraffe", "tiger", "lion", "zebra"]
accessories = ["watch", "necklace", "ring", "bracelet", "earrings"]
stationary = ["pen", "pencil", "notebook", "eraser", "ruler"]
alcohol = ["whiskey", "beer", "wine", "vodka", "tequila"]
words = fruits + animals + accessories + stationary + alcohol

word = random.choice(words)

guesses = ''
turns = 12

name = input("What is your name? ")

while turns > 0:
    correct_guess = False

    for letter in word:
        if letter in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')

    guess = input("\n" + name + ", guess a letter: ")

    for letter in word:
        if letter == guess:
            correct_guess = True

    guesses += guess

    if not correct_guess:
        turns -= 1
        print("Wrong! You have", turns, "turns left.")

        if turns == 0:
            print("Sorry, you have run out of turns. The word was", word)
            break

    if all(letter in guesses for letter in word):
        print("Congratulations, " + name + "! You have guessed the word.")
        break