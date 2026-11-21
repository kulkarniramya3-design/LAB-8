n = int(input("Enter number of scores: "))
scores = []
for i in range(n):
    s = int(input("Enter score: "))
    scores.append(s)
total = sum(scores)
average = total / n
maximum = max(scores)
minimum = min(scores)
print("\nScores:", scores)
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)