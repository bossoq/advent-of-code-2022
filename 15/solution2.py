import re
import sys
from typing import List, Set, Tuple


input_line = []
with open(sys.argv[1], 'r') as f:
    for line in f.read().splitlines():
        input_line.append(line)


def parse(lines: List[str]) -> Set[Tuple[Tuple[int, int], Tuple[int, int]]]:
    sensor_beacon_set = set()
    for line in lines:
        match = re.search(r'Sensor at x=(?P<s_x>\d+), y=(?P<s_y>\d+): closest beacon is at x=(?P<b_x>\d+), y=(?P<b_y>\d+)', line)
        if match:
            sensor_pos = (int(match.group('s_x')), int(match.group('s_y')))
            beacon_pos = (int(match.group('b_x')), int(match.group('b_y')))
            sensor_beacon_set.add((sensor_pos, beacon_pos))
    return sensor_beacon_set


def find_dist(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def find_freq(sensor_beacon_set: Set[Tuple[Tuple[int, int], Tuple[int, int]]], pos_set: Set[Tuple[int, int]], max_x_y: int) -> int:
    for pos in pos_set:
        if pos[0] >= 0 and pos[1] >= 0 and pos[0] <= max_x_y and pos[1] <= max_x_y:
            possible = True
            dup = False
            for sensor_pos, beacon_pos in sensor_beacon_set:
                if abs(sensor_pos[0] - pos[0]) + abs(sensor_pos[1] - pos[1]) == 0 or abs(beacon_pos[0] - pos[0]) + abs(beacon_pos[1] - pos[1]) == 0:
                    dup = True
                elif abs(sensor_pos[0] - pos[0]) + abs(sensor_pos[1] - pos[1]) <= abs(sensor_pos[0] - beacon_pos[0]) + abs(sensor_pos[1] - beacon_pos[1]):
                    possible = False
                    break
            if possible and not dup:
                print(pos)
                return pos[0] * 4000000 + pos[1]
    raise Exception('No solution found')


def find_bound(sensor_beacon_set: Set[Tuple[Tuple[int, int], Tuple[int, int]]], distances: List[int]) -> Tuple[List[int], List[int]]:
    positive_lines = []
    negative_lines = []
    for index, (sensor_pos, _) in enumerate(sensor_beacon_set):
        distance = distances[index]
        positive_lines.extend([sensor_pos[0] - sensor_pos[1] - distance, sensor_pos[0] - sensor_pos[1] + distance])
        negative_lines.extend([sensor_pos[0] + sensor_pos[1] - distance, sensor_pos[0] + sensor_pos[1] + distance])
    return positive_lines, negative_lines


def find_pos(sensor_beacon_set: Set[Tuple[Tuple[int, int], Tuple[int, int]]], positive_lines: List[int], negative_lines: List[int]) -> int:
    positive_pos = 0
    negative_pos = 0
    for i in range(2 * len(sensor_beacon_set)):
        for e in range(i + 1, (2 * len(sensor_beacon_set))):
            pos_x_1, pos_x_2 = positive_lines[i], positive_lines[e]
            if abs(pos_x_1 - pos_x_2) == 2:
                positive_pos = min(pos_x_1, pos_x_2) + 1

            pos_y_1, pos_y_2 = negative_lines[i], negative_lines[e]
            if abs(pos_y_1 - pos_y_2) == 2:
                negative_pos = min(pos_y_1, pos_y_2) + 1
    x, y = (positive_pos + negative_pos) // 2, (negative_pos - positive_pos) // 2
    return x * 4000000 + y


def solve(input_line: List[str]) -> int:
    sensor_beacon_set = parse(input_line)
    distances = [find_dist(sensor_pos, beacon_pos) for sensor_pos, beacon_pos in sensor_beacon_set]
    positive_lines, negative_lines = find_bound(sensor_beacon_set, distances)
    return find_pos(sensor_beacon_set, positive_lines, negative_lines)


print(solve(input_line))
