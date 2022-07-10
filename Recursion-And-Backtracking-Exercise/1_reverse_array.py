def reverse_array(array, index):
    if len(array) <= 1:
        return array[0]

    if index >= len(array) // 2:
        return

    tmp_idx = len(array) - index - 1
    array[index], array[tmp_idx] = array[tmp_idx], array[index]
    reverse_array(array, index + 1)
    
    return ' '.join(array)


arr = input().split(' ')
print(reverse_array(arr, 0))
