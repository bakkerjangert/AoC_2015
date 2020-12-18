with open('input.txt') as f:
    lines = f.read().splitlines()

data = []
for line in lines:
    data1 = int(line.split()[3])
    data2 = int(line.split()[6])
    data3 = int(line.split()[-2])
    data.append((data1, data2, data3))

time = 2503
max_val = 0
for line in data:
    print(line[1] + line[2])
    cur_val = 0
    cycles = time // (line[1] + line[2])
    print(cycles)
    rest = time % (line[1] + line[2])
    print(rest)
    print(cycles * (line[1] + line[2]) + rest)
    print('\n---')
    cur_val += cycles * line[0] * line[1] + min(rest, line[1]) * line[0]
    if cur_val > max_val:
        max_val = cur_val

print(f'The answer is {max_val}')