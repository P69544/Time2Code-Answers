# Shopping list program

# -------------------------
# Subprograms
# -------------------------
def add_item():
    new_item = input("Enter the item to add to the list: ")
    file = open("shopping.txt","r")
    f = file.readlines()
    if new_item+"\n" not in f:
        file.close()
        file = open("shopping.txt", "a")
        new_item = new_item + "\n"
        file.write(new_item)
        file.close()
    else:
        file.close()
        print("Item already in the list!")
    

def output_items():
    try:
        file = open("shopping.txt", "r")
    except FileNotFoundError:
        file = open("shopping.txt", "w")
        file.close()
    else:
        print("-----------------------------")
        for item in file:
            item = item.strip()
            print(item)
        file.close()
        print("-----------------------------")


def sort_items():
    try:
        file = open("shopping.txt", "r")
    except FileNotFoundError:
        file = open("shopping.txt", "w")
        file.close()
    else:
        item_list = []
        for item in file:
            item = item.strip()
            item_list.append(item)
        file.close()
        item_list.sort()
        file = open("shopping.txt", "w")
        for item in item_list:
            item = item + "\n"
            file.write(item)
        file.close()

def clearList():
    file = open("shopping.txt","w")
    file.write("")
    file.close()
    
def menu():
    choice = ""
    while choice != "4":
        print("1. Add item")
        print("2. Output shopping list")
        print("3. Sort list")
        print("4. Clear list")
        print("5. Quit")
        while choice not in ["1", "2", "3", "4", "5"]:
            choice = input("Enter choice: ")
        match choice:
            case "1":
                add_item()
                choice = ""
            case "2":
                output_items()
                choice = ""
            case "3":
                sort_items()
                choice = ""
            case "4":
                clearList()
                choice = ""
            case "5":
                return
                
                
# -------------------------
# Main program
# -------------------------
menu()
