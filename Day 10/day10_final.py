sequence = '3113322113' + '_'

# Part 1 & 2: find the length of the sequence after 40 and 50 steps
# Approach:
# At the start of each step start by initializing a new sequence ''
# Loop over current sequnce and keep track amount of repeated numbers
# If next number != previous number add the amount of numbers to the new sequence and then the previous number
# Rinse and repeat
# Note: To make the code cleaner for the last number, a non-digit character is added at the end of the aequence
# by doing this the last number will always be accounted for in the next sequence while the character is skipped

for step in range(50):
    next_sequence = ''
    current_number = sequence[0]
    number_count = 0
    for number in sequence:
        if number == current_number:
            number_count += 1
        else:
            next_sequence += str(number_count) + current_number
            current_number = number
            number_count = 1
    if step == 39:
        print(f'Part 1: The length after 40 steps = {len(next_sequence)}')
    if step == 49:
        print(f'Part 2: The length after 50 steps = {len(next_sequence)}')
    # print(next_sequence)
    sequence = next_sequence + '_'
