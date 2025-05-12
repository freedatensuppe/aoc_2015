with open("puzzle_input.txt", "r") as f:
    moves = f.read()

houses = set()
current = [0, 0]
houses.add(tuple(current))

for move in moves[::2]:
    if move == ">":
        current[0] += 1
    if move == "<":
        current[0] -= 1
    if move == "^":
        current[1] += 1
    if move == "v":
        current[1] -= 1
    houses.add(tuple(current))

current = [0, 0]

for move in moves[1::2]:
    if move == ">":
        current[0] += 1
    if move == "<":
        current[0] -= 1
    if move == "^":
        current[1] += 1
    if move == "v":
        current[1] -= 1
    houses.add(tuple(current))

print(len(houses))
