# Noughts and crosses program

# -------------------------
# Function Checks
# -------------------------
# The game is a draw
# Invalid move
# O wins diagonal
# O wins horizontal
# O wins vertical
# X wins diagonal
# X wins horizontal
# X wins vertical 
  
# -------------------------
# Subprograms
# -------------------------

def get_move(player):
    global board
    coords = ""
    valid = False
    while not valid: # Checks if its blank, then if its the right length, then if its a empty space to prevent errors
        coords = str(input("Enter XY coordinate: "))
        if len(coords.strip()) != 2: # Check if the string is the right length
            valid = False
        else:
            coordList = []
            for char in coords:
                coordList.append(int(char)) # Converts string into an X and Y integer
            if board[coordList[0]][coordList[1]] == -1: # Check if square is empty
                valid = True
            else:
                valid = False
    if player == 1:
        board[coordList[0]][coordList[1]] = 0
    else:
        board[coordList[0]][coordList[1]] = 10

def draw_board():
    global board
    print("\n  0 1 2")
    rowNum = -1
    for row in board:
        newRow = []
        newRow.append(" ")
        for item in row:
            if item == -1:
                newRow.append("-")
                newRow.append(" ")
            elif item == 0:
                newRow.append("O")
                newRow.append(" ")
            else:
                newRow.append("X")
                newRow.append(" ")
        rowNum += 1
        print(str(rowNum)+"".join(newRow))

def won(): # Fix
    global board
    for y in range(3):
        htotal = 0
        vtotal = 0
        for x in range(3):
            htotal += board[x][y]
            vtotal += board[y][x]
        if htotal == 30 or vtotal == 30:
            return (True, "X")
        elif htotal == 0 or vtotal == 0:
            return (True, "O")
    dtotal = board[0][0] + board[1][1] + board[2][2]
    if dtotal == 30:
        return (True, "X")
    elif dtotal == 0:
        return (True, "O")
    dtotal = board[2][0] + board[1][1] + board[0][2]
    if dtotal == 30:
        return (True, "X")
    elif dtotal == 0:
        return (True, "O")
    return False, ""

def play_game():
    player = 2
    complete = False
    while not complete:
        if player == 1:
            player = 2
        else:
            player = 1
            
        draw_board()
        get_move(player)
        complete, winner = won()
    draw_board()
    print("\n"+winner, "wins!")


# -------------------------
# Main program
# -------------------------
board = [[-1 for x in range(3)] for x in range(3)]
play_game()