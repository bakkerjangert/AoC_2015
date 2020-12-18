with open('input.txt') as f:
    lines = f.read().splitlines()

evil = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']

print(len(lines))

nice_string_count = 0
nice_strings = []

for line in lines:
    # Check for evil double strings
    if any(x in line for x in evil):
        continue

    # Check for at least 3 vowels
    vowel_count = 0
    for char in vowels:
        vowel_count += line.count(char)
    if vowel_count < 3:
        continue

    # check for double letters
    for char in range(len(line) - 1):
        if line[char] == line[char + 1]:
            nice_string_count += 1
            nice_strings.append(line)
            break

for line in nice_strings:
    print(line)
print('-' * 10)
print('The answer is', len(nice_strings))
