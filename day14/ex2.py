#!/usr/bin/env python3

from collections import Counter

lines = []
with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]

polymers = {}
seq = ''

for line in lines:
    if '->' in line:
        poly, insert = line.split(' -> ')
        polymers[poly] = insert
    else:
        seq = line
        #seq = tuple(line)

steps = 40

paired_seq = list(map(''.join, [a + b for a, b in zip(seq, seq[1:])]))
print(paired_seq)
counter_pairs = Counter(map(''.join, paired_seq))
counter_seq = Counter(seq)
for _ in range(steps):
    counter_total = Counter()
    for pair in polymers.keys():
        insert, old_count = polymers[pair], counter_pairs[pair]
        counter_total[pair[0] + insert] += old_count
        counter_total[insert + pair[-1]] += old_count
        counter_seq[insert] += old_count
    counter_pairs = counter_total

most_common = counter_seq.most_common()
max_count = most_common[0][1]
min_count = most_common[-1][1]

print(most_common)

print(f'{max_count} - {min_count} = {max_count-min_count}')

# Guessed: 3245 (too high), 3143 (too low)