# Missiles program

# -------------------------
# Import libraries
# -------------------------
import random

# -------------------------
# Subprograms
# -------------------------
def get_target():
    x = int(input("Enter X Coordinate: ")[0])
    y = int(input("Enter Y Coordinate: ")[0])
    return [x,y]

def place_buildings():
    buildings = []
    for building in range(10):
        xCoord,yCoord = -1, -1
        while [xCoord, yCoord] in buildings or (xCoord == -1 and yCoord == -1):
            xCoord = random.randint(0,7)
            yCoord = random.randint(0,7)
        buildings.append([xCoord, yCoord])
    return buildings

def uav(buildings):
    global board  
    print(buildings)
    for xCoord in range(1,6):
        for yCoord in range (1,6):
            if [xCoord, yCoord] in buildings:
                newX = random.randint(xCoord-1, xCoord+1)
                newY = random.randint(yCoord-1, yCoord+1)
                board[newX][newY] = "u"

def hit(x, y, buildingLocations):
    if [x,y] in buildingLocations:
        board[x][y] = "H"
        buildingLocations.remove([x,y])
        print("That's a hit! There are",len(buildingLocations),"buildings left!")
    else:
        board[x][y] = "x"
        print("You missed, there are still",len(buildingLocations),"buildings left.")
    
def draw_board():
    global board
    rowNum = -1
    print(" 01234567")
    for row in board:
        rowNum += 1
        print(str(rowNum)+"".join(row))
    
def play_game():
    missileCount = 50
    buildings_left = 10
    buildingLocations = place_buildings()
    uav(buildingLocations)
    while missileCount > 0 and len(buildingLocations) != 0:
        draw_board()
        target = get_target()
        hit(target[0], target[1], buildingLocations)
        missileCount -= 1
        print("You have",missileCount,"missiles left.")
    if len(buildingLocations) == 0:
        print("You won!")
    else:
        print("You ran out of missiles, game over!")
        
# -------------------------
# Main program
# -------------------------
random.seed()
board = [["-" for _ in range(8)] for _ in range(8)]
play_game()