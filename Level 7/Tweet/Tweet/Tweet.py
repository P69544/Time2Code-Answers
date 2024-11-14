# Tweet program

# -------------------------
# Subprograms
# -------------------------
def tweets(message, num_chars):
    messagesList = []
    msg = ""

    for count in range(len(message)):
        msg += message[count]
        if (count+1) % num_chars == 0:
            messagesList.append(msg)
            msg = ""
    if msg != "":
        messagesList.append(msg)
    return messagesList
        

# -------------------------
# Main program
# -------------------------
message = input("Enter the message: ")
max_chars = int(input("How many characters per message? :"))
print(tweets(message, max_chars))
