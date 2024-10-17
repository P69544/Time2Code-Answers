# RPG inventory program

# -------------------------
# Subprograms
# -------------------------
def add_item():
    item = input("What item are you adding to your inventory? : ")
    inventory.append(item)
    print("Item added.")

def craft_item():
    print("Options:\n- Charm")
    itemToCraft = input("What item do you want to craft?: ")
    if itemToCraft.lower() == "charm":
        if ("gem" in inventory) and ("leather" in inventory):
            inventory.remove("gem")
            inventory.remove("leather")
            inventory.append("charm")
            print("Item crafted!")
        else:
            print("Insufficient materials.")
def search():
    item = input("What item do you want to see if you have? : ")
    if item in inventory:
        print("You have the item.")
    else:
        print("You do not have a", item)


def drop_item():
    item = input("What item do you want to drop? : ")
    if item in inventory:
        inventory.remove(item)
        print("Item dropped.")
    else:
        print("You do not have this item.")


def look():
    slot = int(input("Which inventory slot do you want to look at? : ")) - 1 # Added -1 for user friendliness, slot 1 is no longer the number "0" etc
    if slot < len(inventory):
        print("You have a", inventory[slot], "in slot", slot)
    else:
        print("Invalid slot.")


def choose_action():
    print("You have", len(inventory), "items in your inventory.")
    action = input("What action do you want to take? (add/craft/look/drop/search) : ")
    match action:
        case "add":
            add_item()
        case "craft":
            craft_item()
        case "drop":
            drop_item()
        case "look":
            look()
        case "search":
            search()            
    print()


# -------------------------
# Main program
# -------------------------
inventory = ["sword", "shield"]
while True:
    choose_action()
