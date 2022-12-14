import sys
from typing import List, Set, Tuple


input_line = []
with open(sys.argv[1], 'r') as f:
    for line in f.read().splitlines():
        input_line.append(line)


def parse(lines: List[str]) -> Set[Tuple[int, int]]:
    rock_list = set()
    for line in lines:
        pos_list = line.split(' -> ')
        f_pos = pos_list.pop(0)
        f_pos = tuple([int(p) for p in f_pos.split(',')])
        rock_list.add(f_pos)
        for pos in pos_list:
            pos = tuple([int(p) for p in pos.split(',')])
            while any([f_pos[i] != pos[i] for i in range(len(f_pos))]):
                dist = 10 ** 10
                n_pos = None
                for dir in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    new_pos = tuple([f_pos[i] + dir[i] for i in range(len(f_pos))])
                    new_dist = abs(new_pos[0] - pos[0]) + abs(new_pos[1] - pos[1])
                    if new_dist < dist:
                        n_pos = new_pos
                        dist = new_dist
                f_pos = n_pos
                rock_list.add(f_pos)
            rock_list.add(f_pos)
    return rock_list


def rest_pos(pos: Tuple[int, int], rock: Set[Tuple[int, int]], max_y: int) -> bool:
    while pos not in rock and pos[1] <= max_y:
        pos = (pos[0], pos[1] + 1)
    if pos[1] > max_y:
        return False
    if (pos[0] - 1, pos[1]) not in rock:
        return rest_pos((pos[0] - 1, pos[1]), rock, max_y)
    if (pos[0] + 1, pos[1]) not in rock:
        return rest_pos((pos[0] + 1, pos[1]), rock, max_y)
    rock.add((pos[0], pos[1] - 1))
    return True


def solve(input_line: List[str]) -> int:
    rock = parse(input_line)
    max_y = 0
    for _, pos_y in rock:
        if pos_y > max_y:
            max_y = pos_y
    start_pos = (500, 0)
    sand = 0
    while rest_pos(start_pos, rock, max_y):
        sand += 1
    return sand


print(solve(input_line))
