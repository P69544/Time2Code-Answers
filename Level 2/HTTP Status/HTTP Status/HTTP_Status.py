
# HTTP status codes program

# -------------------------
# Subprograms
# -------------------------
def http_status(status):
    if code == 400:
        return "Bad request"
    elif code == 401 | 403:
        return "Authentication error"
    elif code == 404:
        return "Not found"
    else:
        return "Unknown error"


# -------------------------
# Main program
# -------------------------
code = int(input("Enter error code: "))
print(http_status(code))
