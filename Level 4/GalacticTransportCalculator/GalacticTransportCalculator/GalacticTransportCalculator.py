# ---------- Libraries ----------

# ---------- Subprograms ----------
def calculateFare(startZone, endZone):
    baseFare = 5
    farePerZone = 2.5
    zonesTravelled = endZone - startZone
    fare = 5 + (farePerZone * zonesTravelled)
    return "%.2f" % round(fare, 2)

# ---------- Main Program ----------
print("Welcome to the Galactic Transport Fare calculator! You wish to leave your home planet and travel through space to forge your own way...")

startZone = int(input("Starting Zone: "))
endZone = int(input("Ending Zone: "))

fare = calculateFare(startZone, endZone)

print("The fare from zone",str(startZone),"to",str(endZone),"is $"+str(fare))