floor = 0

with open("puzzle_input.txt", "r") as f:
    floors = f.read()

for f in floors:
    if f == "(":
        floor += 1
    if f == ")":
        floor -= 1

print(floor)
