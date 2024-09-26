# Polyhedral dice program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
def roll_dice(s):
    if s == 6:
        print("Roll a D6")
        return random.randint(1, 6)
    elif s == 8:
        print("Roll a D8")
        return random.randint(1, 8)
    elif s == 10:
        print("Roll a D10")
        return random.randint(1, 10)
    elif s == 12:
        print("Roll a D12")
        return random.randint(1, 12)
    else:
        return None

# -------------------------
# Main program
# -------------------------
random.seed()
selection = int(input("Would you like to roll the 6, 8, 10, or 12 sided dice?: "))
number = roll_dice(selection)
if number == None:
    print("Invalid selection.")
else:
    if number == 8 or number == 11:
        print("You rolled an", number)
    else:
        print("You rolled a", number)
