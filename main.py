#!usr/bin python3
from solver import *
from board import *

def main():
    solved = solve_board(board)
    print_boards(board, solved)
    
main()
