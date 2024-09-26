# Least common multiple program

# -------------------------
# Subprograms
# -------------------------
def lcm(num1, num2):
    if num1 > num2:
        counter = num1
    else:
        counter = num2
    while not ((counter % num1 == 0) and (counter % num2 == 0)):
        counter += 1
    return counter

# -------------------------
# Main program
# -------------------------
num1 = int(input("Number One: "))
num2 = int(input("Number Two: "))
result = lcm(num1, num2)
print("The LCM of", str(num1),"and",str(num2),"is",str(result))