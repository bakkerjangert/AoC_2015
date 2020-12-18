import itertools

with open('input.txt') as f:
    lines = f.read().splitlines()

packages = []

for line in lines:
    packages.append(int(line))

weight = sum(packages) // 4

r = 0
found = False
combinations = []
while True:
    r += 1
    lst = itertools.combinations(packages, r)
    for line in lst:
        if sum(line) == weight:
            combinations.append(line)
            found = True
    if found:
        break

answer = 999999999999999999999
for line in combinations:
    val = 1
    for char in line:
        val *= char
    if val < answer:
        answer = val

print(f'The answer = {answer}')



