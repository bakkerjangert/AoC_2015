# Advent of Code 2015 - Day 1 part a

with open('input.txt') as f:
    lines = f.read().splitlines()

start = 0

up = lines[0].count('(')
down = lines[0].count(')')

print('The answer is', start + up - down)

counter = 0
level = 0
for char in lines[0]:
    counter += 1
    if char == '(':
        level += 1
    else:
        level -= 1
    if level == -1:
        print('The answer is', counter)
        break

