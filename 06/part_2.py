import numpy as np


def do_stuff(line, grid):
    instr = line.split()
    if instr[0] == "turn":
        x1, y1 = map(int, instr[2].split(","))
        x2, y2 = map(int, instr[4].split(","))
        if instr[1] == "on":
            grid[x1 : x2 + 1, y1 : y2 + 1] += 1
        elif instr[1] == "off":
            grid[x1 : x2 + 1, y1 : y2 + 1] -= 1
    elif instr[0] == "toggle":
        x1, y1 = map(int, instr[1].split(","))
        x2, y2 = map(int, instr[3].split(","))
        grid[x1 : x2 + 1, y1 : y2 + 1] += 2
    grid[grid < 0] = 0


with open("puzzle_input.txt", "r") as f:
    lines = [line.strip() for line in f]

grid = np.zeros((1000, 1000), dtype=int)
print("grid:", len(grid), len(grid[1]))

for line in lines:
    do_stuff(line, grid)

print(np.sum(grid))
