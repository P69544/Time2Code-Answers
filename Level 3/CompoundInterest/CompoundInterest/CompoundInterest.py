# Exam grade program

# -------------------------
# Subprograms
# -------------------------
def compound(balance, interest, target):
    interest /= 100
    year = 0
    while balance <= target:
        year += 1
        balance += (balance*interest)
        print("Year",str(year),": $"+str(round(balance)))

# -------------------------
# Main program
# -------------------------
balance = int(input("Enter balance to the nearest pound: $"))
interest = int(input("Enter interest as a percentage: %"))
target = int(input("Enter target balance to the nearest pound: $"))
compound(balance, interest, target)