# ini file program

# -------------------------
# Subprograms
# -------------------------
def input_settings():
    try:
        file = open("settings.ini","r")
    except FileNotFoundError:
        print("File not found.")
        return
    info = file.readlines()
    for line in info:
        line = line.split("=")
        if len(line) == 1:
            pass
        else:
            if line[0] == "name":
                lmb = line[1].strip("\n").strip(" ")
            elif line[0] == "server":
                server = line[1].strip("\n").strip(" ")
            elif line[0] == "port":
                port = line[1].strip("\n").strip(" ")
    file.close()
    print("Last modified by:",lmb)
    print("IP Address:",server)
    print("Port number:",port)

# -------------------------
# Main program
# -------------------------
input_settings()
