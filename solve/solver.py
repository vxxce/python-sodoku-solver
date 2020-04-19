#!usr/bin python3
import math
from numpy import reshape, array

def solve_board(board=None):
    """Recursively solves a sodoku board
    Parameters
    --------------------------------------------------------------------------------
    board: list
        A list representing the cells of a sodoku board read from left-to-right and
        top-to-bottom with empty cells are denoted with None values.
    --------------------------------------------------------------------------------
    Returns
    --------------------------------------------------------------------------------
    list
        A solved board, or None if no valid solution.
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
        The cell's index
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


