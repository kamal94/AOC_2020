import sys

lines = []

for line in sys.stdin:
    lines.append([line.strip(), False])

from pprint import pprint

pprint(lines)
no_line = 0
acc = 0
while True:
    # print(lines[no_line])
    if lines[no_line][1]:
        print(acc)
        break
    lines[no_line][1] = True
    # print(lines[no_line])
    np, num = lines[no_line][0].split()
    if np == "nop":
        no_line += 1
        continue
    elif np == "acc":
        acc += int(num)
        no_line += 1
    elif np == "jmp":
        no_line += int(num)

