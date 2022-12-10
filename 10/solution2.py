import sys
from collections import deque


command = deque()
x = 1
cycle = 0
buffer = False
screen = []
with open(sys.argv[1], 'r') as f:
    for line in f.read().splitlines():
        command.append(line.split())

while len(command) > 0:
    cycle += 1
    if (cycle - 1) % 40 in range(x - 1, x + 2):
        screen.append('#')
    else:
        screen.append('.')
    cur_command = command.popleft()
    if cur_command[0] == 'noop':
        pass
    elif cur_command[0] == 'addx':
        if buffer:
            x += int(cur_command[1])
            buffer = False
        else:
            command.appendleft(cur_command)
            buffer = True

for i in range(0, len(screen), 40):
    print(''.join(screen[i:i + 40]))
