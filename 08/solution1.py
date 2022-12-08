import sys


tree_map = {}
dimensions = []
with open(sys.argv[1], 'r') as f:
    for ridx, row in enumerate(f.read().splitlines()):
        for cidx, col in enumerate(row):
            tree_map[cidx + 1j * ridx] = int(col)
    dimensions = [cidx, ridx]

visible = (cidx + ridx) * 2

for i in range(1, dimensions[1]):
    for j in range(1, dimensions[0]):
        target_height = tree_map[j + 1j * i]

        found = [1] * 4
        left = j
        while left > 0:
            left -= 1
            if tree_map[left + 1j * i] >= target_height:
                found[0] = 0
                break
        right = j
        while right < dimensions[0]:
            right += 1
            if tree_map[right + 1j * i] >= target_height:
                found[1] = 0
                break
        top = i
        while top > 0:
            top -= 1
            if tree_map[j + 1j * top] >= target_height:
                found[2] = 0
                break
        bottom = i
        while bottom < dimensions[1]:
            bottom += 1
            if tree_map[j + 1j * bottom] >= target_height:
                found[3] = 0
                break
        visible += 1 if sum(found) > 0 else 0

print(visible)
