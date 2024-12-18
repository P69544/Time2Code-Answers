# Checkout program

# -------------------------
# Subprograms
# -------------------------
def read_database():
    database = []
    with open("products.txt","r") as file:
        lines = file.readlines()
        for line in lines:
            newLine = line.split(",")
            database.append(newLine)
    return database

def get_product():
    global products
    valid = False
    choice = 0
    while not valid:
        choice = input("Select Product Number: ")
        valid = True
        if choice == "":
            return -1
        if choice.isnumeric:
            choice = int(choice)
            if choice < 0 or choice > len(products)-1:
                valid = False
            else:
                return choice
                

def output_product(button_number):
    global products # get the global variable for the database
    for product in products:
        if product[0] == str(button_number): # Compare first item in the product list (button number which is a string) to input
            print(product[1], product[2]) # Product name and price

def transaction(products):
    num = 0
    total = 0.0
    while num != -1:
        num = get_product()
        if num != -1:
            output_product(num)
            total += float(products[num][2])
    print("Total: $"+str("%.2f" % total))
        
# -------------------------
# Main program
# -------------------------
products = read_database()
transaction(products)
