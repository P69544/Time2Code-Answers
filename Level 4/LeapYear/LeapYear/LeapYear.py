# Leap year program

# -------------------------
# Subprograms
# -------------------------
def is_leap_year(year):
    #Returns True if the year is a leap year or False if it is not.
    #If the year is exactly divisible by four it is a leap year...
    if year % 4 == 0:
        a = True
        if (year % 100 == int(year % 100)):
            a = False
        if (year % 400 == int(year % 400)):
            a = True
        else:
            a = False
    else:
        a = False
    return a
    #unless it is divisible by one hundred in which case it is not a leap year...
    #although any year that is divisible by four hundred is a leap year.

# -------------------------
# Main program
# -------------------------

while True:    
    year = int(input("Year: "))
    if is_leap_year(year):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
