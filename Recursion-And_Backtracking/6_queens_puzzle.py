CHESSBOARD_SIZE = 8

attacked_cols = set()
attacked_left_diagonals = set()
attacked_right_diagonals = set()


def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def can_place_queen(r, c):
    return (c not in attacked_cols and (r - c) not in attacked_left_diagonals and
            (r + c) not in attacked_right_diagonals)


def set_queen(r, c):
    attacked_cols.add(c)
    attacked_left_diagonals.add(r - c)
    attacked_right_diagonals.add(r + c)
    board[r][c] = '*'


def remove_queen(r, c):
    attacked_cols.remove(c)
    attacked_left_diagonals.remove(r - c)
    attacked_right_diagonals.remove(r + c)
    board[r][c] = '-'


def put_queens(matrix, row):
    if row >= CHESSBOARD_SIZE:
        print_board(matrix)
        return

    for col in range(CHESSBOARD_SIZE):
        if can_place_queen(row, col):
            set_queen(row, col)
            put_queens(matrix, row + 1)
            remove_queen(row, col)


board = [['-' for _ in range(CHESSBOARD_SIZE)] for _ in range(CHESSBOARD_SIZE)]
put_queens(board, 0)
