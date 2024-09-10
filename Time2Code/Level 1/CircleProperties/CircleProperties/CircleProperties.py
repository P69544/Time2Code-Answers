# Circle properties program

# -------------------------
# Subprograms
# -------------------------
def circle_area(diameter):
    radius = diameter/2
    area = 3.14 * (radius * radius)
    return area

def circle_circumference(diameter):
    area = 3.14 * diameter
    return area

# -------------------------
# Main program
# -------------------------
diameter = float(input("Enter circle diameter:"))
area = circle_area(diameter)
circumference = circle_circumference(diameter)
print("Area: ", area)
print("Circumference: ", circumference)