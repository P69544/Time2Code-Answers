# A program to calculate the average height of the giraffes in a zoo

# ----------------
# Constants
# ----------------

GIRAFFE_HEIGHTS = [5.5, 4.95, 5.25, 5.6, 4.3, 4.2, 4.75, 1.7, 1.9]

# ----------------
# Subprograms
# ----------------
def find_average_height(height_list):
  total_giraffe_height = 0
  number_of_giraffes = len(height_list)
  
  for height in height_list:
    total_giraffe_height += height
  
  average_height = total_giraffe_height/number_of_giraffes
  return average_height
# ----------------
# Main program
# ----------------
average = find_average_height(GIRAFFE_HEIGHTS)
print("Average height:",round(average,2))