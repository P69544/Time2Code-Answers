# Cup draw program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
def input_teams():
    teams = []
    cont = "Y"
    while cont == "Y":
        teamOne = input("Enter team one: ")
        teamTwo = input("Enter team two: ")

        teams.append(teamOne)
        teams.append(teamTwo)
        cont = input("Continue? Y/N: ")
        cont = cont.upper()
    return teams 

def draw_teams():
      random.shuffle(teams)
      print("The Draw Is:")
      for i in range(0, len(teams)-1, 2):
          print(teams[i]+" VS "+teams[i+1])
        
# -------------------------
# Main program
# -------------------------

teams = input_teams()
draw_teams()
