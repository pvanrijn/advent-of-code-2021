#!/usr/bin/env python3

from pprint import pprint

def solve_segments(patterns):

    # sort patterns on str length so we can pick out the easy numbers
    patterns = sorted(patterns, key=len)
    one, four, seven, eight = patterns[0], patterns[2], patterns[1], patterns[-1]

    numbers = {one: '1', four: '4', seven: '7', eight: '8'}
    print(numbers)

    for pat in patterns[3:-1]:
        
        pattern_length = len(pat)
        
        if pattern_length == 5:  # 2, 3, 5
            if all(c in pat for c in seven):
                numbers[pat] = '3'
            elif sum(1 for c in four if c in pat) == 3:
                numbers[pat] = '5'
            else:
                numbers[pat] = '2'
        
        elif pattern_length == 6:  # 6, 9, 0
            if all(c in pat for c in four) and all(c in pat for c in seven):
                numbers[pat] = '9'
            elif not all(c in pat for c in one):
                numbers[pat] = '6'
            else:
                numbers[pat] = '0'
    
    return numbers
            

lines = []

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

total = 0

for line in lines:

    all_patterns = line.split(' | ')[0].split()
    digit_patterns = line.split(' | ')[1].split()    
    
    all_patterns = tuple(''.join(sorted(p)) for p in all_patterns)
    digit_patterns = tuple(''.join(sorted(p)) for p in digit_patterns)
    
    enigma = solve_segments(all_patterns)
#    pprint(enigma)

    digit_string = ''.join([enigma[digit_pattern] for digit_pattern in digit_patterns])

    total += int(digit_string)

print(total)

# Guessed: 1038685 (too high), 1024815 (too low), 1031553