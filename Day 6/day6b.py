# . means turned of; # means turned on

with open('input.txt') as f:
    lines = f.read().splitlines()

start_x = []
start_y = []
end_x = []
end_y = []
switch = []

for line in lines:
    start_x_str = line.split(' through ')[0]
    start_x_str = start_x_str.split(',')[0]
    start_x_str = int(start_x_str.split(' ')[-1])
    start_x.append(start_x_str)

    start_y_str = line.split(' through ')[0]
    start_y_str = int(start_y_str.split(',')[1])
    start_y.append(start_y_str)

    end_x_str = line.split(' through ')[1]
    end_x_str = int(end_x_str.split(',')[0])
    end_x.append(end_x_str)

    end_y_str = line.split(' through ')[1]
    end_y_str = int(end_y_str.split(',')[1])
    end_y.append(end_y_str)

    if ' on ' in line:
        switch.append('on')
    elif ' off ' in line:
        switch.append('off')
    else:
        switch.append('toggle')

# for i in range(len(start_y)):
#     print(start_x[i], start_y[i], end_x[i], end_y[i], switch[i])
# quit()

# Buid empty grid


x_size = 1000
y_size = 1000

grid = []

for y in range(y_size):
    grid.append([])
    for x in range(x_size):
        grid[y].append(0)

for i in range(len(start_x)):
    for y in range(start_y[i], end_y[i] + 1):
        for x in range(start_x[i], end_x[i] + 1):
            if switch[i] == 'on':
                grid[y][x] += 1
            elif switch[i] == 'off':
                if grid[y][x] > 0:
                    grid[y][x] -= 1
            else:
                grid[y][x] += 2

lights = 0

for line in grid:
    for char in line:
        lights += char

print('The answer is', lights)

### Code to print grid below
# for line in grid:
#     for char in line:
#         print(char, end='')
#     print('')
