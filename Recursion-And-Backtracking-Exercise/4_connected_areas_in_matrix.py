class Area:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def find_area(r, c, matrix):
    if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]):
        return 0

    if not matrix[r][c] == '-':
        return 0

    matrix[r][c] = 'v'
    result = 1

    result += find_area(r, c + 1, matrix)
    result += find_area(r, c - 1, matrix)
    result += find_area(r + 1, c, matrix)
    result += find_area(r - 1, c, matrix)

    return result


rows = int(input())
cols = int(input())
matrix = []
areas = []

for _ in range(rows):
    matrix.append(list(input()))

for row in range(rows):
    for col in range(cols):
        size = find_area(row, col, matrix)
        if size > 0:
            areas.append(Area(row, col, size))

print(f'Total areas found: {len(areas)}')
for ind, area in enumerate(sorted(areas, key=lambda x: x.size, reverse=True)):
    print(f'Area #{ind + 1} at ({area.row}, {area.col}), size: {area.size}')
