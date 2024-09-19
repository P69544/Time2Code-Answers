# Cashpoint program

# -------------------------
# Subprograms
# -------------------------
def dispense(amount):
    print("W"+str(amount))
    while (amount) >= 20:
        print("D20")
        amount -= 20
    while (amount) >= 10:
        print("D10")
        amount -= 10
    while (amount) >= 5:
        print("D5")
        amount -= 5

# -------------------------
# Main program
# -------------------------
amount = int(input("Enter amount you wish to withdraw: $"))
dispense(amount)