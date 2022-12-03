import sys


prioritized = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        rucksack = line.strip()
        first_compartment, second_compartment = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
        for item in first_compartment:
            if item in second_compartment:
                prioritized.append(item)
                break

print(sum([ord(item) - 96 if item.islower() else ord(item) - 38 for item in prioritized]))
