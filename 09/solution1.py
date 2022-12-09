import sys


h_pos = 0j
t_pos = 0j
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
                h_pos += 1
                t_pos = check_tpos(h_pos, t_pos)
                visit.append(t_pos)
        elif direction == 'U':
            for i in range(distant):
                h_pos += 1j
                t_pos = check_tpos(h_pos, t_pos)
                visit.append(t_pos)
        elif direction == 'L':
            for i in range(distant):
                h_pos -= 1
                t_pos = check_tpos(h_pos, t_pos)
                visit.append(t_pos)
        elif direction == 'D':
            for i in range(distant):
                h_pos -= 1j
                t_pos = check_tpos(h_pos, t_pos)
                visit.append(t_pos)

print(len(set(visit)))
