import sys
from ast import literal_eval


all_packets = []
packets_pair = []
with open(sys.argv[1], 'r') as f:
    for line in f.read().splitlines():
        if len(line) > 0:
            packets_pair.append(literal_eval(line))
        else:
            all_packets.append(packets_pair)
            packets_pair = []
    all_packets.append(packets_pair)


def check_list(left_packet: list, right_packet: list) -> bool:
    for i in range(max(len(left_packet), len(right_packet))):
        left = left_packet[i] if i < len(left_packet) else 'end'
        right = right_packet[i] if i < len(right_packet) else 'end'
        # if both are int, compare them
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return True
            elif left > right:
                return False
        # if left runs out, it's correct
        elif isinstance(left, str) and not isinstance(right, str):
            return True
        # if right runs out, it's incorrect
        elif not isinstance(left, str) and isinstance(right, str):
            return False
        # if both are list, recall function
        elif isinstance(left, list) and isinstance(right, list):
            check = check_list(left, right)
            if check:
                return True
            elif check is None:
                continue
            else:
                return False
        # if one is list and one is int, convert & compare them
        elif isinstance(left, list) or isinstance(right, list):
            check = check_list(left if isinstance(left, list) else [left], right if isinstance(right, list) else [right])
            if check:
                return True
            elif check is None:
                continue
            else:
                return False


correct_packet = 0
for idx, packet_pair in enumerate(all_packets):
    left_packet, right_packet = packet_pair
    if check_list(left_packet, right_packet):
        correct_packet += idx + 1

print(correct_packet)
