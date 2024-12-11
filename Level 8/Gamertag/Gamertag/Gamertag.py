# Gamertag program

# -------------------------
# Subprograms
# -------------------------
def check_exists(tag):
  try:
    file = open("players.txt", "r")
  except FileNotFoundError:
    print("File not found.")
  else:
    lines = file.readlines()
    for each in lines:
      if tag == each.strip():
        file.close()
        return True
    file.close()
    return False

def write_gamertag(tag):
    try:
      file = open("players.txt", "a")
    except FileNotFoundError:
      print("File not found.")
    else:
      file.write(tag + "\n")
      file.close()
        
def get_gamertag():
    taken = True
    while taken:
      tag = input("Enter new gamertag: ")
      taken = check_exists(tag)
      if taken:
        print("Sorry, that tag is already taken.")
      else:
  	    write_gamertag(tag)
  	    print("Successful, tag written!")

# -------------------------
# Main program
# -------------------------

get_gamertag()