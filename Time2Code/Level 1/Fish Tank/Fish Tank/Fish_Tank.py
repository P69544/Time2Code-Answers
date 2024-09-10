
# Fish tank volume problem

# -------------------------
# Subprograms
# -------------------------
def volume(length, width, height):
    vol = (length * width * height) / 1000
    return vol # Calculates and returns volume to variable

def litres_to_gallons(litres):
    gallons =  litres / 4.546
    return gallons # Calculates and returns gallons to variable

# -------------------------
# Main program
# -------------------------
length = int(input("Enter length of fish tank: "))
width = int(input("Enter width of fish tank: "))
height = int(input("Enter height of fish tank: "))
litres = volume(length, width, height) # Calculates litres using previous variables
gallons = litres_to_gallons(litres) # Converts the litres to gallons
print("A", length, "x", width, "x", height, "cm tank is", litres, "litres and", gallons, "imperial gallons.")
