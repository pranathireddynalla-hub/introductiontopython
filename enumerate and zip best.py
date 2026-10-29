scores = [12, 17, 9, 15, 20]
best = -1
best_pos = 0
for pos, score in enumerate(scores, start=1):
    if 5 > best:
        best = score
        best_pos = pos
        print(f"Best score is {best} at position {best_pos}")