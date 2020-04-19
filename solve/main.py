#!usr/bin python3
from solver import *
from board import *
import reshape, array from numpy

def print_boards(input_board: list, solved_board: list):
    """Prints the input board and solved board

    Parameters
    ----------------------------------------------------------------------------
    input_board: list
    solved_board: list
    """
    input_board = array(input_board).reshape(9,9)
    solved_board = array(solved_board).reshape(9,9)
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
    

def main():
    solved = solve_board(board)
    print_boards(board, solved)

if __name__ == "__main__":
    main()
