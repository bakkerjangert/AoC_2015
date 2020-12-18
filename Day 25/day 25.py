tar_row = 2978
tar_col = 3083

delta_col = tar_col - 1
row_c1 = tar_row + delta_col

code = 1
for r in range(1, row_c1 + 1):
    code += r - 1
    # print(code)

target_code = code + delta_col

print(target_code)

start_code = 20151125

for i in range(target_code - 1):
    start_code *= 252533
    start_code = start_code % 33554393
    # print(start_code)
    if i % 1000 == 0:
        print(f'at {round(i / target_code * 100, 2)} %')

print(f'the answer is {start_code}')