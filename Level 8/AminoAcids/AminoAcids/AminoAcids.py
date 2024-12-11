# Amino acids program

# -------------------------
# Subprograms
# -------------------------
def get_amino_acid():
    acid = ""
    while len(acid) != 3:
        acid = input("Enter amino acid: ").upper()
    return acid

def check_sequence(acid):
    try:
        file = open("dna.txt")
    except FileNotFoundError:
        return -1
    else:
        count = 0
        for line in file:
            line = line.strip()
            for index in range(0, len(line), 3):
                sequence = line[index] + line[index+1] + line[index+2]
                if sequence == acid:
                    count += 1
        file.close()
    return count
# -------------------------
# Main program
# -------------------------
acid = get_amino_acid()
result = check_sequence(acid)
if result == -1:
    print("File not found.")
else:
    print("The acid",acid,"appears in the sequence",result,"times.")