import operator
with open('input.txt') as f:
    lines = f.read().splitlines()

class Contestent(object):
    def __init__(self, name, speed, flying_time, resting_time):
        self.name = name
        self.speed = speed  # km/s
        self.flying_time = flying_time  # s
        self.resting_time = resting_time  # s
        self.time = 0  # s
        self.distance = 0  # km
        self.score = 0  # int
        self.mode = 'Flying'

    def move_one_second(self):
        if self.mode == 'Flying':
            self.distance += self.speed
        self.time += 1
        if self.time % (self.flying_time + self.resting_time) == 0:
            self.mode = 'Flying'
        elif self.time % (self.flying_time + self.resting_time) == self.flying_time:
            self.mode = 'Resting'

# Part 1 & 2: Determine the winner of reindier racers after a certain amount of time
# Approach:
# Use a class to keep track of contesters; update the score and distance per second
# Toggle 'Flying' or 'Resting' mode base on % operator of total time
# Use operater tool to sort the list of contestors on distance or score

goal = 2503  # seconds
contestents = []

for line in lines:
    current_contestent = Contestent(line.split()[0], int(line.split()[3]), int(line.split()[6]), int(line.split()[13]))
    contestents.append(current_contestent)

for time in range(goal):
    # Move every constestent foward 1 second
    for contestent in contestents:
        contestent.move_one_second()
    # Award points for contents in the lead (there might be more than 1 in lead)
    contestents.sort(key=operator.attrgetter('distance'), reverse=True)
    current_max_distance = contestents[0].distance
    for contestent in contestents:
        if contestent.distance == current_max_distance:
            contestent.score += 1
        else:
            break

# Part 1: Winner is the reindier with maxmimum travel distance
contestents.sort(key=operator.attrgetter('distance'), reverse=True)
print(f'Part 1: The winner is {contestents[0].name} with {contestents[0].distance} km traveled')

# Part 2: Winner is the reindier with maximum score
contestents.sort(key=operator.attrgetter('score'), reverse=True)
print(f'Part 2: The winner is {contestents[0].name} with a score of {contestents[0].score}')
