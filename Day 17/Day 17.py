import itertools
with open('input.txt') as f:
    lines = f.read().splitlines()

# Part 1 & 2: possible combination of cointainers to fit a certain amount of egg-nog
# Approach part 1 & 2 --> Brute-force: use itertols to generate all possible combinations and check wether it matches

available_containers = tuple(map(int, lines))
required_liters = 150
possible_combinations = 0
possible_combinations_with_minimum_containers = 0
minimum_required_containers = len(available_containers)  # max value; update in loop when 150 liters is found

for i in range(len(available_containers)):
    combinations_with_length_i = itertools.combinations(available_containers, i)
    for combination in combinations_with_length_i:
        if sum(combination) == 150:
            possible_combinations += 1
            if len(combination) < minimum_required_containers:
                minimum_required_containers = len(combination)
                possible_combinations_with_minimum_containers = 1
            elif len(combination) == minimum_required_containers:
                possible_combinations_with_minimum_containers += 1

print(f'Part 1: There are {possible_combinations} combinations to fit {required_liters} liters')
print(f'Part 2: There are {possible_combinations_with_minimum_containers} combinations to fit '
      f'{required_liters} liters in {minimum_required_containers} containers')
