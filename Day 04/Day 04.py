import hashlib

puzzle_input = 'yzbqklnj'
# Test input
# puzzle_input = 'abcdef'
# puzzle_input = 'pqrstuv'

# Part 1: Find first number which MD5 hash string starts with at least 5 leading zeros
# Part 2: Find first number which MD5 hash string starts with at least 6 leading zeros
# Approach: Just bruteforce from 'String' & 1, 1 + i, ... to n and check weather part 1 or part 2 is full filled
# Break while loop if both part 1 and part 2 are found

current_number = 0
part_1_found, part_2_found = False, False
answer_part_1, answer_part_2 = None, None

while not part_1_found or not part_2_found:
    test = puzzle_input + str(current_number)
    if hashlib.md5(test.encode('utf-8')).hexdigest().startswith('00000') and not part_1_found:
        print(f'The answer to part 1 is {current_number}')
        part_1_found = True
    if hashlib.md5(test.encode('utf-8')).hexdigest().startswith('000000') and not part_2_found:
        print(f'The answer to part 2 is {current_number}')
        part_2_found = True
    current_number += 1
