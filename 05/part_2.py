import re

alpha = "abcdefghijklmnopqrstuvwxyz"
char_pairs = set()

for i in alpha:
    for j in alpha:
        p = i + j
        q = j + i
        char_pairs.add(p)
        char_pairs.add(q)


def has_pair(s: str) -> bool:
    for i in char_pairs:
        if i in s:
            t = s.replace(i, "__", 1)
            if i in t:
                #                print("pair:", i, t)
                return True
    return False


def has_repitition(s: str) -> bool:
    for i in alpha:
        restr = i + "[a-zA-Z]" + i
        t = re.search(restr, s)
        if t is not None:
            #            print("rep:", t)
            return True
    return False


with open("puzzle_input.txt", "r") as f:
    lines = [line.strip() for line in f]


nice_count = 0

for line in lines:
    print()
    print(line)
    print()
    if has_pair(line) and has_repitition(line):
        nice_count += 1

print(nice_count)
