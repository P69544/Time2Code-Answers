# Measurements program

# -------------------------
# Subprograms
# -------------------------
def feet_to_inches(feet):
    return feet * 12

def inches_to_feet(inches):
    return inches / 12

def menu():
    valid = False
    print("What do you want to do?:"
          +"\n1. Convert Feet to Inches"
          +"\n2. Convert Inches to Feet"
          +"\n3. Exit Program")
    
    while not valid:
        selection = int(input("Selection: "))
        if selection >= 1 and selection <= 3:
            valid = True
        else:
            valid = False
    return selection

def converter():
    selection = menu()
    if selection == 1:
        feet = float(input("Enter Feet to convert: "))
        print("Result: "+str(feet_to_inches(feet)))
        return True
    elif selection == 2:
        inches = float(input("Enter Inches to convert: "))
        print("Result: "+str(inches_to_feet(inches)))
        return True
    else:
        print("Goodbye.")
        return False
# -------------------------
# Main program
# -------------------------
running = True

while running:
    print()
    running = converter()