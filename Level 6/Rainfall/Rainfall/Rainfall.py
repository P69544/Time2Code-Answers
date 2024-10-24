# Rainfall program

# -------------------------
# Subprograms
# -------------------------
from multiprocessing import Value


def analyse1(data):
    count = 0
    norain = 0
    total = 0
    highest = 0
    
    for value in data:
        if value > highest:
            highest = value
        if value == 0:
            norain += 1
        count += 1
        total += value
    average = total/count
    return norain, round(average,2), highest


def analyse2(data):
    count = 0
    norain = 0
    total = 0
    highest = 0
    
    for index in range(len(data)):
        if data[index] == 0:
            norain += 1
        if data[index] > highest:
           highest = data[index]
        count += 1
        total += data[index]
    average = total/count
    return norain, round(average,2), highest


# -------------------------
# Main program
# -------------------------
daily_rainfall_mm = [0.1, 0.0, 0.2, 0.4, 0.1, 0.0, 0.0,
                     0.0, 0.3, 0.3, 0.2, 0.0, 0.0, 0.1]

print("Analyse1:")
count, average, highest = analyse1(daily_rainfall_mm)
print("Days with no rain:",count)
print("Average:",average)
print("Highest:",highest)

print("\nAnalyse2:")
count, average, highest = analyse2(daily_rainfall_mm)
print("Days with no rain:",count)
print("Average:",average)
print("Highest:",highest)