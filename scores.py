import sys

scores = [85, 90, 78, 92]

if not all(isinstance(score, (int, float)) for score in scores):
    print("Error: All scores must be numeric.")
    sys.exit(1)

total = sum(scores)
average = total / len(scores) if scores else 0

print(f"Scores: {scores}")
print(f"Total Score: {total}")
print(f"Average Score: {average:.2f}")