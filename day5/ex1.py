#!/usr/bin/env python3

from pprint import pprint


def path(coord1, coord2):
    coords = [coord1, coord2]
    traversal = list(range(min(coords), max(coords)+1))
    return traversal


lines = []

with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

register = {}

for line in lines:
    
    xy1, xy2 = line.split(' -> ')
    x1, y1 = map(int, xy1.split(','))
    x2, y2 = map(int, xy2.split(','))

    if (x1 != x2) and (y1 != y2):
        continue
    
    x_traversal = path(x1, x2)
    y_traversal = path(y1, y2)

    for x in x_traversal:
        for y in y_traversal:
            coordinate = f'{x},{y}'
            register[coordinate] = register.get(coordinate, 0) + 1
    
register = {coord: count for coord, count in register.items() if count > 1}

print(len(register))
