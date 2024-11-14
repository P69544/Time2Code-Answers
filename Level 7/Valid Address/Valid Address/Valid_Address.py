# Valid Address program

# -------------------------
# Subprograms
# -------------------------
def validate_address(email):
    splitIndex = email.find("@")
    if splitIndex <= 3:
        return False
    
    prefix = email[:splitIndex]
    domain = email[splitIndex+1:]
    
    # Prefix - Allowed characters: letters (a-z), numbers, underscores, periods, and dashes.
    # An underscore, period, or dash must be followed by one or more letter or number.
    prefixWhitelist = ["-","_","."]
    lastChar = prefix[len(prefix)-1:]
    if not lastChar.isalnum():
        return False
    
    for char in range(len(prefix)):
        if not(prefix[char].isalnum()):
            if prefix[char] in prefixWhitelist:
                if not prefix[char+1].isalnum():
                    return False
            if prefix[char] not in prefixWhitelist:
                return False
    
    # Domain - Allowed characters: letters, numbers, hyphen or period.
    # The domain must be at least three characters, for example: .com, .org, .cc
    domainWhitelist = ["-","."]
    
    if len(domain) < 3:
        return False
    
    urlSplitter = domain.find(".")
    if urlSplitter != -1:
        if (len(domain) - urlSplitter) < 3:
            return False
    
    for char in range(len(domain)):
        if not(domain[char].isalnum()):
            if domain[char] in domainWhitelist:
                if not domain[char+1].isalnum():
                    return False
            if domain[char] not in domainWhitelist:
                return False
    return True
    
    
# -------------------------
# Main program
# -------------------------
email = input("Enter your email address: ")
valid = validate_address(email)
if valid:
    print("This email is valid!")
else:
    print("This email is invalid.")
