# Connect 4 Tutorial from FreeCodeCamp

import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board


def print_board(board):
    print(np.flip(board, 0))


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def winning_move(board, piece):
    # Check horizontals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece
            and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check verticals
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT):
            if board[r][c] == piece and board[r+1][c] == piece
            and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positive-slope diagonals
    for r in range(COLUMN_COUNT-3):
        for c in range(ROW_COUNT):
            if board[r][c] == piece and board[r+1][c+1] == piece
            and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negative-slope diagonals
    for r in range(ROW_COUNT-3):
        for c in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece
            and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    # Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 make your selection (0-6): "))
        # Check valid piece placement
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
        # Check for winning move
        if winning_move(board, 1):
            print("Player 1 Wins!")
            game_over = True     # Game is over

    # ask for player 2 input
    else:
        col = int(input("Player 2 make your selection (0-6): "))
        # Check valid piece placement
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
        # Check for winning move
        if winning_move(board, 2):
            print("Player 2 Wins!")
            game_over = True     # Game is over
            
        print_board(board)
    turn += 1
    turn = turn % 2
