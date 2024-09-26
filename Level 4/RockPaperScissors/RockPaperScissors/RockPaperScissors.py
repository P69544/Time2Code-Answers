# Rock, paper, scisssors program

# -------------------------
# Import libraries
# -------------------------
import random

# -------------------------
# Subprograms
# -------------------------

choices = ["R", "P", "S"]

def getPlayerChoice():
    valid = ["R", "P", "S"]
    selection = ""
    while selection not in choices:
        selection = input("Rock [R], Paper [P], or Scissors [S]?: ")
        selection = selection.upper()
    return selection

def cpuChoice():
    number = random.randint(0,2)
    return choices[number]

def convert(rps):
    if rps == "R":
        return "ROCK"
    elif rps == "P":
        return "PAPER"
    else:
        return "SCISSORS"

def whoWonRound(plr, cpu):
    ##-----------    Draw    -----------
    if plr == cpu:
        return "Draw"
    #-----------   CPU Wins  -----------
    elif plr == "R" and cpu == "P":
        return "CPU"
    elif plr == "P" and cpu == "S":
        return "CPU"
    elif plr == "S" and cpu == "R":
        return "CPU"
    #----------- Player Wins -----------
    elif cpu == "R" and plr == "P":
        return "Player"
    elif cpu == "P" and plr == "S":
        return "Player"
    elif cpu == "S" and plr == "R":
        return "Player"
    #---------- Error Handling ----------
    else:
        return "NaN"

def playGame():
    plrScore = 0
    cpuScore = 0
    
    while plrScore < 5 and cpuScore < 5:
        print("---- Player Score:",str(plrScore),"----")
        print("---- CPU Score:",str(cpuScore),"----")
        
        plrPick = getPlayerChoice()
        cpuPick = cpuChoice()
        
        winner = whoWonRound(plrPick, cpuPick)
        
        print() # Seperating Line
        if winner == "Draw":
            print("Both picked",convert(plrPick))
            print("It's a draw!")
        elif winner == "Player":
            print("Player:",convert(plrPick))
            print("CPU:",convert(cpuPick))
            print("Player Gains A Point!")
            plrScore += 1
        elif winner == "CPU":
            print("Player:",convert(plrPick))
            print("CPU:",convert(cpuPick))
            print("CPU Gains A Point!")
            cpuScore += 1
        print() # Seperating Line
    if plrScore > cpuScore:
        print("Player wins!")
    else:
        print("CPU wins!")
        
# -------------------------
# Main program
# -------------------------
        
playGame()