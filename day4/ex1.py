#!/usr/bin/env python3

import itertools
from pprint import pprint

def load_boards(board_lines):
    
    boards = []
    
    for pos in range(0, len(board_lines), 5):
        board = board_lines[pos:pos+5]
        board = [l.split() for l in board]
        board = [[int(num) for num in l] for l in board]
        boards.append(board)
    
    return boards


def winning_board(board_rows, balls_drawn):
    
    row_length = len(board_rows[0])
    board_columns = [list() for _ in range(row_length)]
    
    for x in range(row_length):
        for y, row in enumerate(board_rows):
            board_columns[y].append(row[x])

    for row, col in zip(board_rows, board_columns):
        if all(r in balls_drawn for r in row):
            return True
        if all(c in balls_drawn for c in board_columns):
            return True
    
    return False


def board_score(board, balls_drawn, winning_ball):
    flat_board = [num for row in board for num in row]
    flat_board = list(filter(lambda x: x not in balls_drawn, flat_board))
    return sum(flat_board) * winning_ball


balls = []
boards = []

with open('input.txt', 'r') as f:
    balls = [int(num) for num in next(f).split(',')]
    board_lines = [l.strip() for l in f.readlines()]
    board_lines = list(filter(lambda x: x != '', board_lines))
    boards = load_boards(board_lines)

balls_drawn = []
winner = None

for ball in balls:
    
    balls_drawn.append(ball)
    
    if winner:
        break

    for board in boards:

        if winning_board(board, balls_drawn):

            winner = board
            score = board_score(board, balls_drawn, ball)
            print(score)
            print(balls_drawn)
            pprint(board)
            break


# Guessed: 19695
# Winner: 27027