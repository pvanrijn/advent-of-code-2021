#!/usr/bin/env python3

def crawl_basin(matrix, y, x, size=1, traversed=[]):

    cur_value = matrix[y][x]

    # get surrounding positions
    new_y = [(ny, x) for ny in [y-1, y+1] if (ny >= 0) and (ny < len(matrix))]
    new_x = [(y, nx) for nx in [x-1, x+1] if (nx >= 0) and (nx < len(matrix[y]))]

    next_points = new_y + new_x

    for ny, nx in next_points:
        
        next_value = matrix[ny][nx]
        if next_value == 9:
            continue
        
        if next_value > cur_value:
            if (ny, nx) in traversed:
                continue
            traversed.append((ny, nx))
            size, traversed = crawl_basin(matrix, ny, nx, size=size+1, traversed=traversed)

    return size, traversed


matrix = tuple()

with open('input.txt', 'r') as f:
#with open('test.txt', 'r') as f:
    matrix = tuple(l.strip() for l in f.readlines())
    matrix = tuple(tuple(int(i) for i in l) for l in matrix)

low_coords = []

for y, row in enumerate(matrix):

    for x, num in enumerate(row):

        check_y = [matrix[n][x] for n in [y-1, y+1] if n >= 0 and n < len(matrix)]
        check_x = [matrix[y][n] for n in [x-1, x+1] if (n >= 0) and (n < len(row))]
        
        if all(num < neighbor for neighbor in check_y + check_x):
            low_coords.append((y, x))

largest_basins = [0, 0, 0]

for y, x in low_coords:
    
    size, _ = crawl_basin(matrix, y, x)
    
    if size > min(largest_basins):
        largest_basins[0] = size
        largest_basins = sorted(largest_basins)

print(largest_basins)
print(largest_basins[0] * largest_basins[1] * largest_basins[2])

# Guessed: 169728 (too low), 15933894293783138763068005200264 (too high), 79356402 (too high), 523260, 1023660