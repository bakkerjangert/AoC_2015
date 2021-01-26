# Advent of Code 2015 - Day 01 part a & b
# Read input data
with open('input.txt') as f:
    lines = f.read().splitlines()

print(f'There are {len(lines[0])} instructions in the input data')

# Part 1
# To what floor do the instructions take Santa?
start_floor = 0
go_up = lines[0].count('(')
go_down = lines[0].count(')')
print(f'The answer is to part 1: The final floor Santa reaches is floor {start_floor + go_up - go_down}')

# Part 2
# Find the position of the first character that causes him to enter the basement
instruction_index = 0
current_level = 0
# Approach: loop till basement is reached; i.o.w. level = -1
# Assumption: Basement is reached in first loop through the input data
for char in lines[0]:
    if char == '(':
        current_level += 1
    elif char == ')':
        current_level -= 1
    if current_level == -1:
        # basement found
        break
    instruction_index += 1

print(f'The answer is to part 2: The basement is reached for the first time at character position {instruction_index + 1}')

