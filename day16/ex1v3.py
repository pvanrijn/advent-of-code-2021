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

def is_literal_value(i):
    return True if i == 4 else False

def is_operator(i):
    return True if i == 11 or i == 15 else False

def parse_literal_value_bits(bits):

    value_bits = ''
    bits_processed = 0
    last_value_processed = False

    while not last_value_processed:

        bits_left = len(bits[bits_processed:])

        if bits_left < 5:
            bits_processed += bits_left
            break

        next_bits = bits[bits_processed:bits_processed+5]
        first_bit = next_bits[0]
        value_bit = next_bits[1:]

        value_bits = value_bits + value_bit
        bits_processed += 5

        if first_bit == '0':
            last_value_processed = True

    print(f'\t* Value bits: {value_bits}')
    return bit_to_int(value_bits), bits_processed


def parse_packet(bits, version_total=0, value_total=0):

    if len(bits) < 11:
        return bits, version_total, value_total

    print(f'\n# Original bits: {bits}')

    packet_version, packet_type, bits = bit_to_int(bits[:3]), bit_to_int(bits[3:6]), bits[6:]
    version_total += packet_version

    print(f'# New bits:            {bits}')
    print(f'# Packet version: {packet_version}')
    print(f'# Packet type:    {packet_type}')
    print(f'# Version total:  {version_total}')

    if is_literal_value(packet_type):
        literal_value, bits_processed = parse_literal_value_bits(bits)
        value_total += literal_value
        bits = bits[bits_processed:]

    else:
        set_bit, bits = bits[0], bits[1:]
        if set_bit == '0':  # parse packets in x bits
            num_packet_bits, bits = bits[:15], bits[15:]
            print(f'\t* Num packet bits raw: {num_packet_bits}')
            num_packet_bits = bit_to_int(num_packet_bits)
            print(f'\t* Num packet bits:     {num_packet_bits}')
            packet_bits, bits = bits[:num_packet_bits], bits[num_packet_bits:]
            while len(packet_bits) >= 11:
                packet_bits, version_total, value_total = parse_packet(packet_bits, version_total=version_total,
                                                                       value_total=value_total)
        else:  # parse x packets
            num_packets, bits = bits[:11], bits[11:]
            num_packets = bit_to_int(num_packets)
            print(f'\t* Num packets: {num_packets}')
            while num_packets > 0:
                bits, version_total, value_total = parse_packet(bits, version_total=version_total,
                                                                value_total=value_total)
                num_packets -= 1

    return bits, version_total, value_total


with open('input.txt', 'r') as f:
    lines = [l.rstrip() for l in f.readlines()]

for hex_line in lines:
    bit_line = hex_to_bit(hex_line)
    bits, version_total, value_total = parse_packet(bit_line)

    print(f'\nFinal bits: {bits}')
    print(f'Final version total: {version_total}')
    print(f'Final value total: {value_total}\n')