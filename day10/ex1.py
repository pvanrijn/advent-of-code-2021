#!/usr/bin/env python3

from functools import reduce

def get_corrupted_char(line):
    
    valid_closers = {'[': ']', '{': '}', '(': ')', '<': '>'}
    queue_opened = []
    
    for char in line:
        
        if char in valid_closers.keys():
            queue_opened.append(char)
            continue

        last_opened = queue_opened[-1]
        if char == valid_closers[last_opened]:
            queue_opened.pop(-1)
            continue
        else:
            print(f'{line} - Expected {valid_closers[last_opened]}, but found {char} instead')
            return char
#            return True
    return ''
#    return False


        

lines = []
#with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f]

char_scores = {
    ')': 3, ']': 57, '}': 1197, '>': 25137
}
total_score = {
    ')': 0, ']': 0, '}': 0, '>': 0
}

#lines = list(filter(is_corrupted, lines))
for l in lines:
    corrupted_char = get_corrupted_char(l)
    if corrupted_char:
        total_score[corrupted_char] += char_scores[corrupted_char]

print(sum(total_score.values()))
