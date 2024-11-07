# Caesar cipher program

# -------------------------
# Subprograms
# -------------------------
def encrypt_message(message):
    key = 5
    encrypted_message = ""
    for character in message:
        ascii_code = ord(character)
        ascii_code = ascii_code + key
        if ascii_code > 126:
            ascii_code = 32 + ascii_code - 127
        encrypted_message = encrypted_message + chr(ascii_code)
    return encrypted_message 

def decrypt_message(message):
    key = 5
    decrypted_message = ""
    for character in message:
        realchar = character
        realchar = chr(ord(character) - key)
        decrypted_message = decrypted_message + realchar
    return decrypted_message

# -------------------------
# Main program
# -------------------------
actual_message = input("Enter a message: ")
stored_message = encrypt_message(actual_message)
decrypted_message = decrypt_message(stored_message)
print("Message to send:", stored_message)
print("Message decrypted to:", decrypted_message)
