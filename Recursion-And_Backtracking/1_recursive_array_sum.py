def solution(arr, index):
    if index == len(arr) - 1:
        return arr[index]

    return arr[index] + solution(arr, index + 1)


arr = list(map(int, input().split()))
print(solution(arr, 0))
