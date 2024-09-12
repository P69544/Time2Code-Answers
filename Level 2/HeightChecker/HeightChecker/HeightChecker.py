# A program where the user can input their height and be informed of another object that is their height
# ----------------
# Subprograms
# ----------------
def check_height(height):
    if height < 80:
        print("You're not yet tall enough to use this height checker.")
    elif height >= 80 and height < 90:
        print("You are about the same height as a snooker table, which is roughly 80cm tall!")
    elif height >= 90 and height < 100:
        print("You are about the same height as the UK's Royal Sceptre, which is roughly 92cm tall!")
    elif height >= 100 and height < 110:
        print("You are about the same height as an Olympic hurdle in the men's high hurdle event, which is 106.7cm tall!")
    elif height >= 110 and height < 120:
        print("You are about the same height as a wild turkey, which is roughly 115cm tall!")
    elif height >= 120 and height < 130:
        print("You are about the same height as an emperor penguin, which is roughly 120cm tall!")
    elif height >= 130 and height < 140:
        print("You are about the same height as a hippo, which is roughly 130cm tall!")
    elif height >= 140 and height < 150:
        print("You are about the same height as a UK postbox, which is 140cm tall!")
    elif height >= 150 and height < 160:
        print("You are about the same height as a gorilla, which is roughly 150cm tall!")
    elif height >= 160 and height < 170:
        print("You are about the same height as the average annual rainfall in Thailand, which is 162.2cm!")
    elif height >= 170 and height < 180:
        print("You are about the same height as computing pioneer Alan Turing, who is believed to have been roughly 170cm tall!")
    else:
        print("You are too tall to use this height checker.")
# ----------------
# Main program
# ----------------
print("Welcome to the height checker!")
user_height = int(input("Enter your height to the nearest centimetre: "))
check_height(user_height)