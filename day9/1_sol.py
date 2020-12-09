import sys

nums = [int(num) for num in sys.stdin]
wl = 25

def can(num, nums):
    for i in nums:
        for j in nums:
            if i == j:
                continue
            if j + i == num:
                return True
    return False

for i in range(wl, len(nums)):
    if not can(nums[i], nums[i-wl:i]):
        print(i, nums[i])
        break

