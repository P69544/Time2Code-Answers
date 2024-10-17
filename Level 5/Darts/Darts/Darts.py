# Darts program

# -------------------------
# Subprograms
# -------------------------
def is_dart_valid(dart):
    if dart > 0 and dart < 20:
        return True
    if dart == 25 or dart == 50:
        return True
    if dart <= 40 and dart % 2 == 0:
        print("Double",dart/2)
        return True
    if dart <= 60 and dart % 3 == 0:
        print("Treble",dart/3)
        return True
    print("Invalid dart")
    return False

def play_game(score):
    player = 1
    turn = 1
    while score[0] > 0 and score[1] > 0:
        print("Player", player,",it's your turn.")
        while turn <= 3:
            print("Dart", turn)
            pts = int(input("Enter score: "))
            valid = is_dart_valid(pts)
            if valid:
                score[player-1] -= pts
            turn += 1
            
        turn = 1
        if player == 1:
            player = 2
        else:
            player = 1
    return score


# -------------------------
# Main program
# -------------------------  
score = [501, 501]
score = play_game(score)
if score[0] <= 0:
    print("Winner is Player 1!")
else:
    print("Winner is Player 2!")