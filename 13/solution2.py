import sys
from ast import literal_eval


all_packets = []
divider_packets = [[[2]], [[6]]]
with open(sys.argv[1], 'r') as f:
    for line in f.read().splitlines():
        if len(line) > 0:
            all_packets.append(literal_eval(line))
all_packets += divider_packets


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


for i in range(len(all_packets)):
    min_idx = i
    for j in range(i + 1, len(all_packets)):
        if check_list(all_packets[j], all_packets[min_idx]):
            min_idx = j
    all_packets[i], all_packets[min_idx] = all_packets[min_idx], all_packets[i]

print((all_packets.index(divider_packets[0]) + 1) * (all_packets.index(divider_packets[1]) + 1))
