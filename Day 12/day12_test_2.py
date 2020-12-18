with open('input.txt') as f:
    lines = f.read().splitlines()

string = lines[0][1:-1]

index_temp_1 = []
for i in range(string.count('{')):
    index_temp_1.append(i)

index_temp_2 = []
for i in range(string.count('[')):
    index_temp_2.append(i)

index_shift = 0
index_open_1 = []
index_close_1 = []
index_open_2 = []
index_close_2 = []
opened = []
closed = []
pos_o_1 = -1
pos_o_2 = -1
pos_1 = []
pos_2 = []
change_1 = False
change_2 = False
while '}' in string or ']' in string:
    index_1 = string.find('{')
    index_2 = string.find('[')
    index_3 = string.find('}')
    index_4 = string.find(']')
    lst = [index_1, index_2, index_3, index_4]
    for i in range(4):
        if lst[i] < 0:
            lst[i] = 9999999999999999999999999
    if index_1 == min(lst):
        opened.append('{')
        index_open_1.append(index_1 + index_shift)
        pos_o_1 += 1
        # index_close_1.append(None)  # placeholder
    elif index_2 == min(lst):
        opened.append('[')
        index_open_2.append(index_2 + index_shift)
        pos_o_2 += 1
    elif index_3 == min(lst):
        index_close_1.append(index_3 + index_shift)
        pos_1.append(index_temp_1[pos_o_1])
        del index_temp_1[pos_o_1]
        # else:
        pos_o_1 -= 1
        if opened[-1] != '{':
            print(f'Error --> trying to close [ with }}')
            exit()
        else:
            del opened[-1]
    else:
        index_close_2.append(index_4 + index_shift)
        pos_2.append(index_temp_2[pos_o_2])
        del index_temp_2[pos_o_2]
        pos_o_2 -= 1
        if opened[-1] != '[':
            print(f'Error --> trying to close {{ with ]')
            exit()
        else:
            del opened[-1]
    # print(opened)
    string = string[min(lst) + 1:]
    index_shift += min(lst) + 1

new_order_1 = index_open_1.copy()
for i in range(len(pos_1)):
    new_order_1[i] = index_close_1[pos_1[i]]
new_order_2 = index_open_2.copy()
for i in range(len(pos_2)):
    new_order_2[i] = index_close_2[pos_2[i]]

string = lines[0]
print(f'[ count is {string.count("[")} --> {len(index_open_2)} == {len(index_close_2)}')
print(f'{{ count is {string.count("{")} --> {len(index_open_1)} == {len(index_close_1)}')


print(index_open_1[0:50])
print(index_close_1[0:50])
print(pos_1[0:50])
print(new_order_1[0:50])

sub_string = string[index_open_1[4]:new_order_1[4]+1]
print(sub_string)
print(sub_string.count('{'), sub_string.count('}'))

exit()


print(len(index_open_1))
print(len(index_close_1))


index_close_1 = new_order_1
index_close_2 = new_order_2

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

