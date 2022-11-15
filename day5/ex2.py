#!/usr/bin/env python3

from pprint import pprint


def path(coord1, coord2):
    if coord1 < coord2:
        return list(range(coord1, coord2+1))
    else:
        return list(range(coord2, coord1+1))[::-1]
#        return traverse[::-1]


lines = []

with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

register = {}

for line in lines:
    
    xy1, xy2 = line.split(' -> ')
    x1, y1 = map(int, xy1.split(','))
    x2, y2 = map(int, xy2.split(','))

#    x_traversal = path(x1, x2)
#    y_traversal = path(y1, y2)

    if (x1 != x2) and (y1 != y2):
#        if len(x_traversal) != len(y_traversal):
#            print(line)
#            continue
        x_diff = max(x1, x2) - min(x1, x2)
        y_diff = max(y1, y2) - min(y1, y2)

        if x_diff != y_diff:
            continue

    x_traversal = path(x1, x2)
    y_traversal = path(y1, y2)

##    print(line)
    if len(x_traversal) != len(y_traversal):
        for x in x_traversal:
            for y in y_traversal:
                coordinate = f'{x},{y}'
                register[coordinate] = register.get(coordinate, 0) + 1
    else:
        for x, y in zip(x_traversal, y_traversal):
            coordinate = f'{x},{y}'
            register[coordinate] = register.get(coordinate, 0) + 1

register = {coord: count for coord, count in register.items() if count > 1}

#pprint(register)
print(len(register))

# 950009, 949904, 872185, 6360