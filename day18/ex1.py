#!/usr/bin/env python3

import math
import re

from ast import literal_eval


def explode(sn):
    pass

def split(sn):
    pass


def depth(sn):
    if isinstance(sn, list):
        return 1 + max(depth(n) for n in sn) if sn else 1
    else:
        return 0

numbers = [literal_eval(l.rstrip()) for l in open('test.txt', 'r').readlines()]
explode_or_split = re.compile(r'\[\d,\d\]|\d\d')
o_brackets = re.compile(r'\[')
c_brackets = re.compile(r'\]')
sn = []
for number in numbers:
    if not sn:
        sn = number
    else:
        sn = [sn, number]

    sn_str = str(sn).replace(' ', '')
    print('Full string:', sn_str)

    while re.search(explode_or_split, sn_str):

        match = re.search(explode_or_split, sn_str)
        value = literal_eval(match.group())
        sn_before = sn_str[:match.start()]
        sn_after  = sn_str[match.end():]

        if isinstance(value, list):
            # if not sn_before:
            #     continue

            open_brackets   = len(re.findall(o_brackets, sn_before))
            closed_brackets = len(re.findall(c_brackets, sn_before))

            if open_brackets - closed_brackets < 4:
                break
            else:
                print('Match:', value)
                r_sn_before = sn_before[::-1]
                prev_num = re.search(r'\d+', r_sn_before)
                sn_before = list(sn_before)
                if prev_num:
                    prev_num_location = len(sn_before) - prev_num.end()
                    prev_num = int(prev_num.group())
                    sn_before[prev_num_location] = str(prev_num + value[0])
                sn_before = ''.join(sn_before)

                next_num = re.search(r'\d+', sn_after)
                sn_after = list(sn_after)
                print('Next num:', next_num)
                if next_num:
                    next_num_location = next_num.start()
                    next_num = int(next_num.group())
                    sn_after[next_num_location] = str(next_num + value[1])
                    print(f'{next_num} + {value[1]} = {next_num + value[1]}')
                sn_after = ''.join(sn_after)

                print('Before:', sn_before)
                print('After:', sn_after)
                sn_str = sn_before + '0' + sn_after
                # sn_str = str(literal_eval(sn_str)).replace(' ', '')

        elif isinstance(value, int):
            print('Match:', value)
            first_value = math.floor(value / 2)
            second_value = math.ceil(value / 2)
            sn_str = literal_eval(sn_before + f'[{first_value},{second_value}]' + sn_after)
            sn_str = str(sn_str).replace(' ', '')
        else:
            raise ValueError(f'Value "{value}" has invalid value type {type(value)}')

        print(sn_str)
    # print(sn)
    sn = literal_eval(sn_str)


print('Result:', sn)
