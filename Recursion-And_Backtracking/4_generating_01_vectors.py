def gen01(arr, index):
    if index == len(arr):
        print(''.join(map(str, arr)))
        return
        
    for i in range(2):
        arr[index] = i
        gen01(arr, index + 1)


input_number = int(input())
arr = [0 for i in range(input_number)]
gen01(arr, 0)
