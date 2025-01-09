# This program will ...

# ----------------
# Subprograms
# ----------------
def saveQuestions(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    questions = []
    for line in lines:
        newline = line.strip("\n")
        newline = newline.split(",")
        questions.append(newline)
    file.close()
    return questions

# ----------------
# Main program
# ----------------
FILENAME = "questions.txt"

questions = saveQuestions(FILENAME)
score = 0

for question in questions:
    print(question[0])
    answer = question[1]
    guess = input("Enter true or false: ").lower()
    if answer == guess:
        score += 1
        print("Correct!")
    else:
        print("Incorrect, it was",answer+"!")
print("Your score was:",score,"/ 10!")