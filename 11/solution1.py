import math
import re
import sys
from typing import List


monkey_dict = {}
all_test = 1
with open(sys.argv[1], 'r') as f:
    monkey = 'x'
    tmp_dict = {}
    for line in f.read().splitlines():
        monkey_match = re.match(r'^Monkey (?P<no>\d+):$', line)
        if monkey_match:
            monkey = monkey_match.group('no')
            tmp_dict = {}
        items_match = re.match(r'^\s+Starting items: (?P<items>.+)$', line)
        if items_match:
            tmp_dict['items'] = [int(item) for item in items_match.group('items').split(', ')]
        operation_match = re.match(r'^\s+Operation: new = (?P<operation>.+)$', line)
        if operation_match:
            tmp_dict['operation'] = operation_match.group('operation').split()
        test_match = re.match(r'^\s+Test: divisible by (?P<test>\d+)$', line)
        if test_match:
            tmp_dict['test'] = int(test_match.group('test'))
            all_test *= int(test_match.group('test'))
        decision_true_match = re.match(r'^\s+If true: throw to monkey (?P<decision>\d+)$', line)
        if decision_true_match:
            tmp_dict['decision'] = [decision_true_match.group('decision')]
        decision_false_match = re.match(r'^\s+If false: throw to monkey (?P<decision>\d+)$', line)
        if decision_false_match:
            tmp_dict['decision'].append(decision_false_match.group('decision'))
        monkey_dict[monkey] = tmp_dict


def evaluation(operation: List[str], old: int) -> int:
    x, op, y = operation
    x = old if x == 'old' else int(x)
    y = old if y == 'old' else int(y)
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y


relief_factor = 3
loop = 20
monkey_inspect = [0] * len(monkey_dict.keys())
for _ in range(loop):
    for key, val in monkey_dict.items():
        monkey = key
        items, operation, test, decision = val.values()
        for item in items:
            monkey_inspect[int(monkey)] += 1
            worry_level = (evaluation(operation, item) // relief_factor) % all_test
            if worry_level % test == 0:
                monkey_dict[decision[0]]['items'].append(worry_level)
            else:
                monkey_dict[decision[1]]['items'].append(worry_level)
        monkey_dict[monkey]['items'] = []

monkey_inspect.sort()
print(math.prod(monkey_inspect[-2:]))
