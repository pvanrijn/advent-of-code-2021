#!/usr/bin/env python

from pprint import pprint


def traverse(curpoint, directions, curroute=[], routes=[], small_visited=[]):

    # dereference original list objects to keep the scope of these
    # variables local to each recursive iteration
    curroute = curroute.copy()
    small_visited = small_visited.copy()
    
    curroute.append(curpoint)

    if curpoint == 'end':
        routes.append(curroute)
        return routes
    
    nextpoints = [d for d in directions[curpoint] if d not in small_visited]
    if (curpoint == curpoint.lower()) and (curpoint not in small_visited):
        small_visited.append(curpoint)

    for nextpoint in nextpoints:
        routes = traverse(nextpoint, directions, routes=routes, curroute=curroute, small_visited=small_visited)
    
    return routes


lines = []
with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

directions = {}
for line in lines:
    point_a, point_b = line.split('-')
    if point_a != 'end':
        directions.setdefault(point_a, []).append(point_b)
    if point_b != 'end':
        directions.setdefault(point_b, []).append(point_a)

directions = {d: [v for v in values if v != 'start'] for d, values in directions.items()}
pprint(directions)

routes = traverse('start', directions)

pprint(routes)
print(f'Total number of routes: {len(routes)}')
