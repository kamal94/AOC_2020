import sys
import re
import itertools

lines = [l.strip() for l in sys.stdin if l.strip()]
mem = {}
masks = []
def get_masks(line):
    ix = [i.start() - 7 for i in re.finditer(r'X', line)]
    masks = []
    # print(line)
    perms = itertools.product('10', repeat=len(ix))
    # print(perms)
    for p in perms:
        # print(p)
        m = ['1' if a=='1' else 'X' for a in line[-36:]]
        for index, char in zip(ix, p):
            m[index] = char
        # print(''.join(m))
        masks.append(''.join(m))
    # print(masks)
    return masks

def get_val(line):
    result = re.search(r"^mem\[(\d+)\] = (\d+)$", line)
    return int(result.group(1)), int(result.group(2))

for l in lines:
    if l[:4] == "mask":
        masks = get_masks(l)
        continue
    loc, val = get_val(l)
    # print(len(masks))
    for m in masks:
        zm = 0
        om = 0
        def get_mask(m):
            zm = int(''.join('1' if a=="0" else "0" for a in m[-36:]), 2)
            om = int(''.join('1' if a=="1" else "0" for a in m[-36:]), 2)
            return zm, om
        zm, om = get_mask(m)
        new_loc = loc | om
        new_loc = new_loc & (~zm)
        # new_loc = m | loc
        # print(m, loc, new_loc)
        mem[new_loc] = val
    # print("*"*10)
    # mem[] = [val|m for m in masks]

# print(mem)

print(sum(mem.values()))
