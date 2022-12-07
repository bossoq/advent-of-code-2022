import re
import sys


path_map = {}
root = [{}, {}, None, '/']
directory = root
with open(sys.argv[1], 'r') as f:
    for line in f.read().splitlines():
        cd_match = re.match(r'\$\scd\s(?P<dir>.+)', line)
        if cd_match:
            dir_name = cd_match.group('dir')
            if dir_name == '/':
                directory = root
            elif dir_name == '..':
                directory = directory[2]
            else:
                directory = directory[0][dir_name]

        ls_match = re.match(r'\$\sls', line)
        if ls_match:
            pass

        dir_match = re.match(r'dir\s(?P<dirname>.+)', line)
        if dir_match:
            dir_name = dir_match.group('dirname')
            if dir_name not in directory[0]:
                new_dir = [{}, {}, directory, directory[3] + dir_name + '/']
                directory[0][dir_name] = new_dir

        file_match = re.match(r'(?P<filesize>\d+)\s(?P<filename>.+)', line)
        if file_match:
            directory[1][file_match.group('filename')] = int(file_match.group('filesize'))

tot_sizes = {}


def get_sizes(directory: dict) -> int:
    sub_dirs, files, _, name = directory

    tot_size = sum(v for v in files.values()) + sum(get_sizes(sub_dir) for sub_dir in sub_dirs.values())
    tot_sizes[name] = tot_size

    return tot_size


get_sizes(root)

print(sum(s for s in tot_sizes.values() if s <= 100000))
