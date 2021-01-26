import itertools
with open('input.txt') as f:
    lines = f.read().splitlines()

# Part 1: find the maximum happiness possible by arranging guest on a circular table
# Approach:
# Make a dict with happiness per neigbor; also make a set of names
# Use itertools to determine every table configuration
# Determine happiness per configuration and kep track of maximum
# Prt 2: Just as part one, but not a circular configuration but just plain list configuration

names = set()
happiness_data = {}

for line in lines:
    name_A, name_B = line.split()[0], line.split()[-1][:-1]
    happiness = int(line.split()[3])
    if line.split()[2] == 'lose':
        happiness *= -1
    names.update((name_A, name_B))
    happiness_data[(name_A, name_B)] = happiness

all_layouts = list(itertools.permutations(names))

maximum_happiness_part_1 = 0
maximum_happiness_part_2 = 0
for layout in all_layouts:
    current_happiness_part_1 = 0
    current_happiness_part_2 = 0
    for i in range(len(layout)):
        if i == len(layout) - 1:
            current_happiness_part_1 += happiness_data[(layout[i], layout[0])] + happiness_data[(layout[0], layout[i])]
        else:
            current_happiness_part_1 += happiness_data[(layout[i], layout[i + 1])] + happiness_data[(layout[i + 1], layout[i])]
            current_happiness_part_2 += happiness_data[(layout[i], layout[i + 1])] + happiness_data[(layout[i + 1], layout[i])]
    if current_happiness_part_1 > maximum_happiness_part_1:
        maximum_happiness_part_1 = current_happiness_part_1
    if current_happiness_part_2 > maximum_happiness_part_2:
        maximum_happiness_part_2 = current_happiness_part_2

print(f'Part 1: The maximum possible happiness is {maximum_happiness_part_1}')
print(f'Part 2: The maximum possible happiness is including me is {maximum_happiness_part_2}')
