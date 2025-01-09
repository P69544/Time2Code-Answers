# Saving data program

# -------------------------
# Subprograms
# -------------------------

def load(filename):
    file = open(filename, "r")
    user = file.read()
    file.close()
    user = user.strip()
    if user == "":
        return False
    else:
        return user

def save(user, filename):
    file = open(filename, "w")
    user = user + "\n"
    file.write(user)
    file.close()

def firstRun():
    print("Hello, I don't believe we have met.")
    name = input("What is your name?: ")
    print("Nice to meet you,",name+".")
    save(name, "datafile.txt")
    
def main(user):
    print("This program was written by", user + ".")
    
# -------------------------
# Main program
# -------------------------
user = load("datafile.txt")
if user == False:
    firstRun()
else:
    main(user)