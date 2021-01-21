import re

with open('input.txt') as f:
    lines = f.read().splitlines()

len_lit = 0
for line in lines:
    print(line)
    len_lit += len(line)


len_screen = 0
for line in lines:
    print(line)
    string = line[1: -1]
    string = string.replace('\\\\', 'x')
    string = string.replace('\\\"', 'x')
    string = re.sub(r'\\x..', 'x', string)
    print(f'{string}')
    len_screen += len(string)



print(f'In string = {len_screen}; in mem = {len_lit}')
print(f'the answer is {len_lit - len_screen}')

