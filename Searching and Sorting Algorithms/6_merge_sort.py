# def merge_arrays(left, right):
#     result = [None] * (len(left) + len(right))
#     left_index = 0
#     right_index = 0
#     result_index = 0

#     while len(left) > left_index and len(right) > right_index:
#         if left[left_index] > right[right_index]:
#             result[result_index] = right[right_index]
#             right_index += 1
#         else:
#             result[result_index] = left[left_index]
#             left_index += 1

#         result_index += 1

#     while len(left) > left_index:
#         result[result_index] = left[left_index]
#         left_index += 1
#         result_index += 1

#     while len(right) > right_index:
#         result[result_index] = right[right_index]
#         right_index += 1
#         result_index += 1

#     return result


# def split_array(nums):
#     if len(nums) < 2:
#         return nums

#     mid_index = len(nums) // 2
#     left = nums[:mid_index]
#     right = nums[mid_index:]
    
#     return merge_arrays(split_array(left), split_array(right))


# nums = [int(x) for x in input().split()]
# print(*split_array(nums))


def merge_sort(arr):
    if len(arr) > 1:
        mid_index = len(arr) // 2
        left = arr[:mid_index]
        right = arr[mid_index:]

        merge_sort(left)
        merge_sort(right)

        left_index = 0
        right_index = 0
        arr_index = 0

        while len(left) > left_index and len(right) > right_index:
            if left[left_index] > right[right_index]:
                arr[arr_index] = right[right_index]
                right_index += 1
            else:
                arr[arr_index] = left[left_index]
                left_index += 1

            arr_index += 1

        while len(left) > left_index:
            arr[arr_index] = left[left_index]
            left_index += 1
            arr_index += 1

        while len(right) > right_index:
            arr[arr_index] = right[right_index]
            right_index += 1
            arr_index += 1
    
    return arr      


nums = [int(x) for x in input().split()]
merge_sort(nums)
print(*nums)
