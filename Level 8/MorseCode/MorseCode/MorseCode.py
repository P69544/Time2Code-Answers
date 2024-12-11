# Morse code program

# -------------------------
# Subprograms
# -------------------------
def translate(morse):
    match morse:
        case ".-":
            return "A"
        case "-...":
            return "B"
        case "-.-.":
            return "C"
        case "-..":
            return "D"
        case ".":
            return "E"
        case "..-.":
            return "F"
        case "--.":
            return "G"
        case "....":
            return "H"
        case "..":
            return "I"
        case ".---":
            return "J"
        case "-.-":
            return "K"
        case ".-..":
            return "L"
        case "--":
            return "M"
        case "-.":
            return "N"
        case "---":
            return "O"
        case ".--.":
            return "P"
        case "--.-":
            return "Q"
        case ".-.":
            return "R"
        case "...":
            return "S"
        case "-":
            return "T"
        case "..-":
            return "U"
        case "...-":
            return "V"
        case ".--":
            return "W"
        case "-..-":
            return "X"
        case "-.--":
            return "Y"
        case "--..":
            return "Z"
        case _:
            return " "


def read_morse(filename):
    result = []
    try:
        file = open(filename,"r")
    except FileNotFoundError:
        print("Error : File not found.")
        return None
    text = file.read().split(" ")
    print(text)
    for item in text:
        if item == "/":
            result.append(" ")
        else:
            letter = translate(item)
            result.append(letter)
    return "".join(result)


# -------------------------
# Main program
# ------------------------- 
message = read_morse("message.txt")
print(message)

