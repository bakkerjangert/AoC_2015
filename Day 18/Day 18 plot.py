import matplotlib.pyplot as plt
import matplotlib.patches as patches
with open('input.txt') as f:
    lines = f.read().splitlines()

def plot(grid1, grid2, name):
    coords1, coords2 = [], []
    for line in grid1:
        coords1.append(list(map(int, line)))
    for line in grid2:
        coords2.append(list(map(int, line)))
    f = plt.figure()
    f.add_subplot(1, 2, 1)
    plt.imshow(coords1, cmap='Greys')
    f.add_subplot(1, 2, 2)
    plt.imshow(coords2, cmap='Greys')
    plt.savefig(name + '.png')
    plt.close()

def set_corners_on(grid):
    grid[1] = '01' + grid[1][2:-2] + '10'
    grid[-2] = '01' + grid[-2][2:-2] + '10'
    return grid

# Part 1 & 2: determine lit bulbs after 100 timesteps
# Approach part 1 & 2 --> Loop over current grid and determine if bulb is lit or dark; keep track in copy of grid
# Rince and repeat per time step
# Add layer of dark bulbs as outer ring for easier coding


grid_part_1 = []  # Grid with '0' (off) and '1' (on). Add outer layer of '0' for easier coding
for line in lines:
    grid_part_1.append('0' + line.replace('.', '0').replace('#', '1') + '0')
grid_part_1.insert(0, '0' * len(grid_part_1[-1]))
grid_part_1.append('0' * len(grid_part_1[0]))
grid_part_2 = set_corners_on(grid_part_1.copy())

maximum_row = len(grid_part_1) - 1
maximum_column = len(grid_part_1[0]) - 1

for time in range(100):
    next_grid_part_1 = grid_part_1.copy()
    next_grid_part_2 = grid_part_2.copy()
    plot(grid_part_1, grid_part_2, 'fig' + str(time))
    for row in range(1, len(grid_part_1) - 1):  # Dont loop over outer zeros
        for column in range(1, len(grid_part_1[0]) - 1):  # Dont loop over outer zeros
            burning_neighbors_part_1, burning_neighbors_part_2 = 0, 0
            for delta_row in [-1, 0, 1]:
                for delta_column in [-1, 0, 1]:
                    if delta_row == 0 and delta_column == 0:
                        pass  # skip middle node
                    else:
                        burning_neighbors_part_1 += int(grid_part_1[row + delta_row][column + delta_column])
                        burning_neighbors_part_2 += int(grid_part_2[row + delta_row][column + delta_column])
            if grid_part_1[row][column] == '1':
                if burning_neighbors_part_1 in [2, 3]:
                    pass
                else:
                    next_grid_part_1[row] = next_grid_part_1[row][:column] + '0' + next_grid_part_1[row][column + 1:]
            elif grid_part_1[row][column] == '0':
                if burning_neighbors_part_1 != 3:
                    pass
                else:
                    next_grid_part_1[row] = next_grid_part_1[row][:column] + '1' + next_grid_part_1[row][column + 1:]
            if grid_part_2[row][column] == '1':
                if burning_neighbors_part_2 in [2, 3]:
                    pass
                else:
                    next_grid_part_2[row] = next_grid_part_2[row][:column] + '0' + next_grid_part_2[row][column + 1:]
            elif grid_part_2[row][column] == '0':
                if burning_neighbors_part_2 != 3:
                    pass
                else:
                    next_grid_part_2[row] = next_grid_part_2[row][:column] + '1' + next_grid_part_2[row][column + 1:]
    grid_part_1 = next_grid_part_1
    grid_part_2 = set_corners_on(next_grid_part_2.copy())

total_lights_after_100_steps_part_1 = 0
total_lights_after_100_steps_part_2 = 0
for i in range(len(grid_part_1)):
    total_lights_after_100_steps_part_1 += grid_part_1[i].count('1')
    total_lights_after_100_steps_part_2 += grid_part_2[i].count('1')

print(f'Part 1: There are {total_lights_after_100_steps_part_1} lights turned on after 100 steps')
print(f'Part 2: There are {total_lights_after_100_steps_part_2} lights turned on after 100 steps')


