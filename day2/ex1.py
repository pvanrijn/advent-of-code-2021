#!/usr/bin/env python3

readings = []

with open('input.txt', 'r') as f:
    commands = [d.strip() for d in f.readlines()]

horizontal = 0
depth = 0

for command in commands:

    ctype, cvalue = command.split()
    cvalue = int(cvalue)

    if ctype == 'up':
        depth -= cvalue
    elif ctype == 'down':
        depth += cvalue
    elif ctype == 'forward':
        horizontal += cvalue
    
print(horizontal * depth)