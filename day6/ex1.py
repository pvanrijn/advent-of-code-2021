#!/usr/bin/env python3

def simulate(fishies, cycles_left):
    if cycles_left == 0:
        return fishies
    cycles_left -= 1
    return simulate(
        {
            0: fishies[1],
            1: fishies[2],
            2: fishies[3],
            3: fishies[4],
            4: fishies[5],
            5: fishies[6],
            6: fishies[7] + fishies[0],
            7: fishies[8],
            8: fishies[0],
        },
        cycles_left
    )

fishies = {i: 0 for i in range(9)}

with open('input.txt', 'r') as f:
    for fish in map(int, next(f).split(',')):
        fishies[fish] += 1

fishies = simulate(fishies, 80)

print(sum([k for k in fishies.values()]))