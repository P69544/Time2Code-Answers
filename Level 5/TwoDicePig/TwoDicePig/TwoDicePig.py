# Two-dice pig program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
def roll():
    dice = [0, 0]
    dice[0] = random.randint(1, 6)
    dice[1] = random.randint(1, 6)
    return dice    


def points(dice):
    if dice[0] == 1 and dice[1] == 1:
        return -1
    elif dice[0] == 1 or dice[1] == 1:
        return 0
    else:
        return dice[0] + dice[1]


def play_game(playerCount):
    random.seed()
    score = [0]*playerCount
    player = 0
    new_player = True
    while score[0] <= 100 and score[1] <= 100:
        if new_player:
            print()
            print("------------------------------------")
            print("Player", player + 1, "it's your turn.")
            print("Your score is currently:", score[player])
            total = 0
            new_player = False
            turn_end = False
        print("Press Enter to roll the dice.")
        input()
        dice = roll()
        result = points(dice)
        print("You rolled a", dice[0], "and", dice[1])
        if result > 0:
            print("You scored", result)
            total = total + result
            print("Your total is", total)
            choice = ""
            while choice not in ["y", "n"]:
                choice = input("Do you want to continue y/n? :")
            if choice == "n":
                score[player] = score[player] + total
                turn_end = True
        elif result == -1:
            print("That's a double pig out, back to zero!")
            score[player] = 0
        else:
            print("Oh no, that's a pig out!")
            turn_end = True
        if turn_end:
            print("Press Enter to hand the dice to the next player.")
            input()
            player = (player + 1) % playerCount
            new_player = True


# -------------------------
# Main program
# -------------------------
playerCount = -1         
while playerCount > 4 or playerCount < 1:            
    playerCount = int(input("How many players (1-4)?: "))   
    
play_game(playerCount)
