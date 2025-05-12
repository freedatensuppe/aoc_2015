s = 0

with open("puzzle_input.txt", "r") as f:
    lines = [line.strip() for line in f]

for line in lines:
    dims = line.split("x")
    l, w, h = sorted([int(d) for d in dims])
    s += 2 * l * w + 2 * w * h + 2 * h * l + l * w

print(s)
