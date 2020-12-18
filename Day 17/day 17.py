import itertools

containers = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]

comb = []

for i in range(len(containers)):
    value = itertools.combinations(containers, i)
    for item in list(value):
        comb.append(item)

answer = 0
for line in comb:
    total = 0
    for container in line:
        total += container
        if total > 150:
            break
    if total == 150:
        answer += 1

print(f'the answer = {answer} combinations')