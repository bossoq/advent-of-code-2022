import sys


last_rucksack = ''
common_items = []
badges = []
with open(sys.argv[1], 'r') as f:
    for idx, line in enumerate(f):
        rucksack = line.strip()
        if idx % 3 == 0:
            last_rucksack = rucksack
            common_items = []
        elif idx % 3 == 1:
            for item in last_rucksack:
                if item in rucksack:
                    common_items.append(item)
        else:
            for item in common_items:
                if item in rucksack:
                    badges.append(item)
                    break

print(sum([ord(item) - 96 if item.islower() else ord(item) - 38 for item in badges]))
