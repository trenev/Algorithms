nums = [int(x) for x in input().split()]

for inx in range(1, len(nums)):
    for i in range(inx, 0, -1):
        if nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
        else:
            break

print(*nums)
