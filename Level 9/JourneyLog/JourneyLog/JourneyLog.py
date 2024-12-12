# Journey log program

# -------------------------
# Subprograms
# -------------------------
def add_chapter():
    book.append([])


def add_story(chapter, entry):
    book[chapter].append(entry)


def output():
    log = 1
    for chapter in range(1, len(book)):
        print("-- CHAPTER "+str(chapter)+" --")    
        for entry in book[chapter]:
            print("Log", log, ":", entry)
            log = log + 1

def save_log():
     with open("log.txt","w") as logFile:
         logFile.write("")
     with open("log.txt","a") as logFile:
         for chapter in range(len(book)):
             if chapter != 0:
                logFile.write("-- CHAPTER "+str(chapter)+" --\n")
                for line in book[chapter]:
                     if line != "":
                        logFile.write(str(line+"\n"))
    
# -------------------------
# Main program
# -------------------------
book = [[]]
add_chapter()
add_story(1, "I find myself alone on a strange world, unequipped and in danger. I have no memory of how I got here, no sense of a before.")
add_story(1, "My Exosuit at least seems to know what it's doing, and I am not dead yet...")
add_chapter()
add_story(2, "I received a set of mysterious coordinates from an unknown source.")
add_story(2, "I followed the signal, and found the wreckage of an abandoned starship.")
add_story(2, "There was little to be gained from the wreck, but the distress beacon contained the hailing frequency labelled 'ARTEMIS'.")
output()
save_log()
