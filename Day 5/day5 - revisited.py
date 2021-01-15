with open('input.txt') as f:
    lines = f.read().splitlines()

naughty_string_parts = ('ab', 'cd', 'pq', 'xy')
vowels = 'aeiou'


def naughty_part_in_string(string):
    if any(x in string for x in naughty_string_parts):
        return True
    return False


def at_least_three_vowels_in_string(string):
    if sum(string.count(x) for x in vowels) >= 3:
        return True
    return False


def double_in_string(string):
    if any(x + x in string for x in set(tuple(string))):
        return True
    return False


def double_double_in_string(string):
    for i in range(len(string) - 1):
        if string[i: i + 2] in string[i + 2:]:
            return True
    return False


def repeated_letter_in_string(string):
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            return True
    return False

def check_part_1(string):
    if naughty_part_in_string(string):
        return False
    if not at_least_three_vowels_in_string(string):
        return False
    if not double_in_string(string):
        return False
    # All tests have passed; string must be nice
    return True


def check_part_2(string):
    if not repeated_letter_in_string(string):
        return False
    if not double_double_in_string(string):
        return False
    # All tests have passed; string must be nice
    return True


# Part 1 & 2: Find nice string by checking certain conditions
# Approach: Start with fastest check, end with slowest; if all checks pass nice string is found
# Order part 1: (1) naughty string-part, (2) vowel, (3) double letter
# Order part 2: (1) repeated letter, (2) double double in string

number_of_nice_strings_part_1, number_of_nice_strings_part_2 = 0, 0

for string in lines:
    if check_part_1(string):
        number_of_nice_strings_part_1 += 1
    if check_part_2(string):
        number_of_nice_strings_part_2 += 1

print(f'Part 1: There are {number_of_nice_strings_part_1} nice strings')
print(f'Part 2: Oh no, that is ridicules; there are {number_of_nice_strings_part_2} nice strings')
