# Fizz buzz program

# -------------------------
# Subprograms
# -------------------------
def fizz_buzz(x):
    for number in range(1,x+1):
        if number%3 == 0 and number%5 == 0:
            print("FizzBuzz")
        elif number%3 == 0:
            print("Fizz")
        elif number%5 == 0:
            print("Buzz")
        else:
            print(number)

# -------------------------
# Main program
# -------------------------
number = int(input("Enter number to count to: "))
fizz_buzz(number)