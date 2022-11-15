#!/usr/bin/env python3

from collections import Counter


def polymerize(seq, polymers, steps, count=1):
    newseq = ''

    for i in range(len(seq)-1):
        p = seq[i:i+2]
        insert = polymers[p]
        if i == 0:
            newseq = newseq + seq[i] + insert + seq[i+1]
        else:
            newseq = newseq + insert + seq[i+1]
    
    newseq = ''.join(newseq)
#    print(f'After step {count}: {newseq}')
    if count != steps:
        return polymerize(newseq, polymers, steps, count=count+1)
    return newseq


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

print(polymers)
print(seq)

#print(f'Start: {seq}')

seq = polymerize(seq, polymers, 10)

polcounts = {v: k for k, v in dict(Counter(seq)).items()}
min_count = min(polcounts)
max_count = max(polcounts)

print(f'{max_count} - {min_count} = {max_count-min_count}')

# Guessed: 3245 (too high)