scores = []
for i in range (5) :
    Enter_Score = (input(f"Enter Score {i+1}: "))
    Score = float(Enter_Score)
    scores.append(Score)

print("All Scores :", (scores))
print("Highest Score :", max(scores))
print("Lowest Score :", min(scores))
print("Average Score :", sum(scores))