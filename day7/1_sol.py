import sys ,re 

combs = {}

s = r"^(.+) bags contain (no other bags.|(\d+ .+ bags?)+\.)$"
a = "faded blue bags contain no other bags."

print(re.search(s,a).groups())
for line in sys.stdin:
    line = line.strip()
    result = re.search(s, line)
    if len([a for a in result.groups() if a is not None]) > 2:
        ins = []
        for bags in result.groups()[1].split(","):
            color = re.search(r"\d+ (.+) bag", bags)
            ins.append(color.group(1))
        combs[result.groups()[0]] = ins
    else:
        combs[result.groups()[0]] = None


from pprint import pprint
pprint(combs)
to_search = ["shiny gold"]
carries = set()
while to_search:
    searching = to_search.pop()
    for bag, content in combs.items():
        if content is None:
            continue
        if searching in content and bag not in carries:
            print("found", searching, "in", bag, content)
            to_search.append(bag)
            carries.add(bag)

print(carries)
print(len(carries))
