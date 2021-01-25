letters = 'abcdefghijklmnopqrstuvwxyz'
next_letter = 'abcdefghjkmnpqrstuvwxyza'  # Exclude i, o, l; end wih 'a' to find next letter easily by index + 1


def get_new_password(old_password):
    reversed_old_password = old_password[::-1]
    for i in range(len(reversed_old_password)):
        if reversed_old_password[i] == 'z':
            continue
        else:
            next_letter_index = letters.index(reversed_old_password[i]) + 1
            reversed_new_password = 'a' * i + letters[next_letter_index] + reversed_old_password[i + 1:]
            return reversed_new_password[::-1]
    return 'a' * len(old_password)


def three_successive_letters(string):
    for i in range(len(letters) - 2):
        if letters[i: i + 3] in string:
            return True
    return False


def two_pairs(string):
    i = 0
    count = 0
    while i < len(string) - 1:
        if string[i] == string[i + 1]:
            count += 1
            if count == 2:
                return True
            i += 2  # skip next entry because of overlap
        else:
            i += 1
    return False


def check_password(string):
    if not three_successive_letters(string):
        return False
    if not two_pairs(string):
        return False
    return True

# Part 1 & 2: find next password that meets certain requirements
# Approach:
# Brute force every password by adding a letter at the end; ommit o, i, l when generating new passwords
# Then only two conditions are required; double pair of letters and three successive letters

current_password = 'hxbxwxba'

while not check_password(current_password):
    current_password = get_new_password(current_password)

print(f'Part 1: The next password = {current_password}')

current_password = get_new_password(current_password)
while not check_password(current_password):
    current_password = get_new_password(current_password)

print(f'Part 2: The second next password = {current_password}')