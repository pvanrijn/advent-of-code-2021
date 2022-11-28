#!/usr/bin/env python

# First 3 bits : packet version
# Second 3 bits: packet type ID

# Packets with type ID 4 represent a literal value.
# Literal values:
#   - 5 bits: 4 bit number, prefixed by 1 or 0 (e.g. 10011 or 01101)
#     * prefix 0 indicates last literal value group
#
# Packets with type ID other than 4 are operators
# Operator packet:
#   - First bit after the packet header:
#     * 0 = next 15 bits dictates the total _length_ of next subpackets
#     * 1 = next 11 bits dictates the total _number_ of subpackets
#   -
# Loop through literal values in subpackets

def hex_to_bit(hex_string):
    cdict = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
    }
    return ''.join([cdict[h] for h in hex_string])

def bit_to_int(bit):
    return int(bit, 2)

def is_literal_val(i):
    return True if i == 4 else False

def is_operator(i):
    return True if i == 11 or i == 15 else False

def literal_val_string_to_int(bit_string):
    concat_bits = ''
    num_of_bits = 0
    nums = []

    for i in range(0, len(bit_string)-5, 5):
        full_bit  = bit_string[i:i+5]
        first_bit = full_bit[0]
        value_bit = full_bit[1:]

        concat_bits = concat_bits + value_bit
        num_of_bits += 1

        if first_bit == 0:
            nums.append(bit_to_int(concat_bits))
            concat_bits = ''
            break

    if concat_bits:
        nums.append(bit_to_int(concat_bits))
        num_of_bits += 1

    return num_of_bits, sum(nums)

def parse_packet(packet, is_new_packet):

    packet_int = bit_to_int(packet)
    packet_len = len(packet)

    if is_new_packet:
        return packet_int, packet_len

    next_packet_len = 0

    if packet_len == 3:
        next_packet_len = 5 if packet_int == 4 else 1

    elif packet_len == 1:
        next_packet_len = 11 if packet_int == 1 else 15

    elif packet_len == 11:
        next_packet_len = packet_int

    elif packet_len == 15:
        next_packet_len = packet_len

    elif packet_len == 5:

        if int(packet[0]) == 1:
            next_packet_len = 5
        else:
            next_packet_len = 0

    return packet_int, next_packet_len


def parse_bit_string(bit_string, operator=False):

    is_new_packet    = True
    versions         = 0
    total_value      = 0
    total_parsed_len = 0
    packet_len       = 3

    while True:
        packet, bit_string = bit_string[:packet_len], bit_string[packet_len:]
        packet_val, next_packet_len = parse_packet(packet, is_new_packet)

        if is_new_packet:
            versions += packet_val
            is_new_packet = False
            continue

        if is_operator(packet_len):
            length_bit, bit_string = bit_string[:1], bit_string[1:]
            op_packet_bits = 15 if length_bit == 0 else 11
            op_bit, bit_string = bit_string[:op_packet_bits], bit_string[op_packet_bits:]
            op_packet_len = bit_to_int(op_bit) * 5
            for i in range(0, op_packet_len, 5):

            is_new_packet = True
            # return parse_bit_string(bstring[packet_len:])

        if is_literal_val(packet_val):
            num_of_bits, value = literal_val_string_to_int(bit_string)
            total_value += value




hex_string = ''

with open('test.txt', 'r') as f:
    hex_string = next(f).strip()

bit_string = hex_to_bit(hex_string)
p_len = 3
is_new_packet = True
total_value = 0
total_versions = 0
version_lengths = [1, 3]

print(bit_string)

while False:

    packet, bit_string = bit_string[:p_len], bit_string[p_len:]

    p_val, next_plen = parse_packet(packet, new_packet=new_packet)

#    print(packet, p_len, p_val)

    if is_new_packet:
        is_new_packet = False
        continue



    if is_operator(p_len):

        for i in range(p_val):
            num_of_bits, value = literal_val_string_to_int(bit_string)
            skip_bits = num_of_bits * 5
#            total_value += value
#            print(value, total_value)

            if len(bit_string) - skip_bits < 5:
                break

            bit_string = bit_string[skip_bits:]

    elif is_literal_val(p_val):
        num_of_bits, value = literal_val_string_to_int(bit_string)
#        total_value += value

    if len(bit_string) < 5:
        break

    p_len = next_plen

print(total_value)