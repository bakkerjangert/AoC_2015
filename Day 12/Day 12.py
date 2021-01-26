import re
with open('input.txt') as f:
    lines = f.read().splitlines()

# Part 1 & 2: find the sum of numbers in string; note that numbers may contain more characters and can be negative
# Approach:
# Part 1: if digit or - is found, keep track of the next chars untill None digit or - is found; then add number to total
# Mind: negative number right behind other number is NOT accounted for (not necessary for my input)
# Mind: Last entry shall be None digit and None - (not ncessary)
# Part 2: Find inner {} with regex (actually used regex finds inner (); Replaced { with ( and } with ) for convience)
# Then check every inner part for ':"red"' --> if present remove inner part from string
# Else only remove outer '(' and ')'
# Repeat process till no inner {} are found and count numbers with code from part 1


def get_sum(string):
    total_sum_of_numbers = 0
    number = ''
    for i in range(len(string)):
        if string[i].isdigit() or (string[i] == '-' and number == ''):
            number += string[i]
        elif len(number) > 0:
            total_sum_of_numbers += int(number)
            number = ''
    return total_sum_of_numbers


string_part_1 = lines[0]
print(f'Part 1: The total sum = {get_sum(string_part_1)}')

string_part_2 = lines[0].replace('{', '(').replace('}', ')')
search_value = ':"red"'
inner_parentises = re.findall('\([^()]*\)', string_part_2)

while len(inner_parentises) > 0:
    for sub_string in inner_parentises:
        if search_value in sub_string:
            string_part_2 = string_part_2.replace(sub_string, '')
        else:
            string_part_2 = string_part_2.replace(sub_string, sub_string[1:-1])
    inner_parentises = re.findall('\([^()]*\)', string_part_2)

print(f'Part 2: The total sum = {get_sum(string_part_2)}')
