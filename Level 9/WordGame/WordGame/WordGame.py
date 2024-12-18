# Word game program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
def shuffle_letters():
    grid = [["" for column in range(4)] for row in range(4)]
    random.shuffle(grid)
    
    file = open("dice.txt","r")
    for row in range(4):
        for column in range(4):
            dice = file.readline()
            dice = dice.strip()
            face_list = dice.split(",")
            face_chosen = random.randint(0,5)
            letter = face_list[face_chosen]
            grid[row][column] = letter
    file.close()
    return grid

def show_letters(grid):
    for row in range(4):
        result = []
        for column in range(4):
            result.append(grid[row][column])
        print("".join(result))
        

# -------------------------
# Main program
# -------------------------
grid = shuffle_letters()
show_letters(grid)
