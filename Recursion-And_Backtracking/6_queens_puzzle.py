CHESSBOARD_SIZE = 8

attacked_cols = set()
attacked_left_diagonals = set()
attacked_right_diagonals = set()

counter = []


def can_place_queen(r, c):
    return (c not in attacked_cols and (r - c) not in attacked_left_diagonals and
            (r + c) not in attacked_right_diagonals)


def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def put_queens(matrix, row):
    if row >= len(matrix):
        counter.append(1)
        print_board(matrix)
        return

    for col in range(len(matrix)):
        if can_place_queen(row, col):
            attacked_cols.add(col)
            attacked_left_diagonals.add(row - col)
            attacked_right_diagonals.add(row + col)
            matrix[row][col] = '*'

            put_queens(matrix, row + 1)

            attacked_cols.remove(col)
            attacked_left_diagonals.remove(row - col)
            attacked_right_diagonals.remove(row + col)
            matrix[row][col] = '-'


board = [['-' for i in range(CHESSBOARD_SIZE)] for y in range(CHESSBOARD_SIZE)]
put_queens(board, 0)

print(len(counter))
