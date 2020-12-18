import copy

with open('input.txt') as f:
    lines = f.read().splitlines()

def print_board(board):
    print('\n --- Printing board ---')
    for line in board:
        for char in line:
            if char == 0:
                print('.', end="")
            else:
                print('#', end="")
        print('')

board = []
for line in lines:
    board.append([])
    for char in line:
        if char == '#':
            board[-1].append(1)
        elif char == '.':
            board[-1].append(0)

print_board(board)

for time in range(100):
    next_board = copy.deepcopy(board)
    for y in range(len(board)):
        for x in range(len(board[0])):
            val = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == dy == 0:
                        continue
                    x_val = x + dx
                    y_val = y + dy
                    if x_val < 0 or y_val < 0:
                        continue
                    try:
                        val += board[y_val][x_val]
                    except IndexError:
                        pass
            # print(f'[{x}],[{y}] has {val} burning neighbours')
            if board[y][x] == 1:
                if val == 2 or val == 3:
                    pass
                else:
                    next_board[y][x] = 0
            elif board[y][x] == 0:
                if val != 3:
                    pass
                else:
                    next_board[y][x] = 1
    board = next_board

print_board(board)
answer = 0
for line in board:
    answer += sum(line)

print(f'\nThere are {answer} lights turned on')

