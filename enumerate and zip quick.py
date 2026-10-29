answers = ["b", "a", "c", "b", "a", "c", "b", "a", "c", "b"]
correct = ["b", "c", "d", "c"]
score=0
for diven, right in zip(answers, correct):
    if diven == right:
        score += 1
        total = len(answers)
        print(f"Score: {score}/4")