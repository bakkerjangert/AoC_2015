with open('input.txt') as f:
    lines = f.read().splitlines()


def find_sub(string):
    # Returns end index of ']' or '}'
    string_org = string
    begin = string[0]
    if begin == '{':
        end = '}'
    elif begin == '[':
        end = ']'
    else:
        print('String does not start correct; check code!')
        exit()
    count = 1
    shift = 0
    while count > 0:
        string = string[1:]
        shift += 1
        index_1 = string.find(begin)
        index_2 = string.find(end)
        if index_1 == -1:
            index_1 = 2 * len(string)
        if index_2 == -1:
            index_2 = 2 * len(string)
        if index_1 < index_2:
            # Open a [] or {}
            count += 1
            string = string[index_1:]
            shift += index_1
        elif index_2 < index_1:
            # close another [] or {}
            count -= 1
            string = string[index_2:]
            shift += index_2
        else:
            print(f'Hey, something went wrong --> Check your code!')
            exit()
    return shift



string = lines[0]
list_curl = []
list_brac = []
shift = 0
while '{' in string or '[' in string:
    index_1 = string.find('{')
    index_2 = string.find('[')
    if (index_1 < index_2 and index_1 != -1) or (index_2 == -1 and index_1 != -1):
        shift += index_1
        string = string[index_1:]
        end = shift + find_sub(string)
        list_curl.append((shift, end))
        # print('\n---')
        # print(lines[0][shift:end + 1])
    else:
        shift += index_2
        string = string[index_2:]
        end = shift + find_sub(string)
        list_brac.append((shift, end))
        # print('\n---')
        # print(lines[0][shift:end + 1])
    string = string[1:]
    shift += 1

string = lines[0]
print(f'[] --> {string.count("[")} == {len(list_brac)}')
print(f'{{}} --> {string.count("{")} == {len(list_curl)}')

curl_true = []

for i in range(len(list_curl)):
    start = list_curl[i][0]
    end = list_curl[i][1]
    sub_string = string[start:end + 1]
    print('\n-----')
    print(sub_string)
    for j in range(len(list_curl)):
        sub_start = list_curl[j][0]
        sub_end = list_curl[j][1]
        if start < sub_start < end:
            chars = sub_end - sub_start - 1
            sub_string = sub_string[:sub_start - start + 1] + 'X' * chars + sub_string[sub_end - start:]
        elif sub_start > end:
            break
    for k in range(len(list_brac)):
        sub_start = list_brac[k][0]
        sub_end = list_brac[k][1]
        if start < sub_start < end:
            chars = sub_end - sub_start - 1
            sub_string = sub_string[:sub_start - start + 1] + 'X' * chars + sub_string[sub_end - start:]
        elif sub_start > end:
            break
    print(sub_string)
    if '"red"' in sub_string:
        curl_true.append(True)
    else:
        curl_true.append(False)

string = lines[0]
for i in range(len(curl_true)):
    if curl_true[i]:
        begin = list_curl[i][0]
        end = list_curl[i][1]
        chars = end - begin - 1
        string = string[:begin + 1] + 'X' * chars + string[end:]
print(string)

total = 0
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
