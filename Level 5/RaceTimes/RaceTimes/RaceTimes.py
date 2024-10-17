# A program to sort and display a list of race times in ascending and descending order.

# ----------------
# Subprograms
# ----------------
def ask_for_times():
  times = []
  add_times = True
  
  while add_times:
    user_input = input("Enter a time, or f when finished: ")
    if user_input == "f":
      add_times = False
    else:
      times.append(float(user_input))
  return times
# ----------------
# Main Program
# ----------------
print("Welcome to the Race Times Sorter!")
print("This program will allow you to enter a list of race times, which it will display to you in ascending and descending order")
print()
times = ask_for_times()
print()
times.sort()
print("Times in ascending order:", times)
times.reverse()
print("Times in descending order:", times)