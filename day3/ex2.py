#!/usr/bin/env python3

def bit_criteria(zeroes, ones, criterium='oxy'):

    if criterium == 'oxy':
        if zeroes <= ones:
            return 1
        else:
            return 0
    elif criterium == 'co2':
        if zeroes <= ones:
            return 0
        else:
            return 1
    else:
        raise ValueError(f'Invalid criterium: {criterium}')


def count_bits_on_pos(lines, pos):
    
    zeroes = len(tuple(int(l[pos]) for l in lines if l[pos] == '0'))
    ones = len(tuple(int(l[pos]) for l in lines if l[pos] == '1'))
    
    return zeroes, ones


lines = []

with open('input.txt', 'r') as f:
    lines = [d.strip() for d in f.readlines()]

lines_oxy = lines.copy()
lines_co2 = lines.copy()

first_line = lines[0]

for pos in range(len(first_line)):

    if len(lines_oxy) != 1:
        zeroes, ones = count_bits_on_pos(lines_oxy, pos)
        print(zeroes, ones)
        lines_oxy = list(filter(lambda l: int(l[pos]) == bit_criteria(zeroes, ones, criterium='oxy'), lines_oxy))

    if len(lines_co2) != 1:
        zeroes, ones = count_bits_on_pos(lines_co2, pos)
        lines_co2 = list(filter(lambda l: int(l[pos]) == bit_criteria(zeroes, ones, criterium='co2'), lines_co2))

print(f'Oxy lines: {lines_oxy}')
print(f'CO2 lines: {lines_co2}')

print(int(lines_oxy[0], 2) * int(lines_co2[0], 2))


# Guessed: 3878091, 3385170