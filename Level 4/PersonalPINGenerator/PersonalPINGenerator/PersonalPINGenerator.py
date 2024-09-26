# ----------------
# Import libraries
# ----------------
import random
# ----------------
# Subprograms
# ----------------
def generate_pin(birthday):
  random.seed(birthday)
  pin = random.randint(1000, 9999)
  return pin
# ----------------
# Main program
# ----------------
birthday = int(input("Enter your birthday (in the form DDMMYYYY): "))

pin = generate_pin(birthday)
print("Your PIN is", pin)