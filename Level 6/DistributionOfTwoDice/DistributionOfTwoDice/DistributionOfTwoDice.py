# Distribution of two dice program

# -------------------------
# Import libraries
# -------------------------
import random

# -------------------------
# Subprograms
# -------------------------
def distribution(rolls):
    tally = [0,0,0,0,0,0,0,0,0,0,0] # 2-12
    for _ in range(1, rolls):
        dice1, dice2 = random.randint(1,6), random.randint(1,6)
        total = dice1+dice2
        tally[total-2] += 1
    return tally

# -------------------------
# Main program
# -------------------------
rolls = int(input("Amount of rolls to simulate: "))
result = distribution(rolls)

for index in range(0,len(result)):
    print(str(index+2)+":",result[index])