#!usr/bin python3
from solver import *
from board import *

def main():
    solved = solve_board(board)
    print_boards(array(board).reshape(9, 9), array(solved).reshape(9, 9))

if __name__ == "__main__":
    main()
