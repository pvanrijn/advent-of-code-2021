#!/usr/bin/env python3


def print_matrix(matrix):
    m = [[num if num <= 9 else 0 for num in row ] for row in matrix]
    for row in m:
        print(''.join(str(n) for n in row))


def new_flashes(matrix, flashed, flash_count):
    flashing = []
    for y, row in enumerate(matrix):
        for x, num in enumerate(matrix[y]):
            if (num > 9) and ((y, x) not in flashed):
                flashing.append((y, x))
                flash_count += 1
    return flashing, flash_count


def flash_neighbours(matrix, flashing):

    for y, x in sorted(flashing):

        new_y = [ny for ny in [y-1, y, y+1] if (ny >= 0) and (ny < len(matrix))]
        new_x = [nx for nx in [x-1, x, x+1] if (nx >= 0) and (nx < len(matrix[y]))]

        for ny in new_y:
            for nx in new_x:
                if (ny, nx) not in flashing:
                    matrix[ny][nx] += 1
    
    return matrix


def flash(matrix, flashed=[], flash_count=0):

    flashing, flash_count = new_flashes(matrix, flashed, flash_count)

    matrix = flash_neighbours(matrix, flashing)

    if flashing:
        flashed = flashed + flashing
        return flash(matrix, flashed=flashed, flash_count=flash_count)  

    return matrix, flash_count
            

def step(matrix, flash_count):
    
    matrix = [[num+1 for num in row] for row in matrix]

#    print('\nAFTER increment:')
#    print_matrix(matrix)

    matrix, flash_count = flash(matrix, flash_count=flash_count)

    matrix = [[num if num <= 9 else 0 for num in row ] for row in matrix]  

    return matrix, flash_count


matrix = []

with open('input.txt', 'r') as f:
    matrix = [l.strip() for l in f.readlines()]
    matrix = [[int(i) for i in l] for l in matrix]

steps = 100

#print(f'Start:')
#print_matrix(matrix)

total_flashes = 0
simultaneous = False
s = 0

#for s in range(steps):
#
#    print(f'\nStep {s+1} BEFORE increment:')
#    print_matrix(matrix)
while not simultaneous:
    s += 1
    matrix, total_flashes = step(matrix, flash_count=total_flashes)

    if all(n == 0 for row  in matrix for n in row):
        print(f'\nSIMULTANEOUS FLASH ON STEP {s}:')
        print_matrix(matrix)
        simultaneous = True

#    print(f'\nStep {s+1} FLASHED:')
#    print_matrix(matrix)

print(f'Total flashes: {total_flashes}')
