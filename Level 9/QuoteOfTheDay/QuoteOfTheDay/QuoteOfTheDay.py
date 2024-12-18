# Quote of the day program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
def random_quote():
    quotes = [["Any fool can write code that a computer can understand. Good programmers write code that humans can understand.","Martin Fowler"],["Code is like humour. When you have to explain it, it's bad.","Cory House"],["Simplicity is the soul of efficiency.","Austin Freeman"]]
    selected = quotes[random.randint(0, len(quotes) - 1)]
    return selected

# -------------------------
# Main program
# ------------------------- 
quote = random_quote()
print('"'+quote[0]+'"')
print("  - "+quote[1])
