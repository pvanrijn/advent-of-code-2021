#!/usr/bin/env python3

lines = []

with open('input.txt', 'r') as f:
    lines = [d.strip() for d in f.readlines()]

first_line = lines[0]

positions_counts = {pos: {'0': 0, '1': 0} for pos in range(len(first_line))}

for line in lines:
    for pos, bit in enumerate(line):
        positions_counts[pos][bit] += 1

gamma_rate = '0b'
epsilon_rate = '0b'

for pos, bitcount_dict in positions_counts.items():
    
    most = ''
    least = ''
    
    if bitcount_dict['0'] > bitcount_dict['1']:
        most = '0'
        least = '1'
    else:
        most = '1'
        least = '0'
    
    gamma_rate = gamma_rate + most
    epsilon_rate = epsilon_rate + least

print(gamma_rate, int(gamma_rate, 2))
print(epsilon_rate, int(epsilon_rate, 2))

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

print(gamma_rate * epsilon_rate)