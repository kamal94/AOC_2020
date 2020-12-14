import sys
import re

lines = [l.strip() for l in sys.stdin if l.strip()]
mem = {}
zm = 0
om = 0
def get_mask(line):
    zm = int(''.join('1' if a=="0" else "0" for a in line[-36:]), 2)
    om = int(''.join('1' if a=="1" else "0" for a in line[-36:]), 2)
    return zm, om

def get_val(line):
    result = re.search(r"^mem\[(\d+)\] = (\d+)$", line)
    return int(result.group(1)), int(result.group(2))

for l in lines:
    if l[:4] == "mask":
        zm, om = get_mask(l)
        continue
    loc, val = get_val(l)
    val = val | om
    val = val & (~zm)
    mem[loc] = val 

print(mem)

print(sum(mem.values()))
