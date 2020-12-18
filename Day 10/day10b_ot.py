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
# puzzle = '111312111213322113'
# puzzle = '11'

for x in range(50):
    print(f'\n--- Analyzing iteration {x}')
    # print(puzzle)
    # print(puzzle)
    # Start by splitting on most common value
    if puzzle.count('1') > puzzle.count('2') and puzzle.count('1') > puzzle.count('3'):
        char = '1'
    elif puzzle.count('2') > puzzle.count('3'):
        char = '2'
    else:
        char = '3'
    puzzle_split = puzzle.split(char)

    # determine chars per split and cleanup list
    char_per_split = []

    count = 0
    series = False
    for i in range(len(puzzle_split)):
        if puzzle_split[i] == '':
            if i == 0 or i == len(puzzle_split) - 1:
                count -= 1  # Ends has exactly no of split; middle has 1 less
            count += 1
            series = True
        elif series:
            char_per_split.append(count + 1)
            count = 0
            series = False
        if not series:
            try:
                if puzzle_split[i+1] != '':
                    # print(f'split = {puzzle_split}, i = {i}')
                    char_per_split.append(1)
            except IndexError:
                pass

    # Add one more time if last entry is ''
    if series:
        char_per_split.append(count + 1)
    # print(puzzle_split)
    # print(char_per_split)

    # print(puzzle)
    # print(puzzle_split)
    puzzle_split_clean = [x for x in puzzle_split if x != '']
    # print(puzzle_split)
    # print(char_per_split)
    # print(puzzle_split_clean)
    # print(puzzle_split_clean)
    # print(char_per_split)

    # Get new solution:
    puzzle = ''
    if puzzle_split[0] == '':
        puzzle += str(char_per_split[0]) + char
        del char_per_split[0]
    for line in puzzle_split_clean:
        puzzle += look_and_say(line)
        if len(char_per_split) > 0:
            puzzle += str(char_per_split[0]) + char
            del char_per_split[0]

    # print(puzzle)

print(f'the answer = {len(puzzle)}')