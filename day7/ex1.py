#!/usr/bin/env python3

from statistics import median, mode

crabmarines = []

with open('input.txt', 'r') as f:
    crabmarines = tuple(sorted(map(int, next(f).split(','))))

crabmarines_median = int(median(crabmarines))

print(f'Median: {crabmarines_median}')

energy_consumption_median = sum([abs(crab - crabmarines_median) for crab in crabmarines])

print(f'Energy median: {energy_consumption_median}')
