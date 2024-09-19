# Square root program

# -------------------------
# Subprograms
# -------------------------
def sqroot(x):
    root = x
    lastRoot = x-1
    while lastRoot != root:
        lastRoot = root
        root = 0.5 * (root + (x / root))
        print(root)
    return root
# -------------------------
# Main program
# -------------------------
num = float(input("Enter number to root: "))
print("The square root of", num, "is", sqroot(num))
