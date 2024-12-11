# Cookies program

# -------------------------
# Subprograms
# -------------------------
def read_cookie():
    file = open("preferences.txt","r")
    for line in file.readlines():
        if "theme = " in line.lower():
            return line
    file.close()
    return "??"

def write_cookie(theme):
    file = open("preferences.txt","w")
    file.write(theme)
    file.close()

def change_theme(theme):
    if "light" in theme:
        write_cookie("theme = dark")
    else:
        write_cookie("theme = light")


# -------------------------
# Main program
# -------------------------
theme = read_cookie()
print("The current", theme)
changeRequest = input("Do you wish to change your theme? Y/N: ").upper()[0]
if changeRequest == "Y":
    print("Changing..")
    change_theme(theme)
