with open('input.txt') as f:
    lines = f.read().splitlines()

# First get list of presents with dimensions (h x l x w)

presents = []
for line in lines:
    presents.append([int(line.split('x')[0]), int(line.split('x')[1]), int(line.split('x')[2])])
    presents[-1].sort()

total = 0
ribbon = 0

for present in presents:
    # Add sides
    total += 2 * present[0] * present[1]
    total += 2 * present[1] * present[2]
    total += 2 * present[0] * present[2]

    # Add additional paper, dimension already sorted
    total += present[0] * present[1]

    # Add ribbon (part 2)
    ribbon += present[0] * 2 + present[1] * 2 + present[0] * present[1] * present[2]

print('The answer feet of paper =', total)
print('The answer feet of ribbon =', ribbon)