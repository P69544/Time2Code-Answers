# Disemvowel program

# -------------------------
# Subprograms
# -------------------------
def dvowel(message):
    vowels = ["A","E","I","O","U"]
    msgList = []
    for char in message:
        if char.upper() not in vowels:
            msgList.append(char)
    newMsg = "".join(msgList)
    return ("The disemvoweled message is: "+newMsg)

# -------------------------
# Main program
# -------------------------
message = input("Enter your message: ")
print(dvowel(message))
