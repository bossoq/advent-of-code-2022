import sys


with open(sys.argv[1], 'r') as f:
    data = [0]
    for line in f:
        if line.strip() == '':
            data.append(0)
        else:
            data[-1] += int(line.strip())
    data.sort()

print(sum(data[-3:]))
