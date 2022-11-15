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
    
    for row in board_rows:
        for x, num in enumerate(row):
            board_columns[x].append(num)

    for row, col in zip(board_rows, board_columns):
        if all(r in balls_drawn for r in row):
            return True
        if all(c in balls_drawn for c in col):
            return True
    else:
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
winners = {}
last_winner = None

for ball in balls:
    
    if len(winners) == len(boards):
        break

    balls_drawn.append(ball)

    for i, board in enumerate(boards):

        if i in winners.keys():
            continue        

        if winning_board(board, balls_drawn):
            winners[i] = balls_drawn
            last_winner = i

last_winning_balls = winners[last_winner]
board = boards[last_winner]
winning_ball = last_winning_balls[-1]
score = board_score(board, last_winning_balls, winning_ball)

print(score)
print(last_winning_balls)
pprint(board)

marked_board = [['X' if num in last_winning_balls else num for num in row] for row in board]
pprint(marked_board)

# Guessed: 918, 26622 (too low)