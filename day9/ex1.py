#!/usr/bin/env python3

matrix = tuple()

with open('input.txt', 'r') as f:
    matrix = tuple(l.strip() for l in f.readlines())
    matrix = tuple(tuple(int(i) for i in l) for l in matrix)

#shadow_matrix = [list(row) for row in matrix]

low_points = []

for y, row in enumerate(matrix):
    
    for x, num in enumerate(row):

        check_y = [matrix[n][x] for n in [y-1, y+1] if n >= 0 and n < len(matrix)]
        check_x = [matrix[y][n] for n in [x-1, x+1] if (n >= 0) and (n < len(row))]
        
        if all(num < neighbor for neighbor in check_y + check_x):

            low_points.append(num)
#            shadow_matrix[y][x] = f'{num}X'


#for row in shadow_matrix:
#    print(row)

print(sum(n+1 for n in low_points))

# Guessed: 1789 (too high)