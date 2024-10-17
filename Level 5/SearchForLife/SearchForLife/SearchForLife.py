# Search for life program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
def probe(planet):    
    creature = ["lizards", "humanoids", "insects"]
    colour = ["red", "green", "blue"]
    characteristic = ["shy", "angry", "docile"]
    climate = ["hot", "frozen", "barren", "temperate"]
    random.seed(planet)
    
    lifeform = creature[random.randint(0,2)]
    specimen = colour[random.randint(0,2)]
    behaviour = characteristic[random.randint(0,2)]
    weather = climate[random.randint(0, 3)]
    
    report = ""
    if weather == "temperate":
        report = specimen
        report = report+", "+behaviour
        report = report+" "+lifeform
        report = report+" on a "+weather+" planet."
    else:
        report = "a "+weather+" planet with no signs of life."
    return report
    
    
# -------------------------
# Main program
# -------------------------
planet = int(input("Enter the catalogue number of a planet: "))
report = probe(planet)
print("Probes report",report)
