import sys

count = 0
answered = set()
for line in sys.stdin:
    line = line.strip()
    if line == "":
        print(len(answered))
        count += len(answered)
        answered = set()
        continue
    answered = answered.union({a for a in line})

if answered:
    print(len(answered))
    count += len(answered)
    answered = set()
print(count)
