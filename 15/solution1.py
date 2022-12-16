import re
import sys
from typing import List, Set, Tuple


input_line = []
with open(sys.argv[1], 'r') as f:
    for line in f.read().splitlines():
        input_line.append(line)


def parse(lines: List[str]) -> Tuple[Set[Tuple[Tuple[int, int], Tuple[int, int]]], int, int]:
    min_x = 10 ** 10
    max_x = 0
    sensor_beacon_set = set()
    for line in lines:
        match = re.search(r'Sensor at x=(?P<s_x>\d+), y=(?P<s_y>\d+): closest beacon is at x=(?P<b_x>\d+), y=(?P<b_y>\d+)', line)
        if match:
            sensor_pos = (int(match.group('s_x')), int(match.group('s_y')))
            min_x = min(min_x, sensor_pos[0])
            max_x = max(max_x, sensor_pos[0])
            beacon_pos = (int(match.group('b_x')), int(match.group('b_y')))
            min_x = min(min_x, beacon_pos[0])
            max_x = max(max_x, beacon_pos[0])
            sensor_beacon_set.add((sensor_pos, beacon_pos))
    return sensor_beacon_set, min_x, max_x


def count_coverage(sensor_beacon_set: Set[Tuple[Tuple[int, int], Tuple[int, int]]], min_x: int, max_x: int, target_y: int) -> int:
    count = 0
    for x in range(min_x - 1000000, max_x + 1000000):
        pos = (x, target_y)
        possible = True
        same = False
        for sensor_pos, beacon_pos in sensor_beacon_set:
            if abs(sensor_pos[0] - pos[0]) + abs(sensor_pos[1] - pos[1]) == 0 or abs(beacon_pos[0] - pos[0]) + abs(beacon_pos[1] - pos[1]) == 0:
                same = True
            elif abs(sensor_pos[0] - pos[0]) + abs(sensor_pos[1] - pos[1]) <= abs(sensor_pos[0] - beacon_pos[0]) + abs(sensor_pos[1] - beacon_pos[1]):
                possible = False
                break
        if not possible and not same:
            count += 1
    return count


def solve(input_line: List[str], target_y: int) -> int:
    sensor_beacon_set, min_x, max_x = parse(input_line)
    return count_coverage(sensor_beacon_set, min_x, max_x, target_y)


print(solve(input_line, 2000000))
