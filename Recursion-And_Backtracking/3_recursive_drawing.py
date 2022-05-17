def drawing(n):
    if n <= 0:
        return

    print(n * '*')
    drawing(n - 1)
    print(n * '#')


input_number = int(input())
drawing(input_number)

