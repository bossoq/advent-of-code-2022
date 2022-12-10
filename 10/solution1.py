import sys
from collections import deque


command = deque()
x = 1
cycle = 0
max_cycle = 220
buffer = False
signal_strength = 0
with open(sys.argv[1], 'r') as f:
    for line in f.read().splitlines():
        command.append(line.split())

while len(command) > 0:
    cycle += 1
    if (cycle - 20) % 40 == 0:
        signal_strength += cycle * x
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
    if cycle == max_cycle:
        break

print(signal_strength)
