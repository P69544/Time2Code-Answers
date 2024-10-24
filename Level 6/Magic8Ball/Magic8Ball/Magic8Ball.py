# A program to simulate a magic fortune ball

# ----------------
# Import libraries
# ----------------
import time, random
# ----------------
# Constants
# ----------------

THINKING_PHRASES = ["THIS MIGHT BE DIFFICULT FOR YOU TO HEAR...", "I SHALL CONSULT MY VISIONS...", "THAT IS A FASCINATING QUESTION...", "ALLOW ME TO GIVE THIS SOME THOUGHT..."]


ANSWERS = ["IT IS CERTAIN", "IT IS DECIDEDLY SO", "WITHOUT A DOUBT", "YES, DEFINITELY", "YOU MAY RELY ON IT", "AS I SEE IT, YES", "MOST LIKELY", "OUTLOOK GOOD", "YES.", "SIGNS POINT TO YES", "REPLY HAZY, TRY AGAIN", "ASK AGAIN LATER", "BETTER NOT TELL YOU NOW", 
"CANNOT PREDICT NOW", "CONCENTRATE AND ASK AGAIN", "DON'T COUNT ON IT", "MY REPLY IS NO", "MY SOURCES SAY NO", "OUTLOOK NOT SO GOOD", "VERY DOUBTFUL."]

# ----------------
# Subprograms
# ----------------
def display_text_slowly(text):
    for letter in text:
        print(letter, end=" ", flush=True)
        time.sleep(0.1)
    print()
    
# ----------------
# Main program
# ----------------
display_text_slowly("WELCOME TO THE MAGIC FORTUNE BALL")
display_text_slowly("ENTER YOUR YES/NO QUESTION.")
input("> ")
thinking_phrase = THINKING_PHRASES[random.randint(0,len(THINKING_PHRASES))]
display_text_slowly(thinking_phrase)
display_text_slowly("......")
answer = random.choice(ANSWERS)
display_text_slowly(answer)