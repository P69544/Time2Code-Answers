# A program to check if a user's password matches the default password
# ----------------
# Constants
# ----------------
PASSWORD = "LetMeIn"
# ----------------
# Subprograms
# ----------------
def checkPassword(actualPass):
    while True:
        guess = str(input("Enter Password: "))
        if guess != actualPass:
            print("Incorrect Password.")
        else:
            print("Login successful!")
            return
            
        
# ----------------
# Main program
# ----------------
print("Welcome!")
checkPassword(PASSWORD)