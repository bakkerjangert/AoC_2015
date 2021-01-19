import re
import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()

modes = {'off': 0,
         'on': 1,
         'toggle': -1}

# Part 1 & 2: Find number of burning lights in 1000 x 1000 grid after applying all instructions
# Approach: get instruction per line; use regex to get coordinate numbers
# Grid is represented as numpy array
# --> Part 1: 0.0 = light off; 1.0 = light on
# --> Part 2: foat = brigthness >= 0.0
# per line generate sub-grid and implement that in to the grid

# Generate instrcutions
instructions = []
for line in lines:
    coordinates = list(map(int, re.findall(r'\d+', line)))
    for mode in modes.keys():
        if mode in line:
            coordinates.append(mode)
    instructions.append(coordinates)

# Generate initial states (all lights turned off at 0.0)
grid_part_1 = np.zeros((1000, 1000))
grid_part_2 = np.zeros((1000, 1000))

for instruction in instructions:
    row, col = (instruction[1], instruction[3]), (instruction[0], instruction[2])
    # Generate sub-grid
    if instruction[4] in ('on', 'off'):
        if instruction[4] == 'off':
            # Turn off sub-grid
            sub_grid_part_1 = np.zeros((row[1] - row[0] + 1, col[1] - col[0] + 1))
            sub_grid_part_2 = np.where(grid_part_2[row[0]:row[1] + 1, col[0]: col[1] + 1] == 0.0, 0.0, -1.0)
            sub_grid_part_2 = np.add(sub_grid_part_2, grid_part_2[row[0]:row[1] + 1, col[0]: col[1] + 1])
        else:
            # Turn on sub-grid
            sub_grid_part_1 = np.ones((row[1] - row[0] + 1, col[1] - col[0] + 1))
            sub_grid_part_2 = np.add(grid_part_2[row[0]:row[1] + 1, col[0]: col[1] + 1],
                                     np.ones((row[1] - row[0] + 1, col[1] - col[0] + 1)))
    else:
        # Toggle sub-grid
        sub_grid_part_1 = np.where(grid_part_1[row[0]:row[1] + 1, col[0]: col[1] + 1] == 0.0, 1.0, 0.0)
        sub_grid_part_2 = np.add(grid_part_2[row[0]:row[1] + 1, col[0]: col[1] + 1],
                                 np.full((row[1] - row[0] + 1, col[1] - col[0] + 1), 2.0))
    # Implement sub-grid
    grid_part_1[row[0]:row[1] + 1, col[0]: col[1] + 1] = sub_grid_part_1
    grid_part_2[row[0]:row[1] + 1, col[0]: col[1] + 1] = sub_grid_part_2

print(f'Part 1: There are {int(grid_part_1.sum())} lights burning after following the instructions')
print(f'Part 2: The total brightness is {int(grid_part_2.sum())} after following the instructions')
