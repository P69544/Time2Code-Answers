# A program to generate a random clickbait newspaper headline

# ----------------
# Import libraries
# ----------------
import random
# ----------------
# Constants
# ----------------

PEOPLE = ["Baby", "Toddler", "Teenager", "Man", "Woman", "Elderly woman", "Elderly man", "Elephant", "Doctor", "Fish"]
ACTIVITIES = ["does a poo", "rides elephant", "falls out of hot air balloon", "makes silly noise", "flies kite", "eats a sandwich", "does a trump"]
PLACES = ["school", "playground", "attic", "swimming pool", "cinema", "bowling alley", "restaurant"]
NOUNS = ["elephant", "dog", "banana", "athlete", "teddy bear", "walkie talkie"]
FEELINGS = ["amused", "shocked", "surprised", "humiliated", "astonished", "bowled over", "amazed"]

# ----------------
# Subprograms
# ----------------
def generate_type1():
  chosen_person = random.choice(PEOPLE)
  chosen_activity = random.choice(ACTIVITIES)
  chosen_place = random.choice(PLACES)
  headline = f"{chosen_person} {chosen_activity} in {chosen_place}."
  return headline

#NUMBER reasons why PLURAL_NOUN is weirder than you think (number NUMBER will surprise you!)
def generate_type2():
  chosen_number = random.randint(8,100)
  chosen_noun = random.choice(NOUNS)
  chosen_num2 = random.randint(8,chosen_number)
  headline = f"{chosen_number} reasons why {chosen_noun} is weirder than you think (number {chosen_num2} will surprise you!)."
  return headline

#PERSON is FEELING to find NOUN in PLACE
def generate_type3():
  chosen_person = random.choice(PEOPLE)
  chosen_feeling = random.choice(FEELINGS)
  chosen_noun = random.choice(NOUNS)
  chosen_place = random.choice(PLACES)
  headline = f"{chosen_person} is {chosen_feeling} to find {chosen_noun} in {chosen_place}!"
  return headline
# ----------------
# Main program
# ----------------
print("Welcome to the fake newspaper headline generator! This will give you a randomly generated silly newspaper headline to make you laugh...")

sentence_type = random.randint(1, 3)
match sentence_type:
    case 1:
        sentence = generate_type1()
    case 2:
        sentence = generate_type2()
    case 3:
        sentence = generate_type3()
print(sentence)