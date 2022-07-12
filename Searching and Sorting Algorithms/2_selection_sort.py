nums = [int(x) for x in input().split()]

for inx in range(len(nums)):
    min_index = inx
    min_number = nums[inx]

    for i in range(inx + 1, len(nums)):
        if nums[i] < min_number:
            min_index = i
            min_number = nums[min_index]

    nums[inx], nums[min_index] = nums[min_index], nums[inx]

print(*nums)
