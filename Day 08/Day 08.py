import re

with open('input.txt') as f:
    lines = f.read().splitlines()

# Part 1 & 2: Diference in strings with / without escape characters
# Approach part 1 --> replace all escape sequences with right amount of 'x' and trim the beginning and ending "
# Approach part 2 --> replace all ecaped characters with 'x' times required chars in escape sequence
# use regex to simplify things and then just add len(string) to totals

characters_in_line = 0
characters_in_string_part_1 = 0
characters_in_string_part_2 = 0

for line in lines:
    # Part 1
    string_part1 = line[1: -1]
    string_part1 = string_part1.replace('\\\\', 'x')
    string_part1 = string_part1.replace('\\\"', 'x')
    string_part1 = re.sub(r'\\x..', 'x', string_part1)
    # Part 2
    string_part2 = line[1:-1]
    string_part2 = re.sub(r'\\x\\\\', 'xxxxxxx', string_part2)
    string_part2 = re.sub(r'\\x\\.', 'xxxxxx', string_part2)
    string_part2 = re.sub(r'\\x.\\', 'xxxxxx', string_part2)
    string_part2 = re.sub(r'\\x""', 'xxxxxxx', string_part2)
    string_part2 = re.sub(r'\\x".', 'xxxxxx', string_part2)
    string_part2 = re.sub(r'\\x."', 'xxxxxx', string_part2)
    string_part2 = re.sub(r'\\x..', 'xxxxx', string_part2)
    string_part2 = string_part2.replace('\\\"', 'xxxx')
    string_part2 = string_part2.replace('\\\\', 'xxxx')
    string_part2 = string_part2.replace('\"', 'xx')
    string_part2 = string_part2.replace('\\', 'xx')
    string_part2 = 'xxx' + string_part2 + 'xxx'
    # add characters to total
    characters_in_line += len(line)
    characters_in_string_part_1 += len(string_part1)
    characters_in_string_part_2 += len(string_part2)

print(f'Part 1: The answer is {characters_in_line} - {characters_in_string_part_1} = '
      f'{characters_in_line - characters_in_string_part_1}')

print(f'Part 2: The answer is {characters_in_string_part_2} - {characters_in_line} = '
      f'{characters_in_string_part_2 - characters_in_line}')
