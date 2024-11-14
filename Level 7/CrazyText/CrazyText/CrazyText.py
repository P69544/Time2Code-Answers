# A program to generate cRAzY tExT

# ----------------
# Import libraries
# ----------------
import random
# ----------------
# Subprograms
# ----------------
def make_text_crazy(text):
    crazy_text = ""
    for character in text:
        if character.isalpha():
            upper_or_lower = random.randint(0,1)
            if upper_or_lower == 0:
                new_letter = character.upper()
            else:
                new_letter = character.lower()
            crazy_text += new_letter
        else:
            crazy_text += character
    return crazy_text
# ----------------
# Main program
# ----------------
print("Welcome to the cRAzY tExT generator")
user_text = input("Enter your text: ")
crazy_text = make_text_crazy(user_text)
print(crazy_text)