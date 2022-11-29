#!/usr/bin/env python3

from itertools import combinations, permutations

def all_combinations(coords):
    all_combinations = [coords]
    for i in range(1, 3):
        tmp_coords = list(coords)
        for j, c in enumerate(coords[:i]):
            tmp_coords[j] = abs(c) if c <= 0 else -c
    all_combinations = list(permutations(coords))
    inverse_coords = tuple(abs(c) if c <= 0 else -c for c in coords)
    all_combinations.extend(list(permutations(inverse_coords)))
    return all_combinations





scanners = {}
with open('test.txt', 'r') as f:
    scanner_count = 0
    for line in f.readlines():
        line = line.rstrip()
        if not line:
            continue
        if line.startswith('---'):
            scanner_count += 1
            scanners[f's{scanner_count}'] = []
            continue
        coords = tuple(map(int, line.split(',')))
        scanners.get(f's{scanner_count}').append(coords)

print(scanners)