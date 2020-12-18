with open('input_b.txt') as f:
    lines = f.read().splitlines()

values = {}
values['b'] = 956

def BW_and(lines, i, values=values):
    try:
        val1 = int(lines[i].split(' ')[0])
    except:
        try:
            val1 = values[lines[i].split(' ')[0]]
        except KeyError:
            # Value is no int and not calculated yet
            return None
    try:
        val2 = int(lines[i].split(' ')[2])
    except:
        try:
            val2 = values[lines[i].split(' ')[2]]
        except KeyError:
            # Value is no int and not calculated yet
            return None
    val3 = lines[i].split(' ')[-1]
    values[val3] = val1 & val2
    del lines[i]
    return None


def BW_or(lines, i, values=values):
    try:
        val1 = int(lines[i].split(' ')[0])
    except:
        try:
            val1 = values[lines[i].split(' ')[0]]
        except KeyError:
            # Value is no int and not calculated yet
            return None
    try:
        val2 = int(lines[i].split(' ')[2])
    except:
        try:
            val2 = values[lines[i].split(' ')[2]]
        except KeyError:
            # Value is no int and not calculated yet
            return None
    val3 = lines[i].split(' ')[-1]
    values[val3] = val1|val2
    del lines[i]
    return None


def BW_not(lines, i, values=values):
    try:
        val1 = int(lines[i].split(' ')[1])
    except:
        try:
            val1 = values[lines[i].split(' ')[1]]
        except KeyError:
            # Value is no int and not calculated yet
            return None
    val3 = lines[i].split(' ')[-1]
    values[val3] = ~val1
    del lines[i]
    return None


def BW_rshift(lines, i, values=values):
    try:
        val1 = int(lines[i].split(' ')[0])
    except:
        try:
            val1 = values[lines[i].split(' ')[0]]
        except KeyError:
            # Value is no int and not calculated yet
            return None
    try:
        val2 = int(lines[i].split(' ')[2])
    except:
        try:
            val2 = values[lines[i].split(' ')[2]]
        except KeyError:
            # Value is no int and not calculated yet
            return None
    val3 = lines[i].split(' ')[-1]
    values[val3] = val1 >> val2
    del lines[i]
    return None


def BW_lshift(lines, i, values=values):
    try:
        val1 = int(lines[i].split(' ')[0])
    except:
        try:
            val1 = values[lines[i].split(' ')[0]]
        except KeyError:
            # Value is no int and not calculated yet
            return None
    try:
        val2 = int(lines[i].split(' ')[2])
    except:
        try:
            val2 = values[lines[i].split(' ')[2]]
        except KeyError:
            # Value is no int and not calculated yet
            return None
    val3 = lines[i].split(' ')[-1]
    values[val3] = val1 << val2
    del lines[i]
    return None


def BW_none(lines, i, values=values):
    try:
        val1 = int(lines[i].split(' ')[0])
    except:
        try:
            val1 = values[lines[i].split(' ')[0]]
        except KeyError:
            # Value is no int and not calculated yet
            return None
    val3 = lines[i].split(' ')[-1]
    values[val3] = val1
    del lines[i]
    return None


i = 0
while len(lines) > 1:
    if i > len(lines) - 1:
        i = 0
    if 'AND' in lines[i]:
        BW_and(lines, i)
    elif 'OR' in lines[i]:
        BW_or(lines, i)
    elif 'NOT' in lines[i]:
        BW_not(lines, i)
    elif 'RSHIFT' in lines[i]:
        BW_rshift(lines, i)
    elif 'LSHIFT' in lines[i]:
        BW_lshift(lines, i)
    else:
        BW_none(lines, i)
    i += 1

print(f'The answer if {values["a"]}')

