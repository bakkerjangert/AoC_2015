with open('input.txt') as f:
    lines = f.read().splitlines()

string = lines[0]
index_shift = 0
index_open_1 = []
index_close_1 = []
index_open_2 = []
index_close_2 = []
opened = []
closed = []
while '}' in string or ']' in string:
    index_1 = string.find('{')
    index_2 = string.find('[')
    index_3 = string.find('}')
    index_4 = string.find(']')
    lst = [index_1, index_2, index_3, index_4]
    for i in range(4):
        if lst[i] < 0:
            lst[i] = 9999999999999999999999
    if index_1 == min(lst):
        opened.append('{')
        index_open_1.append(index_1 + index_shift)
    elif index_2 == min(lst):
        opened.append('[')
        index_open_2.append(index_2 + index_shift)
    elif index_3 == min(lst):
        index_close_1.append(index_3 + index_shift)
        if opened[-1] != '{':
            print(f'Error --> trying to close [ with }}')
            exit()
        else:
            del opened[-1]
    else:
        index_close_2.append(index_4 + index_shift)
        if opened[-1] != '[':
            print(f'Error --> trying to close {{ with ]')
            exit()
        else:
            del opened[-1]
    # print(opened)
    string = string[min(lst) + 1:]
    index_shift += min(lst) + 1

string = lines[0]
print(f'[ count is {string.count("[")} --> {len(index_open_2)} == {len(index_close_2)}')
print(f'{{ count is {string.count("{")} --> {len(index_open_1)} == {len(index_close_1)}')

exit()


# print(index_open_1[0:25])
# print(index_close_1[0:25])
#
# print(len(index_open_1))
# print(len(index_close_1))

red_in = []
for i in range(len(index_open_1)):
    delete = False
    sub_string = string[index_open_1[i]:index_close_1[i] + 1]
    sub_shift = index_open_1[i]
    print(f'\n----\n'
          f'{sub_string}')
    for j in range(len(index_open_2)):
        if index_open_1[i] < index_open_2[j] < index_close_1[i]:
            start = index_open_2[j] - sub_shift
            end = index_close_2[j] - sub_shift
            chars = end - start - 1
            sub_string = sub_string[:start + 1] + 'X' * chars + sub_string[end:]
        elif index_open_2[j] > index_close_1[i]:
            break
    for j in range(len(index_open_2)):
        if index_open_1[i] < index_open_1[j] < index_close_1[i]:
            start = index_open_1[j] - sub_shift
            end = index_close_1[j] - sub_shift
            chars = end - start - 1
            sub_string = sub_string[:start + 1] + 'X' * chars + sub_string[end:]
        elif index_open_1[j] > index_close_1[i]:
            break
    print(sub_string)
    if 'red' in sub_string:
        red_in.append(True)
    else:
        red_in.append(False)

