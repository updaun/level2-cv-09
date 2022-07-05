import sys
nums = dict()
for i in range(10):
    n = int(sys.stdin.readline())
    if n not in nums.keys():
        nums[n] = 1
    else:
        nums[n] += 1
print(int(sum([i*j for i, j in nums.items()])/10))
print(sorted(nums, key=lambda x:nums[x])[-1])