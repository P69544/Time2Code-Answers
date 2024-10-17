# Feud program

# -------------------------
# Variables / Arrays
# -------------------------
validHerbs = ["dandelion", "burdock", "pipewort", "ragwort", "snapdragon", "toadflex"]
validSpells = ["teleport", "protect", "sprites"]
spellRecipes = [["teleport", "dandelion", "burdock"],["protect","pipewort","ragwort"],["sprites","snapdragon","toadflex"]]
inventory = [] 

# -------------------------
# Subprograms
# -------------------------
def forage_herb():
    t = []
    print("Choices: ")
    for herb in validHerbs:
        t.append(herb+"\n")
    print("".join(t))
    
    herbChoice = input("Enter Herb to Forage: ").lower()
    if herbChoice not in validHerbs:
        print("Cannot find herb")
    else:
        print(herbChoice,"added to inventory!")
        inventory.append(herbChoice)

def cauldron(spell, herbs):
    herbsFound = 0
    for herb in herbs:
        if herb in inventory:
            herbsFound += 1
            
    if herbsFound == 2:
        print("Crafting,",spell+"!")
        for herb in herbs:
            inventory.remove(herb)
        inventory.append(spell)
    else:
        print("Missing a required herb.")
    

def brew_spell():
    t = []
    print("Choices: ")
    for spell in validSpells:
        t.append(spell+"\n")
    print("".join(t)) 
    
    toBrew = input("Enter spell you wish to brew: ")
    
    if toBrew in validSpells:
        for recipe in spellRecipes:
            if toBrew == recipe[0]:
                herbsNeeded = []
                herbsNeeded.append(recipe[1])
                herbsNeeded.append(recipe[2])
        cauldron(toBrew, herbsNeeded)
    else:
        print("Spell not found.")

def cast_spell():
    toCast = input("Enter spell you wish to cast: ")
    if toCast in validSpells and toCast in inventory:
        print(toCast,"has been casted!")
        inventory.remove(toCast)
    elif toCast in validSpells and toCast not in inventory:
        print("You do not have that spell.")
    else:
        print("Invalid spell.")

def take_action():
    validInputs = ["F","B","C"]
    
    selection = ""
    while selection not in validInputs:
        selection = input("\nForage (F), Brew (B), or Cast (C)?: ")[0].upper()
        
    if selection == "F":
        forage_herb()
    elif selection == "B":
        brew_spell()
    elif selection == "C":
        cast_spell()
    else:
        print("Error?")

# -------------------------
# Main program
# -------------------------
#        
while True:
    print("Inventory:",inventory)
    take_action()