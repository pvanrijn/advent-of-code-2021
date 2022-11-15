#!/usr/bin/env python3

import time

def simulate(fishies, cycles_left):

    if cycles_left == 0:
        return fishies

    return simulate(
        [
            fishies[1],
            fishies[2],
            fishies[3],
            fishies[4],
            fishies[5],
            fishies[6],
            fishies[7] + fishies[0],
            fishies[8],
            fishies[0],
        ],
        cycles_left-1
    )

fishies = [0 for i in range(9)]

with open('input.txt', 'r') as f:
    for fish in map(int, next(f).split(',')):
        fishies[fish] += 1

start = time.perf_counter()

fishies = simulate(fishies, 256)

end = time.perf_counter()

print(f'Total number of lantern fishies: {sum(fishies)}')
print(f'Time elapsed: {end-start}')