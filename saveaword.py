with open("text.txt", encoding="utf-8") as f:
    text = f.read().lower()
    for p in ".,!?":
        text = text.replace(p, "")
        words = text.split()
        
        count = {}
        for w in words:
            count[w] = count.get(w, 0) + 1
with open("report.txt", "w", encoding="utf-8") as out:
    out.write(f"word: {len(words)}\n")
    out.write(f"unique: {len(count)}\n")
    for w in sorted(counts):
        out.write(f"{w:<10}: {count[w]}\n")
    print("Report saved")
    

