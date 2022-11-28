#!/usr/bin/env python3

import math
import re

from ast import literal_eval


def find_values(sn, mode=''):

    if mode == 'explode':
        matches = list(re.finditer(r'\[\d+,\d+\]', sn))
    elif mode == 'split':
        matches = list(re.finditer(r'\d\d', sn))
    else:
        matches = list(re.finditer(r'\[\d+,\d+\]', sn))

    o_brackets = re.compile(r'\[')
    c_brackets = re.compile(r'\]')
    values_to_check = []

    for match in matches:

        value = literal_eval(match.group())

        if isinstance(value, int):
            values_to_check.append(match)
            continue

        if not mode:
            values_to_check.append(match)
            continue

        sn_before = sn[:match.start()]

        open_brackets   = len(re.findall(o_brackets, sn_before))
        closed_brackets = len(re.findall(c_brackets, sn_before))
        if open_brackets - closed_brackets < 4:
            continue
        else:
            values_to_check.append(match)

    return values_to_check


numbers = [literal_eval(l.rstrip()) for l in open('input.txt', 'r').readlines() if not l.startswith('#')]
sn = []

for number in numbers:
    if not sn:
        sn = number
    else:
        sn = [sn, number]

    sn_str = str(sn).replace(' ', '')
    print('\n###')
    print('# Full string:', sn_str)
    print('###')

    # matches = list(re.findall(explode_or_split, sn_str))
    matches = find_values(sn_str, mode='explode')

    while matches:

        match = matches.pop(0)

        value = literal_eval(match.group())
        sn_before = sn_str[:match.start()]
        sn_after  = sn_str[match.end():]

        if isinstance(value, list):

            r_sn_before  = sn_before[::-1]
            prev_num     = re.search(r'\d+', r_sn_before)
            if prev_num:
                prev_num_start = len(sn_before) - prev_num.end()
                prev_num_end   = len(sn_before) - prev_num.start()
                prev_num       = int(prev_num.group()[::-1])
                new_prev_num   = str(prev_num + value[0])
                sn_before = sn_before[:prev_num_start] + new_prev_num + sn_before[prev_num_end:]

            next_num = re.search(r'\d+', sn_after)
            if next_num:
                next_num_start = next_num.start()
                next_num_end   = next_num.end()
                next_num       = int(next_num.group())
                new_next_num   = str(next_num + value[1])
                sn_after = sn_after[:next_num_start] + new_next_num + sn_after[next_num_end:]

            sn_str = sn_before + '0' + sn_after
            print('Explode:', sn_str)

        elif isinstance(value, int):
            first_value = math.floor(value / 2)
            second_value = math.ceil(value / 2)
            sn_str = literal_eval(sn_before + f'[{first_value},{second_value}]' + sn_after)
            sn_str = str(sn_str).replace(' ', '')
            print('Split:', sn_str)

        else:
            raise ValueError(f'Value "{value}" has invalid value type {type(value)}')

        matches = find_values(sn_str, mode='explode')
        if not matches:
            matches = find_values(sn_str, mode='split')

    print()
    sn = literal_eval(sn_str)


sn = str(sn).replace(' ', '')
pairs = find_values(sn_str)
magnitude = 0
while pairs:

    pair = pairs.pop(0)
    literal_pair = literal_eval(pair.group())

    first_value, second_value = literal_pair[0], literal_pair[1]
    magnitude = (3 * literal_pair[0]) + (2 * literal_pair[1])

    sn = sn[:pair.start()] + str(magnitude) + sn[pair.end():]

    print('SN:', sn)
    pairs = find_values(sn)
# while pairs:
#     correction = 0
#     for pair in pairs:
#         literal_pair = literal_eval(pair.group())
#         first_value, second_value = literal_pair[0], literal_pair[1]

#         magnitude = (3 * literal_pair[0]) + (2 * literal_pair[1])

#         start = pair.start() - correction
#         end = pair.end() - correction

#         sn = sn[:start] + str(magnitude) + sn[end:]

#         correction = correction + (len(pair.group()) - len(str(magnitude)))

#         print('SN:', sn)
#     pairs = find_values(sn)


print('\nFinal result:', sn)
