# Denary to binary program

# -------------------------
# Subprograms
# -------------------------
def den_to_bin(number):
    binary = ""
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2
    return binary


def den_to_oct(number):
    octal = ""
    while number > 0:
        remainder = number % 8
        octal = str(remainder) + octal
        number = number // 8
    return octal

def den_to_hex(number):
    hexa = ""
    while number > 0:
        remainder = number % 16
        digit = remainder
        match remainder:
            case 10:
                digit = "A"
            case 11:
                digit = "B"
            case 12:
                digit = "C"
            case 13:
                digit = "D"
            case 14:
                digit = "E"
            case 15:
                digit = "F"
        hexa = str(digit) + hexa
        number = number // 16
    return hexa
        
# -------------------------
# Main program
# -------------------------
number = int(input("Enter the denary number to convert: "))
print("Binary:", den_to_bin(number))
print("Octal:", den_to_oct(number))
print("Hex:", den_to_hex(number))
