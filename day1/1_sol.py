with open("1_input.txt") as fin:
    dates = [
        int(line) for line in fin.readlines()
    ]

couples = set()
for date in dates:
    for date2 in dates:
        if date + date2 == 2020:
            couples.add((date, date2))

for (date1, date2) in couples:
    print(date1, date2, date1*date2)
