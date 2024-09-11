# Currency converter program

# -------------------------
# Subprograms
# -------------------------
def exchange(gbp, currency):
    if currency == "usd":
        return gbp * 1.3
    elif currency == "euro":
        return gbp * 1.11
    elif currency == "yuan":
        return gbp * 8.92
    elif currency == "yen":
        return gbp * 138.44
    else:
        print("Currency not valid.")

# -------------------------
# Main program
# -------------------------
gbp = float(input("Enter GBP: "))
currency = str(input("Enter currency you wish to convert to (USD, Euro, Yuan, Yen): ")).lower()
money = exchange(gbp, currency)
print(gbp, "GBP =", money, currency)
