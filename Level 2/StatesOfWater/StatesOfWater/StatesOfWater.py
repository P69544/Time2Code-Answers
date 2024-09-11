# States of water program

# -------------------------
# Subprograms
# -------------------------
def water_state(centigrade):
    if temperature <= 0:
        return "solid"
    elif temperature < 100:
        return "liquid"
    else:
        return "gaseous"


# -------------------------
# Main program
# -------------------------
temperature = float(input("Enter water temp"))
state = water_state(temperature)
print("The water is in a", state, "state.")
