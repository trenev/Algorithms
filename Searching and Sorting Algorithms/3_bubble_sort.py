nums = [int(x) for x in input().split()]

end_index = len(nums)
is_sorted = True

while is_sorted:
    is_sorted = False

    for inx in range(1, end_index):
        if nums[inx] < nums[inx - 1]:
            nums[inx], nums[inx - 1] = nums[inx - 1], nums[inx]
            is_sorted = True
    
    end_index -= 1

print(*nums)
