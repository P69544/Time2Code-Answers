# Rainfall collector program

# -------------------------
# Subprograms
# -------------------------
def read_data(filename):
    num_regions = 7
    data = [["" for columns in range(2)] for rows in range(num_regions)]
    file = open(filename, "r")
    for region in range(num_regions):
        data_row = file.readline()
        data_row = data_row.strip()
        data_list = data_row.split(",")
        data[region][0] = data_list[0]
        data[region][1] = data_list[1]
    file.close()
    return data


def padded_label(label, characters):
    return label + " " * (characters - len(label)) 
    
    
def output_table(data):
    num_regions = 7
    characters = 0
    for region in range(num_regions):
        if len(data[region][0]) > characters:
            characters = len(data[region][0])
    for region in range(num_regions):
        table_row = padded_label(data[region][0], characters)
        table_row = table_row + " | "
        table_row = table_row + data[region][1]
        print(table_row)
    print()

def output_short_table(data):
    num_regions = 7
    characters = 0
    for region in range(num_regions):
        region_label = short_label(data[region][0])
        if len(region_label) > characters:
            characters = len(region_label)
    for region in range(num_regions):
        region_label = short_label(data[region][0])
        table_row = region_label
        table_row += " " * (characters - len(region_label))
        table_row += " | "
        table_row += data[region][1]
        print(table_row)

def short_label(label):
    region_label_list = label.split(" ")
    region_label = " "
    for word in region_label_list:
        region_label += word[0]
    return region_label
# -------------------------
# Main program
# -------------------------
data = read_data("data.txt")
output_table(data)
output_short_table(data)