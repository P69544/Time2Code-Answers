# Dungeon master program

# -------------------------
# Import libraries
# -------------------------
import random

# -------------------------
# Subprograms
# -------------------------
# Function to return if a skill check is passed in DnD5e

def check_skill(skill, modifier, dm_value):
    #Automatic pass: if skill plus modifiers is greater than or equal to the DM value plus 5. No dice is rolled.
    if (skill + modifier) >= (dm_value + 5):
        return "Automatic Pass"
    else:
        roll = random.randint(1, 20)
        print("You rolled a",str(roll))
    #Critical fail: if the roll is a 1.
    if roll == 1:
        return "Critical Fail"
    #Critical success: if the roll is a 20.
    elif roll == 20:
        return "Critical Success"
    #Check passed: if the skill plus roll plus the modifier is greater or equal to the DM value.
    elif (skill + roll + modifier) >= dm_value:
        return "Check passed"
    #Check failed: if the ability plus roll plus the modifier is less than the DM value.
    else:
        return "Check failed"
# -------------------------
# Main program
# -------------------------
skill = -1
while skill <= 0:
    skill = int(input("Enter Positive Integer for Skill: "))
modifier = int(input("Enter Positive or Negative Integer for Modifier: "))
dm_value = float(input("Enter Dungeon Master Value: "))
result = check_skill(skill, modifier, dm_value)
print(result)
