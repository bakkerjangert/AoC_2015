import re

with open('input.txt') as f:
    lines = f.read().splitlines()

def replacenth(string, sub, wanted, n):
    pattern = re.compile(sub)
    where = [m for m in pattern.finditer(string)][n-1]
    before = string[:where.start()]
    after = string[where.end():]
    newString = before + wanted + after

    return newString

# test = '123aa456aa990aa'
# val = test.count('aa')
# for i in range(val):
#     print(replacenth(test, 'aa', 'bb', i + 1))

string = lines[-1]
data = lines[:-2]

changes = {}
for line in data:
    key = line.split(' =')[0]
    try:
        changes[key].append(line.split('> ')[1])
    except KeyError:
        changes[key] = []
        changes[key].append(line.split('> ')[1])

for change in changes:
    print(f'{change} --> {changes[change]}')

new_moc = []
for key in changes.keys():
    sub_string = key
    factor = string.count(sub_string)
    for i in range(factor):
        for item in changes[key]:
            # print(sub_string, item)
            new_string = replacenth(string, sub_string, item, i + 1)
            if new_string not in new_moc:
                new_moc.append(new_string)

# for line in new_moc:
#     print(line)
print(f'the answer = {len(new_moc)}')
