#!/usr/bin/env python3

readings = []

with open('input.txt', 'r') as f:
    readings = [int(d.strip()) for d in f.readlines()]

prev_reading = None
total_increases = 0

for reading in readings:

    if not prev_reading:
        prev_reading = reading
        continue

    if reading > prev_reading:
        total_increases += 1
    
    prev_reading = reading

print(total_increases)