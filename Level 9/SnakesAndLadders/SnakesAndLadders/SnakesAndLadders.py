# Snakes and ladders program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
def play(board, players):
    current_player = 0
    game_won = False
    while not game_won:
        player_square = players[current_player]
        print()
        print("------------------------------------")
        print("Player", current_player + 1, "it's your turn.")
        print("You are on square", player_square)
        print("Press Enter to roll the dice.")
        wait = input()
        dice = random.randint(1, 6)
        print("You rolled a", dice)
        player_square = player_square + dice
        if player_square > len(board) - 1:
            player_square = len(board) - 1
        print("You moved to square", player_square)
        board_square = board[player_square]
        if  board_square < player_square:
            print("Oh no, you landed on a snake.")
            player_square = board_square
            print("You are now on square", player_square)
        elif board_square > player_square:
            print("Yay, you landed on a ladder.")
            player_square = board_square
            print("You are now on square", player_square)
        if player_square >= len(board) - 1:
            game_won = True
            print("Player", current_player + 1, "wins the game!")
        else:
            players[current_player] = player_square
            print("Press Enter for the next player to take their turn.")
            wait = input()
            current_player = (current_player + 1) % len(players)


def initialise_board(squares, specials):
    random.seed()
    board = []
    for square in range(squares + 1):
        board.append(square)
    random_start = 0
    random_end = 0
    squares_used = []
    for count in range(specials):
        while random_start in squares_used or random_end in squares_used:
            random_start = random.randint(2, squares - 1)
            random_end = random.randint(2, squares - 1)
        squares_used.append(random_start)
        squares_used.append(random_end)
        board[random_start] = random_end
    return board


def initialise_players():
    playerCount = 0
    while playerCount < 2:
        playerCount = int(input("How many players?"))
    players = []

    for _ in range(playerCount):
        players.append(1)
    return players


# -------------------------
# Main program
# -------------------------
board = initialise_board(25, random.randint(3,7))
players = initialise_players()
play(board, players)
