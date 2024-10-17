# A program to tell the user which continents are still on their travel bucket list

# ----------------
# Constants
# ----------------
CONTINENT_LIST = ["North America", "South America", "Europe", "Asia", "Africa", "Antarctica", "Oceania"]

# ----------------
# Subprograms
# ----------------
def checkVisited():
    continents = CONTINENT_LIST.copy()
    choice = ""
    while choice != "f":
        #print(continents)
        choice = str(input("Enter Continent you have visited ('f' to finish): "))
        if choice in continents:
            continents.remove(choice)
        else:
            print("Invalid Input")
    return continents

# ----------------
# Main program
# ----------------
print("Welcome!")
contList = CONTINENT_LIST.copy()
unvisited = checkVisited()

if len(unvisited) == 1:
    print("The only continent left for you to visit is:",unvisited[0])
elif len(unvisited) == 0:
    print("You have visited every continent!")
else:
    print("The continents left for you to visit are: ",(", ".join(unvisited)))