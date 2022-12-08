import math
import sys


tree_map = {}
dimensions = []
with open(sys.argv[1], 'r') as f:
    for ridx, row in enumerate(f.read().splitlines()):
        for cidx, col in enumerate(row):
            tree_map[cidx + 1j * ridx] = int(col)
    dimensions = [cidx, ridx]

best = 0

for i in range(1, dimensions[1]):
    for j in range(1, dimensions[0]):
        target_height = tree_map[j + 1j * i]

        view = 0
        found = [0] * 4
        left = j
        while left > 0:
            left -= 1
            found[0] += 1
            if tree_map[left + 1j * i] >= target_height:
                break
        right = j
        while right < dimensions[0]:
            right += 1
            found[1] += 1
            if tree_map[right + 1j * i] >= target_height:
                break
        top = i
        while top > 0:
            top -= 1
            found[2] += 1
            if tree_map[j + 1j * top] >= target_height:
                break
        bottom = i
        while bottom < dimensions[1]:
            bottom += 1
            found[3] += 1
            if tree_map[j + 1j * bottom] >= target_height:
                break
        view = math.prod(found)
        best = view if view > best else best

print(best)
