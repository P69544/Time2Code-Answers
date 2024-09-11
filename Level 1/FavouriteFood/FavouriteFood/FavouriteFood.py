# This program will ask the user to enter their favourite food, then assign it to a variable and display it

# ----------------
# Subprograms
# ----------------
def favourite_food(newFood): #Defining subprogram
  food = newFood # Example of a string
  print(food)
  
def favourite_animal(newAnimal): #Defining subprogram
  animal = newAnimal # Example of a string
  print(animal)

# ----------------
# Main program
# ----------------
food = str(input("Enter favourite food: ")) 
animal = str(input("Enter favourite animal: ")) 
favourite_food(food) # Calling subprogram
favourite_animal(animal)