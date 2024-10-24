# Twelve days of Christmas program

# -------------------------
# Subprograms
# -------------------------
def output_song():
    days = ["first", "second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth"]
    gifts = ["a partridge in a pear tree", "two turtle doves","three french hens","four calling birds","five gold rings","six geese a-laying","seven swans a-swimming","eight maids a-milking","nine ladies dancing","ten lords a-leaping","eleven pipers piping","twelve drummers drumming"]

    count = 0
    for day in days:
        count += 1
        print("On the",day,"day of christmas\nMy true love gave to me")
        for index in range(count,0,-1):
            if index == 1 and count != 1:
                print("and",gifts[index-1])
            else:
                print(gifts[index-1])
        print()
                
# -------------------------
# Main program
# -------------------------
output_song()