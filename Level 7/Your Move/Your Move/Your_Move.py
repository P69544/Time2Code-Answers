# Your move program

# -------------------------
# Subprograms
# -------------------------
def get_move():
    move = input("Enter move location: ")
    move = "".join(move.split())
    return move.upper()

def get_indexes(move):
    letters = ["A","B","C","D","E","F","G","H","I"]
    numbers = [1,2,3,4,5,6,7,8,9]
    coords = []
    for char in move:
        if char in letters:
            index = letters.index(char)
            coords.append(numbers[index])
        else:
            coords.append(int(char))
    return coords
    
# -------------------------
# Main program
# -------------------------
    
move = get_move()   
print(get_indexes(move))
