#!/usr/bin/env python3

def traverse(x, y, matrix, route=[], best_score=999999999):

    if not matrix or not len(matrix):
        return

    route = route.copy()
    route.append((x, y))
    
    len_x, len_y = (len(matrix[0]), len(matrix))

    if (x, y) == (len_x-1, len_y-1):

        route_score = sum(matrix[n][m] for m, n in route if (m, n) != (0, 0))
        if route_score < best_score:
            best_score = route_score
        return best_score
#            return route_score
#        else:
#            return best_score

#    new_score = int(best_score)

    if 0 <= x < len_x:
        best_score = traverse(x+1, y, matrix, best_score=best_score, route=route)
#        new_score = traverse(x+1, y, matrix, new_score, route=route)
    
    if 0 <= y < len_y:
        best_score = traverse(x, y+1, matrix, best_score=best_score, route=route)
#        new_score = traverse(x, y+1, matrix, new_score, route=route)

#    route.pop(0)

#    if (x, y) == (0, 0):
#        return best_score
    return best_score


def least_risky_route(routes, matrix, return_score=False):
    least_risk_score = 999999999999999
    least_risk_route = []
    for route in routes:
        route_score = sum(matrix[y][x] for x, y in route if (x, y) != (0, 0))
        if route_score < least_risk_score:
            least_risk_score = route_score
            least_risk_route = route
    if return_score:
        return least_risk_score
    else:
        return least_risk_route

matrix = []

with open('input.txt', 'r') as f:
    matrix = [[int(x) for x in row.strip()] for row in f.readlines()]

#y_traverse = len(matrix)
#x_traverse = len(matrix[0])
#routes = []

#routes = traverse(0, 0, matrix)
min_score = traverse(0, 0, matrix)

#print(routes[0])

#min_score = least_risky_route(routes, matrix, return_score=True)
#min_route = least_risky_route(routes, matrix)

print(f'Best score: {min_score}')
#print(f'Route: {min_route}')