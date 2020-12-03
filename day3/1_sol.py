import sys
lines = []
for line in sys.stdin:
    lines.append(line.strip())

h = len(lines)
w = len(lines[0])
slopes = [
    (1,1),
    (1,3),
    (1,5),
    (1,7),
    (2,1)
]
answers = []
for (h_increment, w_increment) in slopes:
    depth = 0
    width = 0
    trees = 0
    # print(lines)
    while depth < h:
        # if (width % w)-3 < 0 and (width % w)+2 > 0:
        #     print("here")
        #     print(lines[depth][(width % w)-3:]+lines[depth][:(width % w)+2])
        # else:
        #     print(lines[depth][(width % w)-3:(width % w)+2])
        if lines[depth][width % w] == "#":
            trees += 1
            # print(depth, width)
        depth += 1
        width += 3
    answers.append(trees)

from functools import reduce

print(reduce((lambda x,y: x*y), answers))
