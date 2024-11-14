# Debit card program

# -------------------------
# Subprograms
# -------------------------
def validate_number(number_on_card):
    valid = True
    number_of_characters = len(number_on_card)
    if number_of_characters == 16 or number_of_characters == 19:
        for character in number_on_card:
            if not character.isdigit() and character != " ":
                valid = False    
    else:
        valid = False
    return valid

def validate_name(name_on_card):
    if name_on_card.isalpha():
        print(name_on_card.upper())
        return True
    else:
        return False

def input_card_details():
    valid_card = False
    valid_name = False
    while not valid_card:
        while not valid_name:
            name_input = input("Enter cardholder's full name: ")
            valid_name = validate_name(name_input)
        number_input = input("Enter the 16 digit number: ")
        valid_card = validate_number(number_input)


# -------------------------
# Main program
# -------------------------
input_card_details()
print("Card details valid.")
