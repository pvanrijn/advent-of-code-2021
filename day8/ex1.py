#!/usr/bin/env python3

lines = []

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

counts = 0

for line in lines:
    
#    patterns = line.split(' | ')[0].split()
    digits   = line.split(' | ')[1].split()
    counts += len([d for d in digits if len(d) in [2, 3, 4, 7]])

print(counts)