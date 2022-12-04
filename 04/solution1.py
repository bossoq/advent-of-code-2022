import sys


count = 0
with open(sys.argv[1], 'r') as f:
    for line in f.read().strip().splitlines():
        comp = []
        for elv in line.split(','):
            fisrt, end = elv.split('-')
            comp.append(list(range(int(fisrt), int(end) + 1)))
        count += 1 if all(asgmnt in comp[0] for asgmnt in comp[1]) or all(asgmnt in comp[1] for asgmnt in comp[0]) else 0

print(count)
