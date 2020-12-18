import itertools

with open('input.txt') as f:
    lines = f.read().splitlines()

names = []
values = {}

for line in lines:
    name_A = line.split()[0]
    name_B = line.split()[-1]
    name_B = name_B[:-1]
    value = int(line.split()[3])
    if line.split()[2] == 'lose':
        value *= -1
    if name_A not in names:
        names.append(name_A)
    if name_B not in names:
        names.append(name_B)
    values[(name_A, name_B)] = value

print(names)

layouts = list(itertools.permutations(names))

max_val = 0
for layout in layouts:
    maximum = True
    cur_val = 0
    for i in range(len(layout)):
        name_1 = layout[i - 1]
        name_2 = layout[i]
        try:
            name_3 = layout[i+1]
        except IndexError:
            name_3 = layout[0]
        cur_val += values[(name_2, name_1)]
        cur_val += values[(name_2, name_3)]
    if cur_val > max_val:
        max_val = cur_val
    print(cur_val)

print(f'The answer = {max_val}')
