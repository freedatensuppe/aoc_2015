s = 0

with open("puzzle_input.txt", "r") as f:
    lines = [line.strip() for line in f]

for line in lines:
    dims = line.split("x")
    l, w, h = sorted([int(d) for d in dims])
    s += 2 * l + 2 * w + l * w * h

print(s)
