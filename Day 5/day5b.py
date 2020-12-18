with open('input.txt') as f:
    lines = f.read().splitlines()


nice_string_count = 0
nice_strings = []

for line in lines:
    # Check for double strings
    double_count = 0
    for char in range(len(line) - 1):
        double_count += line.count(str(line[char] + line[char + 1])) - 1
    if double_count == 0:
        # String is evil
        continue

    # Check for repeating letter with one in between
    triple_count = 0
    for char in range(len(line) - 2):
        if line[char] == line[char + 2]:
            # string is nice
            nice_string_count += 1
            nice_strings.append(line)
            break


for line in nice_strings:
    print(line)
print('-' * 10)
print('The answer is', len(nice_strings))
