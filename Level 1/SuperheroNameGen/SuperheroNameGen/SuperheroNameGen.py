# A program to generate a superhero name

# ----------------
# Subprograms
# ----------------
def generateName(animal, adjective, verb):
    name = str("The "+adjective+" "+verb+" "+animal)
    return name
  
# ----------------
# Main program
# ----------------

# welcome statement
print("Welcome to the Superhero Name Generator!")

# takes 2 inputs, an adjective and animal
user_adjective = str(input("Enter an adjective (describing word): "))
user_animal = str(input("Enter your favourite species of animal: "))
user_verb = str(input("Enter your favourite verb ending with -ing: "))
name = generateName(user_animal, user_adjective, user_verb)
print("Your superhero name is", name)