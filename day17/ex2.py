#!/usr/bin/env python3

import re


target_area = next(open('input.txt', 'r'))
xmin, xmax, ymin, ymax = map(int, re.findall(r'-?\d+', target_area))

target_area = tuple((x, y) for x in range(xmin, xmax+1) for y in range(ymax, ymin-1, -1))

cur_y = ymin
hits = set()
no_hit_countdown = xmax * abs(ymin)
# no_hit_countdown = xmax + abs(ymin)
# no_hit_countdown = 100

while no_hit_countdown > 0:
    # velocities = tuple((x, cur_y) for x in range(xmax, 0, -1))
    velocities = tuple((x, cur_y) for x in range(1, xmax+1, 1))
    hit = False
    for x_velocity, y_velocity in velocities:
        xv, yv = x_velocity, y_velocity
        x, y = 0, 0
        positions = []

        while x <= xmax and y >= ymin:
            x += xv
            y += yv
            positions.append((x, y))
            xv -= 1 if xv >= 0 else 0
            xv += 1 if xv < 0 else 0
            yv -= 1

        position_hit = any(pos in target_area for pos in positions)
        if position_hit:
            # no_hit_countdown = xmax * abs(ymin)
            hits.add((x_velocity, y_velocity))
            hit = True
    if hit:
        no_hit_countdown = xmax + abs(ymin)
    else:
        no_hit_countdown -= 1

    cur_y += 1


print(hits)
print(len(hits))