
# Temperature converter program

# -------------------------
# Subprograms
# -------------------------
def c_to_f(centigrade):
    farenheit = (centigrade * 1.8) + 32 # Converting to farenheit by multiplying by 1.8 nd then adding 32 on top
    return farenheit
# -------------------------
# Main program
# -------------------------
centigrade = int(input("Enter Centigrade: "))
fahrenheit = c_to_f(centigrade) # Calls c_to_f to convert values
print(centigrade, "degrees Centigrade is", fahrenheit, "degrees Fahrenheit.")
