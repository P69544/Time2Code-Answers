# School club program

# -------------------------
# Subprograms
# -------------------------
def add_student():
    club = ""
    print("Clubs available : Programming, Drama and Football")
    while club not in ["PROGRAMMING", "DRAMA", "FOOTBALL"]:
        club = input("Enter club of your choice: ").upper()
    filename = club.lower()+".txt"
    student = input("Enter your name to sign up for the club: ")
    student = student + "\n"
    file = open(filename, "a")
    file.write (student)
    file.close()
    print("You have been signed up", student)


def show_students():
    club = ""
    print("Clubs available : Programming, Drama and Football")
    while club not in ["PROGRAMMING", "DRAMA", "FOOTBALL"]:
        club = input("Enter club to view: ").upper()
    print("Students that signed up for the",club.lower(),"club:")
    filename = club.lower()+".txt"
    file = open(filename, "r")
    for student in file:
        student = student.strip()
        print(student)
    file.close()
    
    
def menu():
    print("1. Sign up")
    print("2. Show students")
    choice = ""
    while choice not in ["1", "2"]:
        choice = input("Enter choice: ")
    match choice:
        case "1":
            add_student()
        case "2":
            show_students()
            
            
# -------------------------
# Main program
# -------------------------
menu()
