limit = 33100000

house = 0
count = 0

while True:
    house += 1
    house_sum = 0
    i = 0
    while i < house:
        elf = i + 1
        if house % elf == 0:
            house_sum += elf * 10
        i += 1
    if house_sum > limit:
        print(f'House {house} is the first house with more than {limit} present; {house_sum}')
        exit()
    count += 1
    # if count % 1000:
    print(f'House {house} has {house_sum} presents')
    if house > 50:
        exit()