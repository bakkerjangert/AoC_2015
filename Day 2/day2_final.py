with open('input.txt') as f:
    lines = f.read().splitlines()

# Part 1 & 2
# Part 1: How many total square feet of wrapping paper should they order?
# part 2: How many total feet of ribbon should they order?

# Approach: Make a list of presents with dimensions (h x l x w), then dirive the answer by loping over listed list
# To make things easier the present dimensions are order from low to high
# By doing this the smallest side can be easaly determined by index [0] and [1]

presents = []
for line in lines:
    presents.append([int(line.split('x')[0]), int(line.split('x')[1]), int(line.split('x')[2])])
    presents[-1].sort()

sqf_of_wrapping_paper, ft_of_ribbon = 0, 0

for present in presents:
    # Add area of package + 1 additional smallest side (dimension already sorted)
    sqf_of_wrapping_paper += 3 * present[0] * present[1] + 2 * present[1] * present[2] + 2 * present[0] * present[2]
    # Add ribbon
    ft_of_ribbon += present[0] * 2 + present[1] * 2 + present[0] * present[1] * present[2]

print(f'The answer to part 1: They need to order {sqf_of_wrapping_paper} square feet of paper')
print(f'The answer to part 2: They need to order {ft_of_ribbon} feet of ribbon')
