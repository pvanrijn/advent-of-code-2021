#!/usr/bin/env python
'''
def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


def merge_matrices(m1, m2):
    matrix = []
    for y1, y2 in zip(m1, m2):
        row = []
        for x1, x2 in zip(y1, y2):
            if x1 == '#' or x2 == '#':
                row.append('#')
            else:
                row.append('.')
        matrix.append(row)
    return matrix


def fold(matrix, axis, foldline):
    #foldline += 1
    if axis == 'y':
    
        matrix_keep = [[matrix[y][x] for x in range(len(matrix[y]))] for y in range(foldline)]
        
        matrix_merge = [[matrix[y][x] for x in range(len(matrix[y]))] for y in range(foldline+1, len(matrix))]
        matrix_merge = matrix_merge[::-1]
    
    elif axis == 'x':
        matrix_keep = [[matrix[y][x] for x in range(foldline)] for y in range(len(matrix))]
        
        matrix_merge = [[matrix[y][x] for x in range(foldline+1, len(matrix[y]))] for y in range(len(matrix))]
        matrix_merge = [row[::-1] for row in matrix_merge]

#        return merge_matrices(matrix_merge, matrix_keep)
    
    return merge_matrices(matrix_keep, matrix_merge)
'''


def fold_up(point, foldline):
    x, y = point
    return (x, 2*foldline-y) if y > foldline else (x, y)


def fold_left(point, foldline):
    x, y = point
    return (2*foldline-x, y) if x > foldline else (x, y)


def fold(points, ax, foldline):
    if ax == 'x':
        points = set(fold_left(p, foldline) for p in points)
    else:
        points = set(fold_up(p, foldline) for p in points)
    return points

def print_matrix(points):
    max_x = max(p[0] for p in points) + 1
    max_y = max(p[1] for p in points) + 1
    for y in range(max_y):
        row = ''
        for x in range(max_x):
            if (x, y) in points:
                row = row + '#'
            else:
                row = row + '.'
        print(row)
    print()


lines = []
with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]

folds = []
points = []
for line in lines:
    if line.startswith('fold'):
        tmp = line.split('=')
        ax, num = tmp[0][-1], int(tmp[1])
        folds.append((ax, num))
    else:
        points.append(tuple(map(int, line.split(','))))

points = set(points)

print_matrix(points)
for ax, foldline in folds:

    #matrix = fold(matrix, ax, foldline)
    points = fold(points, ax, foldline)
    #print_matrix(points)
    #print(len(points))
    #break
print_matrix(points)


#print(f'\nFolded matrix:')
#print_matrix(matrix)
# Guessed: 825 (Too high)