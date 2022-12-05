import re
import sys


total_col = 0
crate_list = []
adj_crate_list = []
with open(sys.argv[1], 'r') as f:
    for line in f.read().splitlines():
        if re.search(r'(\d+)\s+', line):
            if len(adj_crate_list) == 0:
                adj_crate_list = [[crate for crate in reversed(crate_col) if crate != ' '] for crate_col in crate_list]
            match = re.search(r'move (\d+) from (\d+) to (\d+)', line)
            if match:
                num_crates_move = int(match.group(1))
                move_from = int(match.group(2)) - 1
                move_to = int(match.group(3)) - 1
                move_crate = adj_crate_list[move_from][-num_crates_move:]
                adj_crate_list[move_from] = adj_crate_list[move_from][:-num_crates_move]
                adj_crate_list[move_to] += move_crate
        elif len(line) > 0:
            if total_col == 0:
                total_col = int((len(line) + 1) / 4)
            for idx, i in enumerate(range(1, total_col * 4, 4)):
                try:
                    crate_list[idx].append(line[i])
                except IndexError:
                    crate_list.append([line[i]])

word = ''
for crate in adj_crate_list:
    word += crate[-1]
print(word)
