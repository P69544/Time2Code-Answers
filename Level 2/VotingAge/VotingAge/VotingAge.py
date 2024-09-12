# A program to check if the user is old enough to vote in the UK
# ----------------
# Subprograms
# ----------------
def check_age(age, country):
    if country == "UK":
        boundary = 18
    elif country == "AUSTRIA":
        boundary = 16
    else:
        boundary = 18
        
    if age >= boundary: # Condition
        print("You are old enough to vote!")
    else:
        print("You are not old enough to vote.")
# ----------------
# Main program
# ----------------
user_age = int(input("How old are you? ")) # Input statement
user_country = input("What country are you from? (UK, Austria): ")
check_age(user_age, user_country.upper())