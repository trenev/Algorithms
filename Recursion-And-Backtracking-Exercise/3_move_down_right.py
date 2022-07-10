def possible_paths(rows, cols, r, c):
    if r >= rows or c >= cols:
        return 0

    if r == rows - 1 and c == cols - 1:
        return 1
    
    result = 0
    result += possible_paths(rows, cols, r, c + 1)       # Right
    result += possible_paths(rows, cols, r + 1, c)       # Down

    return result


rows = int(input())
cols = int(input())

print(possible_paths(rows, cols, 0, 0))
