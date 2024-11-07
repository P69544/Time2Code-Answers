# Teacher code program

# -------------------------
# Subprograms
# -------------------------
from types import NoneType


def tcode(teacher):
    lenChoice = int(input("Enter amount of letters to output: "))
    letters = ["", ""]
    letters[0] = teacher[0]
    space = teacher.find(" ")
    teacher = teacher.replace("'","")
    letters[1] = teacher[space + 1: space + lenChoice]
    teacher_code = "".join(letters)
    teacher_code = teacher_code.upper()
    return teacher_code
 

# -------------------------
# Main program
# -------------------------
teacher = input("Enter the name of the teacher: ")
teacher_code = tcode(teacher)
print(teacher_code)
