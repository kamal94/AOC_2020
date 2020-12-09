import sys
from functools import reduce

count = 0
answered = []
for line in sys.stdin:
    line = line.strip()
    if line == "":
        print(len(reduce(lambda a, b: a.intersection(b), answered)))
        count += len(reduce(lambda a, b: a.intersection(b), answered))
        answered = []
        continue
    answered.append({a for a in line})

if answered:
    print(len(reduce(lambda a, b: a.intersection(b), answered)))
    count += len(reduce(lambda a, b: a.intersection(b), answered))
    answered = set()
print(count)
