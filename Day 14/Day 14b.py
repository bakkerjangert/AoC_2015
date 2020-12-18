with open('input.txt') as f:
    lines = f.read().splitlines()

data = []
for line in lines:
    data1 = int(line.split()[3])
    data2 = int(line.split()[6])
    data3 = int(line.split()[-2])
    data.append((data1, data2, data3))

time = 2503
score = []

for i in range(len(lines)):
    score.append(0)

distance = score.copy()

for i in range(time):
    for j in range(len(data)):
        if i % (data[j][1] + data[j][2]) < data[j][1]:
            distance[j] += data[j][0]
    max_dist = max(distance)
    for k in range(len(distance)):
        if distance[k] == max_dist:
            score[k] += 1

print(f'The answer is {max(score)}')