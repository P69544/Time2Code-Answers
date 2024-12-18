# Grade book program

# -------------------------
# Subprograms
# -------------------------
def read_grade_book(filename):
    global grade_book
    with open(filename,"r") as file:
        for record in file:
            record = record.strip()
            fields = record.split(",")
            grade_book.append(fields)

def output_assignment():
    global grade_book
    choice = 0
    while choice < 1 or choice > 3:
        choice = int(input("Which unit do you wish to output results for?"))
    for student in grade_book:
        toPrint = []
        toPrint.append(student[0]+" "); toPrint.append(student[1]+": ") # Student's name
        unit = choice+1
        toPrint.append(student[unit])
        print("".join(toPrint))

              
# -------------------------
# Main program
# -------------------------
grade_book = []
read_grade_book("gradebook.txt")
output_assignment()