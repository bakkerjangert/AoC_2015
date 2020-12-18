data = [[4, -2, 0, 0, 5],
        [0, 5, -1, 0, 8],
        [-1, 0, 5, 0, 6],
        [0, 0, -2, 2, 1]]

max_val, max_val_500 = 0, 0
# Set value below to True is you want to print step results
print_values = False

for i in range(101):
    for j in range(101 - i):
        for k in range(101 - i - j):
            for l in range(101 - i - j - k):
                if (i + j + k + l) < 100:  # Check wether exactly 100 spoons are used
                    continue
                factors = [i, j, k, l]
                cap, dur, fla, tex, cal = 0, 0, 0, 0, 0
                for pos in range(4):
                    cap += data[pos][0] * factors[pos]
                    dur += data[pos][1] * factors[pos]
                    fla += data[pos][2] * factors[pos]
                    tex += data[pos][3] * factors[pos]
                    cal += data[pos][4] * factors[pos]
                if cap <= 0 or dur <= 0 or fla <= 0 or tex <= 0:  # negative values become 0 resulting in 0 total score
                    continue
                cur_val = cap * dur * fla * tex
                if print_values:
                    print(f'i = {i}, j = {j}, k = {k}, l = {l}, sum = {i+j+k+l} with value = {cur_val}')
                if cur_val > max_val:
                    max_val = cur_val
                if cal == 500 and cur_val > max_val_500:
                    max_val_500 = cur_val

print(f'The answer to part 1 is {max_val}')
print(f'The answer to part 2 is {max_val_500}')
