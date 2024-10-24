# Voting count program

# -------------------------
# Subprograms
# -------------------------
def count_votes(ballot):
    voteA, voteB, voteC, voteD = 0,0,0,0
    
    for vote in ballot:
        if vote == "A":
            voteA += 1
        elif vote == "B":
            voteB += 1
        elif vote == "C":
            voteC += 1
        elif vote == "D":
            voteD += 1
            
    results = [voteA, voteB, voteC, voteD]
    return results
                
# -------------------------
# Main program
# -------------------------
votes = ["A", "B", "B", "B", "B", "C", "C", "D", "A", "B",
         "A", "B", "A", "B", "D", "B", "C", "B", "B", "A"]

result = count_votes(votes)
print("Answer A:", result[0])
print("Answer B:", result[1])
print("Answer C:", result[2])
print("Answer D:", result[3])
