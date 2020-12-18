with open('input.txt') as f:
    lines = f.read().splitlines()

print('.'.isdigit())
string = lines[0]
total = 0
print(string[0:100])
i = 0
while i < len(string) - 1:
    if string[i] == '-' or string[i].isdigit():
        j = i
        while string[j + 1].isdigit():
            j += 1
        if i == j and string[i] == '-':
            # Single '-' found
            i += 1
            continue
        total += int(string[i:j+1])
        try:
            print(string[i:i+100])
        except IndexError:
            print(string[i:])
        print(total)
        string = string[j+1:]
        i = 0
        continue
    i += 1


print(f'the answer is {total}')