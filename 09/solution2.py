import sys


all_pos = [0j] * 10
visit = [0j]


def check_tpos(h_pos: complex, t_pos: complex) -> complex:
    d = h_pos - t_pos
    shift_real = 0
    shift_imag = 0
    if abs(d.real) > 1:
        shift_real = d.real / abs(d.real)
        if abs(d.imag) > 0:
            shift_imag = d.imag / abs(d.imag)
    if abs(d.imag) > 1:
        shift_imag = d.imag / abs(d.imag)
        if abs(d.real) > 0:
            shift_real = d.real / abs(d.real)
    return t_pos + shift_real + shift_imag * 1j


with open(sys.argv[1], 'r') as f:
    for line in f.read().splitlines():
        direction, distant = line.split()
        distant = int(distant)
        if direction == 'R':
            for i in range(distant):
                all_pos[0] += 1
                for i in range(len(all_pos) - 1):
                    all_pos[i + 1] = check_tpos(all_pos[i], all_pos[i + 1])
                visit.append(all_pos[-1])
        elif direction == 'U':
            for i in range(distant):
                all_pos[0] += 1j
                for i in range(len(all_pos) - 1):
                    all_pos[i + 1] = check_tpos(all_pos[i], all_pos[i + 1])
                visit.append(all_pos[-1])
        elif direction == 'L':
            for i in range(distant):
                all_pos[0] -= 1
                for i in range(len(all_pos) - 1):
                    all_pos[i + 1] = check_tpos(all_pos[i], all_pos[i + 1])
                visit.append(all_pos[-1])
        elif direction == 'D':
            for i in range(distant):
                all_pos[0] -= 1j
                for i in range(len(all_pos) - 1):
                    all_pos[i + 1] = check_tpos(all_pos[i], all_pos[i + 1])
                visit.append(all_pos[-1])

print(len(set(visit)))
