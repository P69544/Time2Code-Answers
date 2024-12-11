# This program will display the 480 most popular movies of all time

# ----------------
# Subprograms
# ----------------
def display_header():
  layout = "| {:<48} | {:^4} | {:<8} | {:^27} | {:^11} | {:^18} |"
  print(layout.format("Name", "Year", "WWG ($m)", "WWG Inflation Adjusted ($m)", "Budget ($m)", "x Budget Recovered"))
  print ("-"*135)
  
def display_movies():
  layout = "| {:<48} | {:^4} | {:^8} | {:^27} | {:^11} | {:^18} |"
  with open("movie_statistics.tsv", "r") as movie_file_data:
    for line in movie_file_data:
      line = line.strip()
      movie_data_list = line.split("\t")
      print(layout.format(movie_data_list[0], movie_data_list[7], movie_data_list[1], movie_data_list[2], movie_data_list[5], movie_data_list[4])) 
# ----------------
# Main Program
# ----------------
print("*** 480 TOP MOST PROFITABLE MOVIES ***")
print()
display_header()
display_movies()
input()