with open('input.txt') as f:
    lines = f.read().splitlines()

# Part 1 & 2: Find Sue who sent you a package by looking at certain items she ownes
# Approach part 1 & 2 --> For every Sue entries see if all match the Sue who sent package
# If a single entry does not match, test is false and continue to next Sue

# See puzzle description on the website for input regarding ue who sent the package
sue_who_sent_package = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0,
                        'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

all_sues = {}

for line in lines:
    number_sue = line.split(':')[0]
    all_sues[number_sue] = {}
    string = line[len(number_sue) + 2:]
    sue_data = string.split(', ')
    for i in range(len(sue_data)):
        all_sues[number_sue][sue_data[i].split(': ')[0]] = int(sue_data[i].split(': ')[1])

matching_sues = []
for sue in all_sues.keys():
    test_part_1, test_part_2 = True, True
    for key in all_sues[sue].keys():
        if all_sues[sue][key] != sue_who_sent_package[key]:
            test_part_1 = False
        if key in ('cats', 'trees'):
            if all_sues[sue][key] <= sue_who_sent_package[key]:
                test_part_2 = False
        elif key in ('pomeranians', 'goldfish'):
            if all_sues[sue][key] >= sue_who_sent_package[key]:
                test_part_2 = False
        elif all_sues[sue][key] != sue_who_sent_package[key]:
            test_part_2 = False
    if test_part_1:
        print(f'Part 1: {sue} is the Sue who sent the package')
        matching_sues.append(sue)
    if test_part_2:
        print(f'Part 2: Oh no, {sue} is the Sue who sent the package')
        matching_sues.append(sue)
