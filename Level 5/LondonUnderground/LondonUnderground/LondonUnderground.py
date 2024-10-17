# London Underground program

# -------------------------
# Subprograms
# -------------------------
def get_station():
    choice = ""
    while choice not in stations:
        choice = input("Enter A Station: ")
        if choice not in stations:
            print("Invalid Station.")
    return choice

def calculate_stops(choiceList):
    stationA = stations.index(choiceList[0])
    stationB = stations.index(choiceList[1])
    
    if stationB > stationA:
        return stationB - stationA
    else:
        return stationA - stationB
    
# -------------------------
# Main program
# -------------------------
# Victoria line
stations = ["Brixton", "Stockwell", "Vauxhall", "Pimlico", "Victoria", "Green Park", "Oxford Circus", "Warren Street", "Euston", "King's Cross", "Highbury & Islington", "Finsbury Park", "Seven Sisters", "Tottenham Hale", "Blackhorse Road", "Walthamstow Central"]

stationA = get_station()
stationB = get_station()

choices = [stationA, stationB]
distance = calculate_stops(choices)

if distance == 1:
    print(stationA,"to",stationB,"will be in 1 stop.")
else:
    print(stationA,"to",stationB,"will be in",str(distance),"stops.")