import sys


seq = []
with open(sys.argv[1], 'r') as f:
    for line in f.read().splitlines():
        for idx, char in enumerate(line):
            seq.append(char)
            if len(seq) < 14:
                continue
            if len(set(seq)) == 14:
                print(idx + 1)
                break
            seq.pop(0)
