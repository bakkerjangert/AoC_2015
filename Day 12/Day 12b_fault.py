with open('input.txt') as f:
    lines = f.read().splitlines()

string = lines[0]
# string = '[1,{"c":"red","b":2},3]'

def find_index(string, chars):
    char_1 = chars[0]
    char_2 = chars[1]
    index_shift = 0
    while string.count(char_1) > 0:
        index_start = string.find(char_1)
        sub_string = string[:index_start]
        if sub_string.count(char_2) > 0:
            # Opened and closed again
            try:
                string = string[index_start + 1:]
                index_shift += index_start + 1
            except IndexError:
                # Char 1 at last position
                return None
        else:
            # char_1 found without closing
            return index_start + index_shift
    # Not found
    return None

#
# test_string = '012345678[01]345]789080'
# print(find_index(test_string, ']['))
# print(test_string[16:])


while 'red' in string:
    red_index = string.find('red')
    part_1 = string[:red_index]
    part_2 = string[red_index:]
    try:
        end_brac = red_index + find_index(part_2, '][')
    except:
        end_brac = None
    try:
        end_curl = red_index + find_index(part_2, '}{')
    except:
        end_curl = None
    try:
        begin_brac = red_index - find_index(part_1[::-1], '[]')
    except:
        begin_brac = None
    try:
        begin_curl = red_index - find_index(part_1[::-1], '{}')
    except:
        begin_curl = None
    print('\n---')
    print(f'[] = {begin_brac}:{end_brac} and {{}} = {begin_curl}:{end_curl}')
    if begin_curl is None and end_curl is None:
        # Not in {}
        print(f'Deleting string --> {string[red_index:red_index + 3]}')
        string = string[:red_index] + string[red_index + 3:]
    elif begin_brac is None and end_brac is None:
        # In {}
        print(f'Deleting string --> {string[begin_curl:end_curl]}')
        string = string[:begin_curl] + string[end_curl:]
    elif begin_curl < begin_brac and end_curl > end_brac:
        # Not in {}
        print(f'Deleting string --> {string[red_index:red_index + 3]}')
        string = string[:red_index] + string[red_index + 3:]
    elif begin_curl > begin_brac and end_curl < end_brac:
        # In {}
        print(f'Deleting string --> {string[begin_curl:end_curl]}')
        string = string[:begin_curl] + string[end_curl:]
    else:
        print('???? Something went wrong!!!')
        exit()
    # print(string[begin_brac - 1:end_brac + 1])
    # print(string[begin_curl - 1:end_curl + 1])

print(f'Find red in string --> {string.count("red")}')
exit()

# string_org = lines[0]

start = 0

# for i in range(10):
#     end = start + 200
#     print(f'\n------\n')
#     # print(string_org[start:end])
#     print(string[start:end])
#     start += end
#
# exit()

print('.'.isdigit())
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