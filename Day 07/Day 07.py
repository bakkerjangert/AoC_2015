with open('input.txt') as f:
    lines = f.read().splitlines()

def BW_AND(values):
    return values[0] & values[1]
def BW_OR(values):
    return values[0] | values[1]
def BW_XOR(values):
    return values[0] ^ values[1]
def BW_NOT(values):
    return ~values[0]
def BW_LSHIFT(values):
    return values[0] << values[1]
def BW_RSHIFT(values):
    return values[0] >> values[1]


def solve_dict(instructions, unsolved_entries):
    while len(unsolved_entries) > 0:
        for unsolved_entry in unsolved_entries.copy():
            inputs = instructions[unsolved_entry][1]
            if (inputs[0].isdigit() or type(instructions[inputs[0]]) == int) and \
                    (inputs[-1].isdigit() or type(instructions[inputs[-1]]) == int):
                values = []
                for input in inputs:
                    if input.isdigit():
                        values.append(int(input))
                    else:
                        values.append(instructions[input])
                operator = instructions[unsolved_entry][0]
                instructions[unsolved_entry] = BW_operations[operator](values)
                unsolved_entries.remove(unsolved_entry)
    return instructions['lx']


# Part 1 & 2: Find signal on wire a by implementing different bitwise operations
# Make dict with instructions; output signal as key; input as value
# --> value is either an int or tuple(BW_operater, (BW input 1, BW input 2))
# Keep track of solved entries in the dict (a.k.a. --> if dict value is an INT the signal is solved) with a list
# Loop over unsolved list --> if entry can be solved, solve it, update dict and delete from list
# For part 2 --> Just reload original instructions and unsolved list, update dict and repeat solver

# Note --> one Weird input line --> "lx --> a"
# --> This is not in line other inputs; delete entry 'a' and search for 'lx' instead

BW_operations = {'AND': BW_AND, 'OR': BW_OR, 'XOR': BW_XOR,
                 'NOT': BW_NOT, 'LSHIFT': BW_LSHIFT, 'RSHIFT': BW_RSHIFT}

instructions = dict()
unsolved_entries = []

for line in lines:
    key = line.split(' -> ')[1]
    if line.split(' -> ')[0].isdigit():
        val = int(line.split(' -> ')[0])
    else:
        mode = ''.join(c for c in line if c.isupper())
        sub_line = line.replace(mode + ' ', '')
        values = sub_line.split(' -> ')[0].split(' ')
        val = (mode, values)
        unsolved_entries.append(key)
    instructions[key] = val

# Weird input line --> "lx --> a". This is not in line other inputs; delete entry 'a' and search for 'lx' instead
del instructions['a']
unsolved_entries.remove('a')

# Solve part 1
value_wire_a = solve_dict(instructions.copy(), unsolved_entries.copy())
print(f'The answer to part 1 = {value_wire_a}')

# Update instructions and solve again for part 2
instructions['b'] = value_wire_a
value_wire_a_p2 = solve_dict(instructions.copy(), unsolved_entries.copy())
print(f'The answer to part 2 = {value_wire_a_p2}')
