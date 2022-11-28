#!/usr/bin/env python3

import re


target_area = next(open('test.txt', 'r'))
xmin, xmax, ymin, ymax = map(int, re.findall(r'-?\d+', target_area))

target_area = tuple((x, y) for x in range(xmin, xmax+1) for y in range(ymax, ymin-1, -1))

cur_y = ymin
highest_y = 0
no_hit_countdown = xmax * abs(ymin)

while no_hit_countdown > 0:
    velocities = tuple((x, cur_y) for x in range(xmax, 0, -1))

    for x_velocity, y_velocity in velocities:
        x = 0
        y = 0
        positions = []

        while x <= xmax and y >= ymin:
            x += x_velocity
            y += y_velocity
            positions.append((x, y))
            x_velocity -= 1 if x_velocity >= 0 else 0
            x_velocity += 1 if x_velocity < 0 else 0
            y_velocity -= 1

        if any(pos in target_area for pos in positions):
            no_hit_countdown = xmax * abs(ymin)
            cur_highest_y = max(positions, key=lambda t: t[1])[1]
            if cur_highest_y > highest_y:
                highest_y = cur_highest_y
        else:
            no_hit_countdown -= 1

    cur_y += 1

print(highest_y)