# A program to simulate the TV show Play Your Cards Right

# ----------------
# Import libraries
# ----------------
import random

# ----------------
# Subprograms
# ----------------
def display_intro():
  print("Welcome to Play Your Cards Right!")
  print("Cards with the numbers 1-9 have been randomly shuffled.")
  print("You'll be shown the first card and will have to guess whether the next card is higher or lower.")
  print("If you guess correctly, then you'll repeat the process with the next card, and will have to guess whether the next card is higher or lower.")
  print("To win the game, you'll have to predict all the cards correctly.")

def play_game(cards):
  guessed_incorrectly = False
  while len(cards) > 1 and not guessed_incorrectly:
    print()
    print("Your card is:", cards[0])
    user_guess = input("Do you think the next card will be higher or lower? ")
    if cards[1] > cards[0] and user_guess == "higher":
      cards.pop(0)
    elif cards[1] < cards[0] and user_guess == "lower":
      cards.pop(0)
    else:
      guessed_incorrectly = True
  return len(cards)

def check_result(cards_length):
  if cards_length == 1:
    print("Congratulations, you won!")
  else:
    print("You have lost!")
    print("Play again? Y/N : ")
    choice = ""
    while choice != "Y" or choice != "N":
        choice = str(input("Choice: "))[0].upper()
        if choice == "Y":
          return True
        else:
          return False

# ----------------
# Main program
# ----------------
playing = True
display_intro()

while playing:
    cards = [1,2,3,4,5,6,7,8,9]
    random.shuffle(cards)
    cards_length = play_game(cards)
    playing = check_result(cards_length)    