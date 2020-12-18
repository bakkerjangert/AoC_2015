import re

with open('input.txt') as f:
    lines = f.read().splitlines()

len_lit = 0
for line in lines:
    len_lit += len(line)


len_screen = 0
for line in lines:
    string = line[1:-1]
    string = re.sub(r'\\x\\\\', 'xxxxxxx', string)
    string = re.sub(r'\\x\\.', 'xxxxxx', string)
    string = re.sub(r'\\x.\\', 'xxxxxx', string)
    string = re.sub(r'\\x""', 'xxxxxxx', string)
    string = re.sub(r'\\x".', 'xxxxxx', string)
    string = re.sub(r'\\x."', 'xxxxxx', string)
    string = re.sub(r'\\x..', 'xxxxx', string)
    string = string.replace('\\\"', 'xxxx')
    string = string.replace('\\\\', 'xxxx')
    string = string.replace('\"', 'xx')
    string = string.replace('\\', 'xx')
    string = 'xxx' + string + 'xxx'
    len_screen += len(string)



print(f'In string = {len_lit}; in mem = {len_screen}')
print(f'the answer is {len_screen - len_lit}')

