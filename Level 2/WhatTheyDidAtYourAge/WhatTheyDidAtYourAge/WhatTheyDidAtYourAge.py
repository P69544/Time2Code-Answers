# A program to:

# ----------------
# Subprograms
# ----------------
def age_achievement_checker(age):
    if age < 8 or age > 16:
        print("We don't have anyone of your age on our list, but remember it's never too late to do something amazing and never too early to start trying!")
    elif age == 8:
        print("At age 8, three-time Olympic gold medal winner Wilma Rudolph walked for the first time.")
    elif age == 9:
        print("At age 9, Mozart began composing symphonies.")
    elif age == 10:
        print("At age 10, Stevie Wonder was signed by Motown records.")
    elif age == 11:
        print("At age 11, Victoria van Meter was the first girl to fly across the United States.")
    elif age == 12:
        print("At age 12, Steven Spielberg got his first movie camera.")
    elif age == 13:
        print("At age 13, Jordan Romero became the youngest person to summit Mount Everest.")
    elif age == 14:
        print("At age 14, Laura Dekker sailed around the world solo.")
    elif age == 15:
        print("At age 15, Hanson Crockett Gregory claims to cut the centre out a doughnut to make the first ring doughnut.")
    elif age == 16:
        print("At age 16, Lana del Rey released her first album, 'Born to Die'")
    
# ----------------
# Main program
# ----------------
print("Welcome to 'WHAT THEY DID AT YOUR AGE!'")      
user_age = int(input("Enter your age: "))
age_achievement_checker(user_age)