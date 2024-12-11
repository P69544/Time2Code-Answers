# This program allows the user to display a random joke from a text file, and write their own jokes to the text file

import random

# ----------------
# Constants
# ----------------

FILE_PATH = "jokes.txt"

# ----------------
# Subprograms
# ----------------

def read_jokes_from_file(file_path):
  with open(file_path, 'r') as jokes_file: # Using 'with' is a lot more organised, and does not need a file.close() statement.
    jokes = jokes_file.readlines() # Puts each line in a list for reading
  return jokes

def choose_random_joke(jokes):
  random_joke = random.choice(jokes)
  return random_joke

def add_joke(file_path):
  new_joke = input("Enter your joke: ") + "\n"
  with open(file_path,"a") as jokes_file:
    jokes_file.write(new_joke)
    
def menu():
  while True:
    jokes = read_jokes_from_file(FILE_PATH)
    print("Welcome to the Joke Book!")
    choice = 0
    while (choice < 1) or (choice > 3):
      choice = int(input("What do you wanna do?:\n1. Hear a joke\n2. Add a joke\n3. Exit\nChoice: "))
    match choice:
      case 1:
        random_joke = choose_random_joke(jokes)
        print("Random Joke:", random_joke)
      case 2:
        add_joke(FILE_PATH)
      case 3:
        return
# ----------------
# Main Program
# ----------------

menu()