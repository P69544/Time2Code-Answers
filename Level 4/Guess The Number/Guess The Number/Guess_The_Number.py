
# Guess the number program

# -------------------------
# Import libraries
# -------------------------
import random

# -------------------------
# Subprograms
# -------------------------
def play_guess_the_number(min, max):
    answer = random.randint(min, max)
    wrong = True
    guesses = 0
    while wrong:
        guess = int(input("Enter your guess: "))
        guesses += 1
        if guess == answer:
            wrong = False
            print("You got it correct!")
        elif guess > answer:
            print("Your guess is too high!")
        else:
            print("Your guess is too low.")
    print("You guessed:",str(guesses),"time(s)!")
# -------------------------
# Main program
# -------------------------
minimum = int(input("Enter minimum number: "))
maximum = int(input("Enter maximum number: "))
play_guess_the_number(minimum, maximum)