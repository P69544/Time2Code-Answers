
# Microscopy program

# -------------------------
# Subprograms
# -------------------------
def magnification(actual_size, image_size):
    magnification = (image_size * 10000) / actual_size
    return magnification

# -------------------------
# Main program
# -------------------------
actual_size = int(input("Enter actual size (micrometers): "))
image_size = int(input("Enter image size (centimeters): "))
mag = magnification(actual_size, image_size)
print("The magnification is", mag ,"X")
