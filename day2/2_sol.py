import sys
import re

count = 0
# TODO: i can likely do this inline instead of use a regex.
# but i dont want to parse text rn
for line in sys.stdin:
    match = re.search(r"(\d+)-(\d+) ([a-z]): (.+)", line)
    i1 = int(match.group(1))-1
    i2 = int(match.group(2))-1
    char = match.group(3)
    password = match.group(4)
    if (password[i1] == char) ^ (password[i2] == char):
        count += 1
        print(line)
print(count)
