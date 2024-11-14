# Palindrome program

# -------------------------
# Subprograms
# -------------------------
def palindrome(phrase):
    phraseList = []
    phrase = ''.join(char for char in phrase if char.isalnum()).upper()
    
    for char in phrase:
        phraseList.append(char)
    reverseList = phraseList; reverseList.reverse()
    
    if reverseList == phraseList:
        return True
    else:
        return False

# -------------------------
# Main program
# -------------------------
phrase = input("Enter your palindrome: ")
isPalindrome = palindrome(phrase)

if isPalindrome:
    print(phrase,"is a palindrome!")
else:
    print(phrase,"is not a palindrome!")