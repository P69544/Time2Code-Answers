# A program to: 

# ----------------
# Import libraries
# ----------------
import random
# ----------------
# Subprograms
# ----------------
def generateNumber():
    digits = [0,0,0,0]
    
    for index in range(0,4):
        num = random.randint(0,9)
        digits[index] = str(num)
        
    digits = "".join(digits)
    return int(digits)

def giveClue(guess, answer):
    samePlace = False
    differentPlace = False
    guess,answer = str(guess), str(answer)
    
    for index in range(0,len(guess)-1):
        if guess[index] == answer[index]:
            samePlace = True
        for digit in answer:
            if digit in guess:
                differentPlace = True
    if samePlace:
        return "Bosh"
    elif differentPlace:
        return "Bash"
    else:
        return "Bish"
        
    
# ----------------
# Main program
# ----------------
answer = generateNumber()
guess = 0

print("The answer is a 4 digit number [0000-9999]")
while guess != answer:
    guess = int(input("Enter your guess"))
    if guess != answer:
        print(giveClue(guess,answer))
    else:
        print("You got it!")