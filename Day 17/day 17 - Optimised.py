import itertools

containers = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]
combos = []

for i in range(1, len(containers)):
    combos.append(list(itertools.combinations(containers, i)))

answer = 0
for combo in combos:
    liters = sum(map(int, combo[0]))
    if liters == 150:
        answer += 1

print(f'the answer = {answer} combinations')