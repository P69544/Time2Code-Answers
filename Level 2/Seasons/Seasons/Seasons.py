
# Seasons program

# -------------------------
# Subprograms
# -------------------------
def seasons(month):
    match month:
        case "December" | "January" | "February" | "12" | "1" | "2":
            return "Winter"
        case "March" | "April" | "May" | "3" | "4" | "5":
            return "Spring"
        case "June" | "July" | "August" | "6" | "7" | "8":
            return "Summer"
        case "September" | "October" | "November" | "9" | "10" | "11":
            return "Autumn"
        case _:
            return "Error"


# -------------------------
# Main program
# -------------------------
month = str(input("Enter the month: "))
season = seasons(month)
print("Month", month, "is in the", season)
