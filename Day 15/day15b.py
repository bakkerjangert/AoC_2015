data = [[4, -2, 0, 0, 5],
        [0, 5, -1, 0, 8],
        [-1, 0, 5, 0, 6],
        [0, 0, -2, 2, 1],]

cap = 0
dur = 0
fla = 0
tex = 0
cal = 0

max_val = 0

print_step = False

for i in range(101):
    for j in range(101 - i):
        for k in range(101 - i - j):
            for l in range(101 - i - j - k):
                if (i + j + k + l) < 100:
                    continue
                if print_step:
                    print(f'i = {i}, j = {j}, k = {k}, l = {l}, sum = {i+j+k+l}')
                cap = data[0][0] * i + data[1][0] * j + data[2][0] * k + data[3][0] * l
                if cap <= 0:
                    continue
                dur = data[0][1] * i + data[1][1] * j + data[2][1] * k + data[3][1] * l
                if dur <= 0:
                    continue
                fla = data[0][2] * i + data[1][2] * j + data[2][2] * k + data[3][2] * l
                if fla <= 0:
                    continue
                tex = data[0][3] * i + data[1][3] * j + data[2][3] * k + data[3][3] * l
                if tex <= 0:
                    continue
                cal = data[0][4] * i + data[1][4] * j + data[2][4] * k + data[3][4] * l
                cur_val = cap * dur * fla * tex
                if cur_val > max_val and cal == 500:
                    max_val = cur_val

print(f'The answer is {max_val}')



