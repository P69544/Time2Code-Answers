# Find and replace program

# -------------------------
# Subprograms
# -------------------------
def replace(x, y, l):
    for index in range(0,len(l)):
        if l[index] == x:
            l[index] = y
    return l

def output(l):
    for word in l:
        print(word)
         
# -------------------------
# Main program
# -------------------------
rhyme = ["roly", "poly", "roly", "poly", "up", "up", "up", 
         "roly", "poly", "roly", "poly", "down", "down", "down"]

output(rhyme)
toReplace = input("Enter word to replace: ")
replaceWith = input("Enter word to replace with: ")
replace(toReplace, replaceWith, rhyme)
output(rhyme)