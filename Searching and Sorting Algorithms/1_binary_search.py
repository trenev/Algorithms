def binary_search(nums, target):
    start_inx = 0
    end_inx = len(nums) - 1
    
    while start_inx <= end_inx:
        mid_inx = (start_inx + end_inx) // 2

        if nums[mid_inx] == target:
            return mid_inx
        if nums[mid_inx] < target:
            start_inx = mid_inx + 1
        else:
            end_inx = mid_inx - 1
    
    return -1


nums = [int(x) for x in input().split()]
target = int(input())

print(binary_search(nums, target))
