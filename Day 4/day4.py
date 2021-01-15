import hashlib

puzzle_input = 'yzbqklnj'

counter = 0

while True:
    test = puzzle_input + str(counter)
    crypted = hashlib.md5(test.encode('utf-8')).hexdigest()
    # print(crypted[:5])
    if crypted[:5] == '00000':
        answer = counter
    if crypted[:6] == '000000':
        answer = counter
        break
    counter += 1

print('The answer to part 1 is, ', answer)
print('The answer to part 2 is, ', answer)



