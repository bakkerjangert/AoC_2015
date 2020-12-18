import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor

limit = 33100000

house = 0
count = 0
amount = {}
while True:
    house += 1
    house_sum = 0
    elfs = list(divisorGenerator(house))
    for elf in elfs:
        try:
            amount[elf] += 1
        except KeyError:
            amount[elf] = 1
        if amount[elf] <= 50:
            house_sum += elf * 11
    if house_sum > limit:
        print(f'House {house} is the first house with more than {limit} present; {house_sum}')
        exit()
    count += 1
    if count % 1000 == 0:
        print(f'House {house} has {house_sum} presents')
