import itertools

with open('input.txt') as f:
    lines = f.read().splitlines()

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


paths = list(itertools.permutations(cities))

max_len = 0
for cities in paths:
    minimum = True
    cur_len = 0
    for i in range(len(cities) - 1):
        city_1 = cities[i]
        city_2 = cities[i + 1]
        cur_len += distances[(city_1, city_2)]
    if cur_len > max_len:
        max_len = cur_len
    print(cur_len)

print(f'The answer = {max_len}')
