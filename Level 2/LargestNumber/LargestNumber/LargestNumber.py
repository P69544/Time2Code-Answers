# Largest number program

# -------------------------
# Subprograms
# -------------------------
def largest(number1, number2, number3):
    if (number1 == number2) and (number1 == number3):
        return "1"
    elif (number1 > number2) and (number1 > number3):
        return "1"
    elif (number2 > number1) and (number2 > number3):
        return "2"
    else:
        return "3"


# -------------------------
# Main program
# -------------------------
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
print("The largest is number", largest(number1, number2, number3))
