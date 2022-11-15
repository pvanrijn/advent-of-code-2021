#!/usr/bin/env python3

from functools import reduce

def is_valid(line):
    
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
#            print(f'{line} - Expected {valid_closers[last_opened]}, but found {char} instead')
            return False
    return True

def get_missing_chars(line):
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
    
    missing_chars = ''.join([valid_closers[char] for char in queue_opened[::-1]])
    return missing_chars
        

lines = []
#with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f]

lines = list(filter(is_valid, lines))

char_scores = {
    ')': 1, ']': 2, '}': 3, '>': 4
}
total_scores = []
for l in lines:
    cur_score = 0
    missing_chars = get_missing_chars(l)
    for char in missing_chars:
        cur_score *= 5
        cur_score += char_scores[char]
    total_scores.append(cur_score)
    print(f'{l} - Completed by {missing_chars} - Total score {cur_score}')

total_scores = sorted(total_scores)
middle_pos = int(len(total_scores) / 2)

print(f'Middle score: {total_scores[middle_pos]}')

