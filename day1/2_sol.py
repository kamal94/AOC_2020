with open("1_input.txt") as fin:
    dates = fin.readlines()

couples = set()
for date in dates:
    for date2 in dates:
        for date3 in dates:
            if int(date) + int(date2) + int(date3) == 2020:
                couples.add((date, date2, date3))

for (date1, date2,date3) in couples:
    print(date1, date2, date3, int(date1)*int(date2)*int(date3))
