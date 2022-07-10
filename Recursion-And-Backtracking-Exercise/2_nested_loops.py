def gen_vectors(arr, index):
    if index >= len(arr):
        print(*arr)
        return

    for i in range(1, len(arr) + 1):
        arr[index] = i
        gen_vectors(arr, index + 1)


number = int(input())
arr = [None] * number
gen_vectors(arr, 0)