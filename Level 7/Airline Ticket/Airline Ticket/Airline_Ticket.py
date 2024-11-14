# Airline ticket program

# -------------------------
# Subprograms
# -------------------------
# Function to return truncated airport names
def airports(departure, arrival):
    departure = departure[:4].upper()
    arrival = arrival[:4].upper()
    return (departure+"-"+arrival)

# -------------------------
# Main program
# -------------------------
print(airports("Gatwick", "Amsterdam"))
