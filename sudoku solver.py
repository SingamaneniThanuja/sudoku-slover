print("SUDOKO SLOVER")
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None  # if no empty location is found


def is_valid(board, num, row, col):
    # Check if the number is already in the row
    if num in board[row]:
        return False

    # Check if the number is already in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is already in the 3x3 box
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(box_row_start, box_row_start + 3):
        for j in range(box_col_start, box_col_start + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    row, col = find_empty_location(board)

    if row is None:  # if no empty location is found, the puzzle is solved
        return True

    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            # If placing num at board[row][col] doesn't lead to a solution, backtrack
            board[row][col] = 0

    return False  # Trigger backtracking


# Example Sudoku board (0 represents empty cells)
board = [
    [0, 9, 0, 0, 0, 0, 0, 0, 5],
    [0, 8, 0, 0, 4, 7, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 8, 2, 0, 5, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 7, 4, 0, 3, 1, 0, 0],
    [0, 6, 0, 0, 9, 4, 0, 0, 0],
    [0, 0, 0, 7, 6, 8, 0, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 0]
]

print("Sudoku board before solving:")
print_board(board)

if solve_sudoku(board):
    print("\nSudoku board after solving:")
    print_board(board)
else:
    print("\nNo solution exists for the given Sudoku board.")
    #time complexity : O(9^(n^2))
    #space complexity : O(n^2)