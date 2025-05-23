bad_strings = ["ab", "cd", "pq", "xy"]
vowels = ["a", "e", "i", "o", "u"]
alpha = "abcdefghijklmnopqrstuvwxyz"
double_chars = " ".join("".join(x) for x in zip(alpha, alpha)).split()


def has_vowels(s):
    count = 0
    for a in s:
        if a in vowels:
            count += 1
        if count > 2:
            return True
    return False


def double_letters(s):
    for d in double_chars:
        if d in s:
            return True
    return False


def no_bad_strings(s):
    for b in bad_strings:
        if b in s:
            return False
    return True


def isnice(s):
    if has_vowels(s) and double_letters(s) and no_bad_strings(s):
        return True
    return False


with open("puzzle_input.txt", "r") as f:
    lines = [line.strip() for line in f]

s = 0

for line in lines:
    if isnice(line):
        s += 1

print(s)
