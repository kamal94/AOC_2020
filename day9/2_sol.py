import sys

nums = [int(line) for line in sys.stdin]

target = 675280050

mi = 0
ma = 0
total = 0
while ma < len(nums):
    total = sum(nums[mi:ma])
    if total == target:
        print(nums[mi:ma])
        print(mi,ma)
        print(min(nums[mi:ma] )+ max(nums[mi:ma]))
        break
    if total < target:
        ma += 1
    else:
        mi += 1
