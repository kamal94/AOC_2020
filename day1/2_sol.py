with open("1_input.txt") as fin:
    dates = sorted([
        int(line) for line in fin.readlines()
    ])

couples = set()
for date in dates:
    done = False
    for date2 in dates:
        if done:
            break
        for date3 in dates:
            sum = date + date2 + date3
            if sum == 2020:
                couples.add((date, date2, date3))
            elif sum > 2020:
                done = True
                break

for (date1, date2, date3) in couples:
    print(date1, date2, date3, date1*date2*date3)
