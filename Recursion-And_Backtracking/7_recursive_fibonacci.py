'''
With memorization
'''

fibonacci_memo = {}

def get_fibonacci(n):
    if n <= 1:
        return 1

    if n not in fibonacci_memo:
        fibonacci_memo[n] = get_fibonacci(n - 1) + get_fibonacci(n - 2)

    return fibonacci_memo[n]


input_number = int(input())
print(get_fibonacci(input_number))
