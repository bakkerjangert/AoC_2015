with open('input.txt') as f:
    lines = f.read().splitlines()

standard = ['Al', 'B', 'Ca', 'F', 'H', 'Mg', 'N', 'O', 'P', 'Si', 'Th', 'Ti', 'e']
ends = ['Ar', 'Rn']
special_min = ['CRn']
special_plus = ['Y']

string = lines[-1]
data = lines[:-2]

counts = {'standard_count': [0, standard],
          'ends_count': [0, ends],
          'special_min_count': [0, special_min],
          'special_plus_count': [0, special_plus], }

total = 0

for item in counts.values():
    for mol in item[1]:
        item[0] += string.count(mol)
    total += item[0]

answer = 0
answer += total
answer -= counts['ends_count'][0]
answer -= 2 * counts['special_plus_count'][0]
answer -= 1

for k, v in counts.items():
    print(f'{k} --> {v[0]}')
print(f'total --> {total} molecules in the required string')
print(f'\n----\n'
      f'Every step standard adds 1 molecule. End molecules come for "free" (added with non-end molecule)\n'
      f'Molecule special_min (="CRn") is not in the required string --> no worries about that one\n'
      f'Molecule special_plus (="Y") adds yet another molecule in the step. "Y" itself comes for free, just like end molecules\n'
      f'steps = total - end_mol - 2 x special_plus and then minus 1 (starts with one molecule at step 0)\n'
      f'The answer is {answer} steps')
