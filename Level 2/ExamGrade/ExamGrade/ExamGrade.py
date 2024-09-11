# Exam grade program

# -------------------------
# Subprograms
# -------------------------
def grade(mark):
    if mark >= 80:
        return 9
    elif mark >= 67:
        return 8
    elif mark >= 54:
        return 7
    elif mark >= 41:
        return 6
    elif mark >= 31:
        return 5
    elif mark >= 22:
        return 4
    elif mark >= 13:
        return 3
    elif mark >= 4:
        return 2
    elif mark >= 2:
        return 1
    else:
        return "U"

def marks_needed(marks):
    if mark >= 80:
        return 0
    elif mark >= 67:
        return 80 - marks
    elif mark >= 54:
        return 67 - marks
    elif mark >= 41:
        return 54 - marks
    elif mark >= 31:
        return 41 - marks
    elif mark >= 22:
        return 31 - marks
    elif mark >= 13:
        return 22 - marks
    elif mark >= 4:
        return 13 - marks
    elif mark >= 2:
        return 4 - marks
    else:
        return 2 - marks
    
# -------------------------
# Main program
# -------------------------
mark = int(input("Enter your marks on the exam 0-100: "))
grade = grade(mark)
marksNeeded = marks_needed(mark)
print("A mark of", mark,"achieves a grade", grade)
print("You need", marksNeeded, "more marks to achieve the next grade")