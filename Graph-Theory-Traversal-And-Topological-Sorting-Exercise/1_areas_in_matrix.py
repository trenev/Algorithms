def dfs(key, row, col, matrix, visited):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    if visited[row][col]:
        return
    if not matrix[row][col] == key:
        return

    visited[row][col] = True

    dfs(key, row + 1, col, matrix, visited)
    dfs(key, row - 1, col, matrix, visited)
    dfs(key, row, col + 1, matrix, visited)
    dfs(key, row, col - 1, matrix, visited)


rows = int(input())
cols = int(input())

matrix = []
visited = []
areas = {}
areas_count = 0

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

for row in range(rows):
    for col in range(cols):
        if not visited[row][col]:
            key = matrix[row][col]
            dfs(key, row, col, matrix, visited)

            if key not in areas:
                areas[key] = 0
            
            areas[key] += 1
            areas_count += 1

print(f'Areas: {areas_count}')
[print(f"Letter '{k}' -> {v}") for (k, v) in sorted(areas.items(), key=lambda x: x[0])]

