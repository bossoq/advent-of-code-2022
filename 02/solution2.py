import sys


win = ['A Y', 'B Z', 'C X']
draw = ['A X', 'B Y', 'C Z']
shape = ['X', 'Y', 'Z']
op_shape = ['A', 'B', 'C']
point = 0

with open(sys.argv[1], 'r') as f:
    for line in f:
        if line.strip()[-1] == 'X':
            line = line.replace('X', shape[op_shape.index(line.strip()[0]) - 1])
        elif line.strip()[-1] == 'Y':
            line = line.replace('Y', shape[op_shape.index(line.strip()[0])])
        elif line.strip()[-1] == 'Z':
            line = line.replace('Z', shape[(op_shape.index(line.strip()[0]) + 1) % 3])
        if line.strip() in win:
            point += 6
        elif line.strip() in draw:
            point += 3
        point += shape.index(line.strip()[-1]) + 1

print(point)
