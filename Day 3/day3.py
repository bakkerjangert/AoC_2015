with open('input.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    input_list = line

print(type(input_list))
coord = (0, 0)

houses = {}

for char in input_list:
    if coord not in houses.keys():
        houses[coord] = 1
    else:
        houses[coord] += 1
    if char == '^':
        coord = (coord[0], coord[1] + 1)
    elif char == '>':
        coord = (coord[0] + 1, coord[1])
    elif char == '<':
        coord = (coord[0] - 1, coord[1])
    elif char == 'v':
        coord = (coord[0], coord[1] - 1)

print('The answer is', len(houses))

