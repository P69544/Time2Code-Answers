# A program to check if the user's password is secure

# ----------------
# Subprograms
# ----------------
def check_password_score(password):
    score = 0
    has_numbers = False
    has_uppercase = False
    has_lowercase = False
    has_special_characters = False
    
    if len(password) > 8:
        score += 1
    
    for character in password:
        if character.isalpha():
            if character.isupper():
                if not has_uppercase:
                    score += 1
                    has_uppercase = True
            if character.islower():
                if not has_lowercase:
                    score += 1
                    has_lowercase = True
        if character.isdigit():
            if not has_numbers:
                score += 1
                has_numbers = True
        if not character.isalnum():
            if not has_special_characters:
                score += 1
                has_special_characters = True
    return score

def check_password_strength(score):
    if score == 5:
        print("Strong password!")
    elif score >= 3:
        print("Moderate password.")
    else:
        print("Weak password!")
# ----------------
# Main program
# ----------------
print("Welcome to the Password Strength Checker!")
print("For security reasons, we recommend that you don't enter your real passwords here.")
password = input("Enter your password: ")
password_score = check_password_score(password)
check_password_strength(password_score)