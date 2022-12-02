import sys


win = ['A Y', 'B Z', 'C X']
draw = ['A X', 'B Y', 'C Z']
shape = ['X', 'Y', 'Z']
point = 0

with open(sys.argv[1], 'r') as f:
    for line in f:
        if line.strip() in win:
            point += 6
        elif line.strip() in draw:
            point += 3
        point += shape.index(line.strip()[-1]) + 1

print(point)
