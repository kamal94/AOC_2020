import sys
max_idd = 0
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
    if idd > max_idd:
        max_idd = idd
print(max_idd)
