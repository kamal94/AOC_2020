import sys
ids = []
for line in sys.stdin:
    line = line.strip()
    if line == "":
        continue
    row_start, row_end = 0, 127
    col_start, col_end = 0, 7
    for i in range(7):
        if line[i] == "F":
            row_end = (row_start + row_end)//2
        else:
            row_start = ((row_start + row_end)//2) +1
        # print(row_start, row_end)
        
    assert row_start == row_end
    for i in range(3):
        if line[7+i] == "L":
            col_end = (col_start + col_end) // 2
        else:
            col_start = ((col_start + col_end) // 2) + 1
    assert col_start == col_end

    idd = row_start*8 + col_start
    print(line, row_start, col_start, idd)
    ids.append(idd)

for idd in ids:
    for id2 in ids:
        if abs(idd - id2) == 2:
            print(idd, id2)

# Shame, Shame, Shame
# thre's a mathematical solution somewhere here.
sorted_ids = sorted(ids)
prev = sorted_ids[0]
for i in range(1, len(sorted_ids)):
    if sorted_ids[i] == prev + 2:
        print("sol:")
        print(prev, sorted_ids[i])
    prev = sorted_ids[i]
print(len(ids))
