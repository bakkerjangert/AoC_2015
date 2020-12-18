# Advent of Code 2015 - Day 1 part a & b
# Read input data
with open('input.txt') as f:
    lines = f.read().splitlines()

print(f'There are {len(lines[0])} instructions in the input data')

# Part a
start_floor = 0
up = lines[0].count('(')
down = lines[0].count(')')

print(f'The answer is to part 1: The final floor after all input data is processed is floor {start_floor + up - down}')

# Part b
counter = 0
level = 0
# loop till basement is reached; i.o.w. level = -1
# assumption: Basement is reached in first loop through input data
for char in lines[0]:
    counter += 1
    if char == '(':
        level += 1
    elif char == ')':
        level -= 1
    if level == -1:
        # basement found
        break

print(f'The answer is to part 2: The basement is reached for the first time at instruction {counter}')

