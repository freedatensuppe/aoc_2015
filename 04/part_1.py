import hashlib

with open("puzzle_input.txt", "r") as f:
    key = str(f.read().strip())


for i in range(10_000_000):
    s = key + str(i)
    res = hashlib.md5(s.encode())
    if res.hexdigest()[:5] == "00000":
        print(s)
        print(i)
        break
