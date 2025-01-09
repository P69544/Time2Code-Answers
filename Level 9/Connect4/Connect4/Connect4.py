# This program will simulate the classic Four in a Row game

# ----------------
# Subprograms
# ----------------
def create_empty_board():
    board = []
    for i in range(6):
        row = []
        for j in range(7):
            row.append("⚪")
        board.append(row)
    return board

def display_board(board):
    print()
    print(("+----" * 7) + "+")
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print(('+----' * 7) + "+")
    print("  1    2    3    4    5    6    7  ")
    
def get_user_move(player, board):
    col = int(input(f"Player {player}, choose a column (1 to 7): ")) - 1
    while not (0 <= col < 7 and board[0][col] == "⚪"):
        col = int(input(f"Invalid move. Player {player}, choose a column (1 to 7): ")) - 1
    return col

def make_move(board, col, player_character):
    placed = False
    row = len(board)-1
    while not placed and row >= 0:
        if board[row][col] == "⚪":# and board[row+1][col] != "⚪":
          board[row][col] = player_character
          placed = True
        row -= 1
    return board

def check_winner(board, player_character):
    for row in range(6):
        for col in range(4):
            winning_sequence = True
            for i in range(4):
                if board[row][col + i] != player_character:
                    winning_sequence = False
            if winning_sequence:
                 return True
    for col in range(7):
        for row in range(3):
            winning_sequence = True
            for i in range(4):
                if board[row + i][col] != player_character:
                    winning_sequence = False
                    break
            if winning_sequence:
                return True
    for row in range(3):
        for col in range(4):
            winning_sequence = True
            for i in range(4):
                if board[row + i][col + i] != player_character:
                    winning_sequence = False
                    break
            if winning_sequence:
                return True
    for row in range(3):
        for col in range(3, 7):
            winning_sequence = True
            for i in range(4):
                if board[row + i][col - i] != player_character:
                    winning_sequence = False
                    break
            if winning_sequence:
                return True
            
def is_board_full(board):
    for row in board:
        if "⚪" in row:
            return False
    return True
# ----------------
# Main program
# ----------------
player_characters = ["🔴", "🔵"]
player = 1
game_finish = False

print("Welcome to Four in a Row!\n")
board = create_empty_board()
display_board(board)

while not game_finish:
    player_character = player_characters[player - 1]
    column = get_user_move(player, board)
    board = make_move(board, column, player_character)
    display_board(board)
    
    if check_winner(board, player_character):
      print(f"Player {player} wins!")
      game_finish = True
    elif is_board_full(board):
      print("It's a tie!")
      game_finish = True
      
    if player == 1:
        player = 2
    else:
        player = 1