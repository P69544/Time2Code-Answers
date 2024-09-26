# A program to test students arithmetic with a simple guess the number game

# ----------------
# Import libraries
# ----------------
import random
# ----------------
# Subprograms
# ----------------
def generate_number(number1, number2):
    option = random.randint(1, 3)
    match option:
        case 1:
            answer = number1 + number2
        case 2:
            answer = number1 - number2
        case 3:
           answer = number1 * number2
    return answer
# ----------------
# Main program
# ----------------
print("Welcome to Twisted Guess the Number! You'll be presented with two numbers and asked to guess the third, which will either be the sum of the two, the multiple of the two or the second subtracted from the first.")
lost = False
score = 0
while not lost:
    number1 = random.randint(1, 11)
    number2 = random.randint(1, 11)
    answer = generate_number(number1, number2)
    print("The first number is:", number1)
    print("The second number is:", number2)
    guess = int(input("Take a guess at the third number: "))
    if guess == answer:
        score += 1
        print("You were right! Your score is now:", score)
    else:
        print("Incorrect! The answer was actually:", answer)
        print("Your final score is:", score)
        lost = True
    print()