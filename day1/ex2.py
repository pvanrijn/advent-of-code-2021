#!/usr/bin/env python3

readings = []

with open('input.txt', 'r') as f:
    readings = [int(d.strip()) for d in f.readlines()]

prev_reading = None
total_increases = 0

for i1 in range(len(readings)):
    
    i2 = i1 + 1
    
    if i2 + 3 > len(readings):
        break

    measure1 = sum(readings[i1:i1+3])
    measure2 = sum(readings[i2:i2+3])

    if measure2 > measure1:
        total_increases += 1
    
print(total_increases)