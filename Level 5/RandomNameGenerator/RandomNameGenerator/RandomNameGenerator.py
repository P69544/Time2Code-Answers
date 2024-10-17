# Random name generator program

# -------------------------
# Import libraries
# -------------------------
import random


# -------------------------
# Subprograms
# -------------------------
# Function to return a random name
def generate_name():
    forenames =  ["Muhammad", "Noah", "Jack", "Lily", "Sophia", "Olivia"]
    surnames = ["Wang", "Smith", "Devi", "Jones", "Kim", "Rodriguez"]
    
    forename = forenames[random.randint(0,len(forenames)-1)]
    surname = surnames[random.randint(0,len(surnames)-1)]
    
    return(forename+" "+surname)
    
# -------------------------
# Main program
# -------------------------
print(generate_name())
