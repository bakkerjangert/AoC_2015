with open('input.txt') as f:
    lines = f.read().splitlines()

instructions = []

for line in lines:
    if 'hlf' in line:
        instructions.append(('hlf', line[-1]))
    elif 'tpl' in line:
        instructions.append(('tpl', line[-1]))
    elif 'inc' in line:
        instructions.append(('inc', line[-1]))
    elif 'jmp' in line:
        instructions.append(('jmp', int(line.split(' ')[-1])))
    elif 'jie' in line:
        instructions.append(('jie', line[4], int(line.split(' ')[-1])))
    elif 'jio' in line:
        instructions.append(('jio', line[4], int(line.split(' ')[-1])))

for line in instructions:
    print(line)

print(len(instructions))

a = 1
b = 0
i = 0

while i < len(instructions):
    instruction = instructions[i][0]
    print(f'a ==> {a}, b ==> {b}, i ==> {i}, instruction = {instructions[i]}')
    if instruction == 'hlf':
        if instructions[i][1] == 'a':
            a = a // 2
        else:
            b = b // 2
    elif instruction == 'tpl':
        if instructions[i][1] == 'a':
            a = a * 3
        else:
            b = b * 3
    elif instruction == 'inc':
        if instructions[i][1] == 'a':
            a += 1
        else:
            b += 1
    elif instruction == 'jmp':
        i += instructions[i][1]
        continue
    elif instruction == 'jie':
        if instructions[i][1] == 'a':
            if a % 2 == 0:
                i += instructions[i][2]
                continue
        else:
            if b % 2 == 0:
                i += instructions[i][2]
                continue
    elif instruction == 'jio':
        if instructions[i][1] == 'a':
            if a == 1:
                i += instructions[i][2]
                continue
        else:
            if b == 1:
                i += instructions[i][2]
                continue
    else:
        print(f'HUH, Whats happening; input not recornized')
        exit()
    i += 1



print(f'the answer is {b}')