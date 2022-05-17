def read_matrix(r_count):
    matrix = []
    for _ in range(r_count):
        matrix.append(list(input()))
    return matrix


def find_paths(lab, row, col, path, direction):
    if row < 0 or row >= len(lab) or col < 0 or col >= len(lab[0]):
        return

    if lab[row][col] == '*' or lab[row][col] == 'v':
        return

    path.append(direction)

    if lab[row][col] == 'e':
        print(''.join(path))
        path.pop()
        return

    lab[row][col] = 'v'
    
    find_paths(lab, row, col - 1, path, 'L')       # Left
    find_paths(lab, row, col + 1, path, 'R')       # Right
    find_paths(lab, row - 1, col, path, 'U')       # Up
    find_paths(lab, row + 1, col, path, 'D')       # Down

    lab[row][col] = '-'
    path.pop()


rows_count = int(input())
column_count = int(input())
labyrinth = read_matrix(rows_count)

find_paths(labyrinth, 0, 0, [], '')
