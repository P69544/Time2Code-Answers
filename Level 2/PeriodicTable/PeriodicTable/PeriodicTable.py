# Periodic table program

#Storing all data in a list for easy access and efficiency
elementInfo = [["Lithium", "Li", 6.94, "Alkali"], ["Sodium", "Na", 22.99, "Alkali"], ["Potassium", "K", 39.098, "Alkali"], ["Fluorine", "F", 18.998, "Halogens"], ["Chlorine", "Cl", 35.45, "Halogens"], ["Bromine", "Br", 79.904, "Halogens"]]

# -------------------------
# Subprograms
# -------------------------
def periodic_table(element):
    foundItem = False # For later usage, if the element is not found
    for item in elementInfo: # Checks list made previously
        if item[0].upper() == element.upper() or item[1].upper() == element.upper(): # Checks if element matches index's name or symbol (non case sensitive)
            foundItem = True # Makes foundItem true to show it has found an element
            index = item
            # Prints out data
            print("Element Name: ", index[0])
            print("Element Symbol: ", index[1])
            print("Atomic Weight: ", index[2])
            print("Group: ", index[3])
    if not foundItem:
        print("Element not found.") # Print a message for if the element was not found determined by foundItem
     
# -------------------------
# Main program
# -------------------------
element = str(input("Enter Element Name/Symbol: "))
periodic_table(element)