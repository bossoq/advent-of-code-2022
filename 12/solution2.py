import sys
from collections import deque
from typing import List


tree_map = {}
start_pos = []
possible_d: List[complex] = [-1j, 1, 1j, -1]
with open(sys.argv[1], 'r') as f:
    for ridx, row in enumerate(f.read().splitlines()):
        for cidx, col in enumerate(row):
            if col == 'S':
                start_pos.append(cidx + 1j * ridx)
                tree_map[cidx + 1j * ridx] = 'S'
            elif col == 'E':
                target_pos = cidx + 1j * ridx
                tree_map[cidx + 1j * ridx] = 'E'
            elif col == 'a':
                start_pos.append(cidx + 1j * ridx)
                tree_map[cidx + 1j * ridx] = ord(col) - 97
            else:
                tree_map[cidx + 1j * ridx] = ord(col) - 97


def get_solution(visited: set, tovisit: deque) -> int:
    while len(tovisit) > 0:
        pos, steps, depth = tovisit.popleft()
        if pos in visited:
            continue
        visited.add(pos)
        for d in possible_d:
            new_pos = pos + d
            if new_pos in tree_map.keys():
                new_depth = tree_map[new_pos]
                if new_depth == 'E':
                    new_depth = 25
                elif new_depth == 'S':
                    new_depth = 0
                if new_depth <= depth + 1:
                    if tree_map[new_pos] == 'E':
                        return steps + 1
                    tovisit.append((new_pos, steps + 1, new_depth))


best = 10**10
for pos in start_pos:
    tovisit = deque()
    visited = set()
    tovisit.append((pos, 0, 0))
    steps = get_solution(visited, tovisit)
    if not steps:
        continue
    best = min(best, steps)

print(best)
