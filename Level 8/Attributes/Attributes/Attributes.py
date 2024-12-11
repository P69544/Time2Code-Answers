
# Attributes program

# -------------------------
# Subprograms
# -------------------------
def make_character():
    name = str(input("Enter character name: "))
    health = int(input("Enter health amount: "))
    attack = int(input("Enter attack value: "))
    defence = int(input("Enter defence value: "))
    return [name, health, attack, defence]


def save_character(attributes):
    file = open("character.txt","w")
    for item in attributes:
        file.writelines(str(item)+"\n")
    file.close()


# -------------------------
# Main program
# -------------------------
character = make_character()
save_character(character)
print("Character saved.")
