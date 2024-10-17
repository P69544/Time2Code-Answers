# Cut the deck program

# -------------------------
# Import libraries
# -------------------------
import random

# -------------------------
# Subprograms
# -------------------------
def output_winner(player, cpu):
    plrI = cards.index(player)
    cpuI = cards.index(cpu)
    
    if plrI % 9 == cpuI % 9:
        if plrI > cpuI:
            print("Player Wins!")
        else:
            print("CPU Wins!")
    elif plrI % 9 > cpuI % 9:
        print("Player Win!")
    else:
        print("CPU Wins!")
        
def play_game():
    choice = -1

    random.shuffle(deck)
    while choice > 34 or choice < 0:
        print("Enter a number from 0-34!")
        choice = int(input("Choice: "))
    print("Your Card:",deck[choice])
    deck.pop(choice)
    choice = deck[choice]
    
    cpuI = random.randint(0, len(deck)-1)
    cpuCard = deck[cpuI]
    deck.pop(cpuI)
    print("Computer's Card:",cpuCard)
    
    output_winner(choice, cpuCard)
        

# -------------------------
# Main program
# -------------------------
cards = ["6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC",
         "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD",
         "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH",
         "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS"]

deck = cards.copy()
seed = random.seed("P69544")
play_game()