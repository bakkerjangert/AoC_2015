import itertools
import math
import copy

with open('input.txt') as f:
    lines = f.read().splitlines()


# Swap function
def swap_positions(data, pos1, pos2):
    data[pos1], data[pos2] = data[pos2], data[pos1]
    return list


def swap_set(data):
    swap_list = []
    for i in range(len(data)):
        sub_set = []
        for j in range(i + 1, len(data)):
            sub_set.append([i, j])
        swap_list.append([sub_set.copy()])
        sub_set.clear()
    return swap_list


def comb(data_set):
    total_set = set()
    shifts = []
    max_pos = len(data_set) - 1


cities = []
distances = {}

for line in lines:
    city_A = line.split()[0]
    city_B = line.split()[2]
    dist = int(line.split()[-1])
    if city_A not in cities:
        cities.append(city_A)
    if city_B not in cities:
        cities.append(city_B)
    distances[(city_A, city_B)] = dist
    distances[(city_B, city_A)] = dist

print(cities)

paths = swap_set(cities)
ans = 1
for path in paths:
    print(path)
    ans *= len(path[0])
    print(ans)

print(ans)



exit()



paths = list(itertools.permutations(cities))

max_len = sum(list(distances.values()))
for cities in paths:
    minimum = True
    cur_len = 0
    for i in range(len(cities) - 1):
        city_1 = cities[i]
        city_2 = cities[i + 1]
        cur_len += distances[(city_1, city_2)]
        if cur_len > max_len:
            minimum = False
            break
    if minimum:
        max_len = cur_len
    print(cur_len)

print(f'The answer = {max_len}')
