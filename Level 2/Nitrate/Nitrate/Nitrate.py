# Nitrate program

# -------------------------
# Subprograms
# -------------------------
def calculate_dose(nitrate):
    if nitrate > 10:
        return 3
    elif nitrate > 2.5:
        return 2
    elif nitrate > 1:
        return 1
    elif nitrate <= 1:
        return 0.5
    else:
        return "ERROR"


# -------------------------
# Main program
# -------------------------
nitrate = float(input("Enter level of nitrate: "))
carbon_dose = str(calculate_dose(nitrate))
print("For", nitrate, "nitrate dose", carbon_dose, "ml of carbon.")
