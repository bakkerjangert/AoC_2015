with open('input.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    input_list = line

print(type(input_list))
santa_coord = (0, 0)
robo_coord = (0, 0)

houses = {}

counter = 2

for char in input_list:
    if counter % 2 == 0:
        if santa_coord not in houses.keys():
            houses[santa_coord] = 1
        else:
            houses[santa_coord] += 1
        if char == '^':
            santa_coord = (santa_coord[0], santa_coord[1] + 1)
        elif char == '>':
            santa_coord = (santa_coord[0] + 1, santa_coord[1])
        elif char == '<':
            santa_coord = (santa_coord[0] - 1, santa_coord[1])
        elif char == 'v':
            santa_coord = (santa_coord[0], santa_coord[1] - 1)
    if counter % 2 != 0:
        if robo_coord not in houses.keys():
            houses[robo_coord] = 1
        else:
            houses[robo_coord] += 1
        if char == '^':
            robo_coord = (robo_coord[0], robo_coord[1] + 1)
        elif char == '>':
            robo_coord = (robo_coord[0] + 1, robo_coord[1])
        elif char == '<':
            robo_coord = (robo_coord[0] - 1, robo_coord[1])
        elif char == 'v':
            robo_coord = (robo_coord[0], robo_coord[1] - 1)

    counter += 1


print('The answer is', len(houses))

