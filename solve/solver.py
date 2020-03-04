#!usr/bin python3
import math
from numpy import reshape, array


def solve_board(board=None):
    """Recursively solves a sodoku board

    Parameters
    --------------------------------------------------------------------------------
    board: list
        A two-dimensional list representing a sodoku board where each inner list is
        a row of cells.
    --------------------------------------------------------------------------------
    Returns
    --------------------------------------------------------------------------------
    list
        A solved board
    --------------------------------------------------------------------------------
    """

    for ind, v in enumerate(board):
        if v != None:
            continue
        neighbors = get_neighbors(ind)
        possible_nums = list(
            {1, 2, 3, 4, 5, 6, 7, 8, 9} - set([board[e] for e in (neighbors)])
        )

        for n in possible_nums:
            try_board = board.copy()
            del try_board[ind]
            try_board.insert(ind, n)
            result = solve_board(try_board)
            if result != None:
                return result
        return None
    return board


def get_neighbors(i):
    """Gets a cell's neighbors

    Parameters
    ----------------------------------------------------------------------------
    i: int
        A cell's position in a zero-indexed, one dimensional list representing a
        sodoku board read left-to-right, top-to-bottom.
    ----------------------------------------------------------------------------
    Returns
    ----------------------------------------------------------------------------
    list
        The indices of a cell's neighbors  
    ----------------------------------------------------------------------------
    """

    row = i // 9
    col = i % 9
    square_i = ((row % 3) * 3) + (i % 3)
    square_t_targets = {0: 10, 1: 9, 2: 8, 3: 1, 4: 0, 5: -1, 6: -8, 7: -9, 8: -10}
    target_i = square_t_targets[square_i] + i
    square_neighbors = [target_i + v for v in square_t_targets.values()]
    col_neighbors = list(map(lambda x: x + col, [0, 9, 18, 27, 36, 45, 54, 63, 72]))
    row_neighbors = list(range(i - col, i - col + 9))
    all_neighbors = row_neighbors + col_neighbors + square_neighbors
    return all_neighbors


def print_boards(input_board: list, solved_board: list):
    """Prints the input board and solved board

    Parameters
    ----------------------------------------------------------------------------
    input_board: list
    solved_board: list
    """
    input_board = [
        (lambda row: [e if type(e) == int else "." for e in row])(row)
        for row in input_board
    ]
    print("\n             I N P U T                      S O L V E D      \n")
    print("   +---------------------------+   +---------------------------+")
    for i in range(3):
        print("   | +-----------------------+ |   | +-----------------------+ | ")
        for j in range(3):
            print(
                "   | |",
                *input_board[i * 3 + j][:3],
                "|",
                *input_board[i * 3 + j][3:6],
                "|",
                *input_board[i * 3 + j][6:],
                "| |",
                " ",
                "| |",
                *solved_board[i * 3 + j][:3],
                "|",
                *solved_board[i * 3 + j][3:6],
                "|",
                *solved_board[i * 3 + j][6:],
                "| |"
            )
    print("   | +-----------------------+ |   | +-----------------------+ | ")
    print("   +---------------------------+   +---------------------------+")

