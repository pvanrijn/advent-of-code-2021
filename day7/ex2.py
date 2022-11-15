#!/usr/bin/env python3

from statistics import median, mode

crabmarines = []

with open('input.txt', 'r') as f:
#with open('test.txt', 'r') as f:
    crabmarines = tuple(map(int, next(f).split(',')))


positions = range(max(crabmarines)+1)

least_fuel = None
best_pos = 0
for pos in positions:

    fuel_spent = sum([abs(pos - crab) + sum(range(abs(pos - crab))) for crab in crabmarines])
#    fuel_spent = sum([sum(range(abs(crab - pos)+1)) for crab in crabmarines])

    print(f'Pos: {pos}, Fuel: {fuel_spent}')

    if not least_fuel:
        least_fuel = fuel_spent
        continue

    if fuel_spent < least_fuel:
        least_fuel = fuel_spent
        best_pos = pos

print(f'Position {best_pos} required the least fuel: {least_fuel}')

# Guessed: 94017648, 94017638