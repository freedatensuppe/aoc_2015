floor = 0

with open("puzzle_input.txt", "r") as f:
    floors = f.read()

for i, f in enumerate(floors):
    if f == "(":
        floor += 1
    if f == ")":
        floor -= 1
    if floor < 0:
        print(i + 1)
        break
