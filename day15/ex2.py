#!/usr/bin/env python3

from pprint import pprint


def traverse(closedby, cur):
    total_path = [cur]
    while cur in closedby:
        cur = closedby[cur]
        total_path.insert(0, cur)
    return total_path


def heuristic(a, b):
    h = 4
    return (2 * b[0] - a[0] - a[1]) * h


def dijkstra(matrix, edges, start=(0, 0)):
    
    x_len, y_len = len(matrix[0]), len(matrix)
    end = (x_len-1, y_len-1)
    
    costs = {(x, y): float('inf') for y in range(y_len) for x in range(x_len)}
    costs[start] = 0
    
    fcosts = {(x, y): float('inf') for y in range(y_len) for x in range(x_len)}
    fcosts[start] = heuristic(start, end)

    opened = {start}
    closed = {}

    while opened:
        
        opened_fcosts = {o: fcosts[o] for o in opened}
        current_point = min(opened_fcosts, key=opened_fcosts.get)
        if current_point == end:
            return traverse(closed, current_point)

        opened.remove(current_point)

        neighbors = {nb: c for nb, c in edges[current_point].items() if nb not in closed}
        for nb, c in neighbors.items():
            tentative_cost = opened_fcosts[current_point] + c
            if tentative_cost < costs[nb]:
                closed[nb] = current_point
                costs[nb] = tentative_cost
                fcosts[nb] = tentative_cost# + heuristic(nb, end)
                if nb not in opened:
                    opened.add(nb)
    return []


matrix = []
m_len = len(matrix)
edges = {}

with open('input.txt', 'r') as f:

    matrix = [[int(x) for x in row.strip()] for row in f.readlines()]

matrix = [[n+i*1 for i in range(5) for n in row] for row in matrix]
matrix = [[n-9 if n > 9 else n for n in row] for row in matrix]
matrix = [[n+i*1 for n in row] for i in range(5) for row in matrix]
matrix = [[n-9 if n > 9 else n for n in row] for row in matrix]

for y, row in enumerate(matrix):
    for x, cost in enumerate(row):
            
        x_edges = [(nx, y) for nx in (x-1, x+1) if 0 <= nx < len(row)]
        y_edges = [(x, ny) for ny in (y-1, y+1) if 0 <= ny < len(matrix)]
        
        edges[(x, y)] = {(nx, ny): matrix[ny][nx] for nx, ny in x_edges+y_edges}

best_path = dijkstra(matrix, edges)
print(best_path)
score = sum(matrix[y][x] for x, y in best_path if (x, y) != (0, 0))
print(score)

# Guessed: 2821