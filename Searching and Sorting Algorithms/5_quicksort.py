def quick_sort(start, end, nums):
    if start >= end:
        return

    pivot_inx = start
    left_inx = start + 1
    right_inx = end

    while left_inx <= right_inx:
        if nums[left_inx] > nums[pivot_inx] and nums[right_inx] < nums[pivot_inx]:
            nums[left_inx], nums[right_inx] = nums[right_inx], nums[left_inx]
        
        if nums[left_inx] <= nums[pivot_inx]:
            left_inx += 1

        if nums[right_inx] >= nums[pivot_inx]:
            right_inx -= 1

    nums[pivot_inx], nums[right_inx] = nums[right_inx], nums[pivot_inx]
    
    quick_sort(start, right_inx - 1, nums)
    quick_sort(left_inx, end, nums)


nums = [int(x) for x in input().split()]
quick_sort(0, len(nums) -1, nums)
print(*nums)
