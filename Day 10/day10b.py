def look_and_say_rec(string):
    if string.count(string[0]) == len(string):
        partly_string = str(len(string)) + string[0]
        return partly_string
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            continue
        else:
            partly_string = str(i + 1) + string[0]
            return partly_string + look_and_say_rec(string[i + 1:])

def look_and_say(string):
    partly_string = ''
    while True:
        if string.count(string[0]) == len(string):
            partly_string += str(len(string)) + string[0]
            return partly_string
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                continue
            else:
                partly_string += str(i + 1) + string[0]
                string = string[i + 1:]
                break

puzzle = '3113322113'

for i in range(50):
    puzzle = look_and_say(puzzle)
    print(f'---Analyzing loop {i}]\ncurrent string = {puzzle}\n')

print(f'the answer = {len(puzzle)}')