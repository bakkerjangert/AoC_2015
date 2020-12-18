letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

triples = []

for i in range(len(letters) - 2):
    triples.append(letters[i] + letters[i+1] + letters[i+2])

not_in = ('i', 'o', 'l')

def doubles(string):
    count = 0
    i = 0
    while i < len(string) - 1:
        if string[i] == string[i + 1]:
            count += 1
            i += 2  # Skip pair
            if count == 2:
                return True
            continue
        i += 1
    return False

def increment(string, letters=letters, not_in=not_in):
    if string[-1] == 'z':
        return increment(string[:-1]) + 'a'
    val = letters.index(string[-1]) + 1
    if letters[val] in not_in:
        val += 1
    return string[:-1] + letters[val]

string = 'hxbxxyzz'

# First get rid of not_in:

for i in range(len(string)):
    if string[i] in not_in:
        val = letters.index[string[i]] + 1
        string = string[:i] + letters[val] + string[i+1:]

count = 0
while True:
    test1 = False
    test2 = False
    string = increment(string)
    for line in triples:
        if line in string:
            test1 = True
            break
    test2 = doubles(string)
    if test1 and test2 and count == 1:
        print(f'the next password = {string}')
        count += 1
        break
    if test1 and test2 and count == 0:
        print(f'the next password = {string}')
        count += 1
    string = increment(string)


