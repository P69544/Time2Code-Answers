# Times tables program

# -------------------------
# Subprograms
# -------------------------
# Procedure to output the X times table.
def times_table(x):
    for mult in range(1, 13):
        result = x*mult
        print(x,"x",mult,"=",result)

# -------------------------
# Main program
# -------------------------
table = -1
while table > 12 or table < 1:
    table = int(input("Table to output (1-12): "))

times_table(table)
