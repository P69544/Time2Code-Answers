# A program to:

# ----------------
# Import libraries
# ----------------
import random
# ----------------
# Subprograms
# ----------------
def select_random_song():
  with open("songs.txt", "r") as songfile:
    songs = songfile.readlines()
    amount = len(songs)
    selection = random.randint(0, amount-1)
    return songs[selection]

def format_song(song):
  song = song.split()
  result = []
  for each in song:
    underscores = len(each)-1
    if each[len(each)-1:] == ",":
      underscores -= 1
      newWord = [each[0], ("_"*underscores)+", "]
    else:
      newWord = [each[0], ("_"*underscores)+" "]
    result.append("".join(newWord))
  return "".join(result)
  
# ----------------
# Main program
# ----------------
cont = True
score = 0

print("Welcome to Guess the Song!")
while cont:
  print("Fill in the blanks: ")
  
  answer = select_random_song()
  question = format_song(answer)
  
  print(question)
  guess = input("Your Guess: ")
  
  if guess.strip().lower() == answer.strip().lower():
    print("Correct answer!")
    score += 1
  else:
    print("The correct answer was",answer)
    cont = False
print("You scored",score)
input("-- ENTER TO EXIT --")