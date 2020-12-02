import sys
import re

count = 0
for line in sys.stdin:
    match = re.search(r"(\d+)-(\d+) ([a-z]): (.+)", line)
    mi = int(match.group(1))
    ma = int(match.group(2))
    char = match.group(3)
    password = match.group(4)
    occurances = len([c for c in password if c == char])
    if mi <= occurances <= ma:
        count += 1
        print(line)
print(count)
