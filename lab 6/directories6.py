for i in range(26):
    letter = chr(65 + i)
    with open(f"{letter}.txt", "w") as f:
        f.write(f"{letter}.txt")
        