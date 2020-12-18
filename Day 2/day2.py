with open('input.txt') as f:
    lines = f.read().splitlines()

presents = []
for line in lines:
    presents.append([int(line.split('x')[0]), int(line.split('x')[1]), int(line.split('x')[2])])

total = 0
ribbon = 0

for present in presents:
    total += 2 * present[0] * present[1]
    total += 2 * present[1] * present[2]
    total += 2 * present[0] * present[2]
    temp = sorted(present)
    total += temp[0] * temp[1]
    ribbon += temp[0] * 2 + temp[1] * 2 + present[0] * present[1] * present[2]

print('The answer feet of paper =', total)
print('The answer feet of ribbon =', ribbon)