# A program to: 

# ----------------
# Subprograms
# ----------------
def seconds(age):
    return age * 31557600

def minutes(age):
   return age * 525960

def hours(age):
    return age * 8766

def days(age):
    return age * 365.25

def weeks(age):
    return age * 52

def months(age):
    return age * 12

# ----------------
# Main program
# ----------------
age = int(input("Enter your age in years: "))
print("You are", months(age), "months old, ", weeks(age), "weeks old, ", days(age), "days old, ", hours(age), "hours old, ", minutes(age), "minutes old, and ", seconds(age), "seconds old!")