with open('input.txt') as f:
    lines = f.read().splitlines()

true_sue = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0,
            'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

sues = {}

for line in lines:
    name = line.split(':')[0]
    sues[name] = {}
    string = line[len(name) + 2:]
    items = string.split(', ')[:]
    for i in range(len(items)):
        sues[name][items[i].split(': ')[0]] = int(items[i].split(': ')[1])


found = []
for sue in sues.keys():
    test = True
    for key in sues[sue].keys():
        try:
            if sues[sue][key] != true_sue[key]:
                test = False
                break
        except KeyError:
            continue
    if test:
        print(f'{sue} is the true Sue')
        found.append(sue)

for sue in found:
    print(f'{sues[sue]}')
