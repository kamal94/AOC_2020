import sys
from copy import deepcopy

lines = []

for line in sys.stdin:
    lines.append([line.strip(), False])


def ends(instructions):
    no_line = 0
    acc = 0
    while no_line <= len(instructions) - 1:
        # print(instructions[no_line])
        if instructions[no_line][1]:
            # print("cycle on", no_line, instructions[no_line])
            return False
        instructions[no_line][1] = True
        # print(instructions[no_line])
        np, num = instructions[no_line][0].split()
        if np == "nop":
            no_line += 1
            continue
        elif np == "acc":
            acc += int(num)
            no_line += 1
        elif np == "jmp":
            no_line += int(num)
    print(acc)
    return True


for idx, line in enumerate(lines):
    instructions = deepcopy(lines)
    np, num = instructions[idx][0].split()
    if np == "jmp":
        instructions[idx] = ["nop " + num, False]
    if np == "nop":
        instructions[idx] = ["jmp " + num, False]
    from pprint import pprint

    # pprint(instructions)
    # print("changed line", idx, line, "to", instructions[idx][0])
    if ends(instructions):
        break
