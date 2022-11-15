#!/usr/bin/env python

# First 3 bits : packet version
# Second 3 bits: packet type ID

# Packets with type ID 4 represent a literal value.
# Literal values:
#   - 5 bit number: 4 bit number, prefixed by 1 or 0 (e.g. 10011 or 01101)
#   - Prefix 0 indicates last literal value group
# Packets with type ID other than 4 are operators
# Operator length packet ID is bit immediately after the packet header:
#   - 0 = 15 next bits dictate length of subpackets
#   - 1 = 11 next bits dictate length of subpackets
# Loop through literal values in subpackets

def hex_to_bit(hex_string):
    cdict = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
    }
    return ''.join([cdict[h] for h in hex_string])

def bit_to_int(b):
    return int(b, 2)

def literal_val_string_to_int(bit_string):
    lens = []
    sums = []
    nums = []
#    print(bit_string)
    for i in range(0, len(bit_string)-5, 5):
        bit = bit_string[i:i+5]
        bit_int = bit_to_int(bit[1:])
        nums.append(bit_int)
        if bit[0] == 0:
            lens.append(len(nums))
            sums.append(sum(nums))
            nums = []
            break
    if nums:
        lens.append(len(nums))
        sums.append(sum(nums))
    print(sums)
    return sum(lens), sum(sums)

def is_literal_val(i):
    return True if i == 4 else False

def is_operator(i):
    return True if i == 11 or i == 15 else False

def parse_packet(p, prev_p=''):
    p_int = bit_to_int(p)
    p_len = len(p)
    
    if not prev_p:
        return p_int, p_len

    next_p_len = 0
    if p_len == 3:
        next_p_len = 5 if p_int == 4 else 1
    elif p_len == 1:
        next_p_len = 11 if p_int == 1 else 15
    elif p_len == 11:
        next_p_len = p_int
    elif p_len == 15:
        next_p_len = p_len
    elif p_len == 5:
        if int(p[0]) == 1:
            next_p_len = 5
        else:
            next_p_len = 0

    return p_int, next_p_len

hex_string = ''
with open('test.txt', 'r') as f:
    hex_string = next(f).strip()

bit_string = hex_to_bit(hex_string)
print(bit_string)
p_len = 3
prev_packet = ''
packet = ''
total_value = 0

while True:
    packet, bit_string = bit_string[:p_len], bit_string[p_len:]
    p_val, next_plen = parse_packet(packet, prev_p=prev_packet)

#    print(packet, p_len, p_val)
  
    if not prev_packet:
        prev_packet = packet
        continue
    
    if is_operator(p_len):
#        print(p_val)
        for i in range(p_val):
            num_of_bits, value = literal_val_string_to_int(bit_string)
#            total_value += value
#            print(value, total_value)

            skip_bits = num_of_bits * 5
            bit_string = bit_string[skip_bits:]
            if len(bit_string) > 5:
                break
    
    elif is_literal_val(p_val):
        num_of_bits, value = literal_val_string_to_int(bit_string)
#        total_value += value
    
    if len(bit_string) < 5:
        break

    p_len = next_plen
 
print(total_value)