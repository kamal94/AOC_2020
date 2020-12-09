from pprint import pprint
import sys
import re

combs = {}

s = r"^(.+) bags contain (no other bags.|(\d+ .+ bags?)+\.)$"
a = "faded blue bags contain no other bags."

print(re.search(s, a).groups())
for line in sys.stdin:
    line = line.strip()
    result = re.search(s, line)
    if len([a for a in result.groups() if a is not None]) > 2:
        ins = []
        for bags in result.groups()[1].split(","):
            color = re.search(r"(\d+) (.+) bag", bags)
            ins.append((int(color.group(1)), color.group(2)))
        combs[result.groups()[0]] = ins
    else:
        combs[result.groups()[0]] = None


pprint(combs)
to_search = ["shiny gold"]


def count(bag):
    if combs[bag] == None:
        return 1
    total = 0
    for num, name in combs[bag]:
        total += count(name) * num
    return total + 1


carries = set()
print(count("shiny gold") - 1)
