with open('input.txt') as f:
    lines = f.read().splitlines()


def move(current_position, direction):
    """
    :param current_position: current position
    :param direction: direction to move in --> ^, >, v or <
    :return: position after the movement
    """
    delta = directions[direction]
    return current_position[0] + delta[0], current_position[1] + delta[1]


directions = {'^': (0, 1),
              '>': (1, 0),
              'v': (0, -1),
              '<': (-1, 0)}

# Part 1 & 2
# Part 1: How many houses receive at least one present, while only Santa is running?
# part 2: How many total feet of ribbon should they order?
# Approach: determine all coordinates and keep track of a set of uniques house coordinates

santas_only_position, santas_position, robo_santas_position = (0, 0), (0, 0), (0, 0)
visted_houses_by_santa, visted_houses_together = set(), set()
instruction_index = 0

for direction in lines[0]:
    # Part 1
    visted_houses_by_santa.add(santas_only_position)
    santas_only_position = move(santas_only_position, direction)
    # Part 2
    if instruction_index % 2 == 0:
        # Santa moves
        visted_houses_together.add(santas_position)
        santas_position = move(santas_position, direction)
    else:
        # Robo-Santa moves
        visted_houses_together.add(robo_santas_position)
        robo_santas_position = move(robo_santas_position, direction)
    instruction_index += 1

print(f'Part 1: Santa has visited {len(visted_houses_by_santa)} on his own')
print(f'Part 2: Santa + Robo-Santa have visited {len(visted_houses_together)} together')
