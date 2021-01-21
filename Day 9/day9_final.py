import itertools

with open('input.txt') as f:
    lines = f.read().splitlines()

# Part 1 & 2: Find shortest and longest path between cities
# Approach:
# Generate dict with distances (note: 2 entries per line: A -> B = distance and B -> A = distance for convience)
# Generate permutations of unique city list; use itertools package (to do --> Wrte code myself)
# Brute force the lengths of permutations to deterime the answers

unique_cities = set()
distances = {}

for line in lines:
    city_A, city_B, distance = line.split()[0], line.split()[2], int(line.split()[-1])
    unique_cities.add(city_A), unique_cities.add(city_B)
    distances[city_A, city_B], distances[city_B, city_A] = distance, distance

all_possible_paths = list(itertools.permutations(unique_cities))

minimum_length = sum(distances.values())
maximum_length = 0

for path in all_possible_paths:
    current_path_length = 0
    for i in range(len(path) - 1):
        current_path_length += distances[(path[i], path[i + 1])]
    if current_path_length > maximum_length:
        maximum_length = current_path_length
    if current_path_length < minimum_length:
        minimum_length = current_path_length

print(f'Part 1: The shortest route is {minimum_length}')
print(f'Part 2: The longest route is {maximum_length}')
