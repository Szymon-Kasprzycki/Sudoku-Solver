# Sudoku solver

def create_board(resolution):
    board = [[] for _ in range(resolution*3)]
    for index, row in enumerate(board):
        row_values = input(f'Enter the numbers of row number {index+1} (splitted by space): ').split()
        if len(row_values) != resolution*3:
            raise ValueError(f'Row number {index+1} has {len(row_values)} values, but {resolution*3} are required')
        row.extend([int(x) for x in row_values])
    return board


def print_board(board):
    copy = [[str(x) for x in row] for row in board]
    for i in range(len(copy)):
        if i % 3 == 0:
            print('-'*25)
        print(
            '| '
            + ' '.join(copy[i][:3])
            + ' | '
            + ' '.join(copy[i][3:6])
            + ' | '
            + ' '.join(copy[i][6:])
            + ' |'
        )
    print('-'*25)


def is_not_in_row_or_col(board, row, col, num):
    global board_resolution
    return not any(
        board[row][x] == num or board[x][col] == num
        for x in range(board_resolution * 3)
    )


def solve_sudoku(board):
    while are_zeros(board):
        for i, row in enumerate(board):
            for j in range(9):
                if row[j] == 0:
                    poss = check_cell(board, row=i, col=j)
                    xzy = check_square(board, row=i, col=j, possible=poss)
                    if len(xzy) == 1:
                        board[i][j] = xzy[0]
    print_board(board)


def are_zeros(board):
    for i in range(len(board)):
        for j in range(9):
            if str(board[i][j]) == '0':
                return True
    return False


def check_cell(board, row, col):
    return [num for num in range(1, 10) if is_not_in_row_or_col(board, row, col, num)]


def check_square(board, row, col, possible):
    square_start_cell_x = row - row % 3
    square_start_cell_y = col - col % 3
    duplicates = []
    for i in range(3):
        duplicates.extend(
            board[square_start_cell_x + i][square_start_cell_y + j]
            for j in range(3)
            if board[square_start_cell_x + i][square_start_cell_y + j]
            in possible
        )
    return [i for i in possible if i not in duplicates]


if __name__ == '__main__':
    global board_resolution
    try:
        board_resolution = int(input('How many squares per side in your sudoku? -> '))
    except ValueError:
        raise ValueError('Please enter an integer!')

    sudoku_rows = create_board(board_resolution)
    print_board(sudoku_rows)
    print('Solving...')
    solve_sudoku(sudoku_rows)
