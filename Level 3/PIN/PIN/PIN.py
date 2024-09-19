# PIN program

# -------------------------
# Subprograms
# -------------------------
def get_pin():
    CORRECT_PIN = 7528
    pin = int(input("Enter your pin: "))
    
    if pin == CORRECT_PIN:
        return True
    else:
        return False

# -------------------------
# Main program
# -------------------------
attempts = 3
cont = True

while cont:
    correct = get_pin()

    if not correct:
        attempts -= 1
        #print("Incorrect PIN, Attempts Left:",str(attempts))
        if attempts <= 0:
            print("Out of attempts. Locked out.")
            cont = False
    else:
        print("Security check passed.")
        cont = False