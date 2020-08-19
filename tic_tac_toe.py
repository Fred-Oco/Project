import random

play_list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
convert_dict = {
    0: ' ',
    1: 'X',
    -1: 'O'
}
result = False
win = False
peace = False
peace_count = 0

def convert_xy(opt):
    if opt <= 3:
        y = 0
    elif opt <= 6:
        y = 1
    else:
        y = 2
    x = opt - (3 * y) - 1
    return (x, y)


while result is False:
    for y in range(3):
        print('\n-------')
        print('|', end='')
        for x in range(3):
            convert = convert_dict[play_list[y][x]]
            print(convert + '|', end='')
    print('\n-------')
    player_opt = int(input('which room you choose?(1-9): '))
    x, y = convert_xy(player_opt)
    if play_list[y][x] != 0:
        print('Input not valid', end='')
        continue
    play_list[y][x] = -1
    dia_total = 0
    for r in range(3):
        if 0 not in play_list[r]:
            peace_count += 1
            if peace_count == 3:
                result = True
                peace = True
                break
        dia_total = dia_total + play_list[r][r]
        if dia_total == 3:
            result = True
            break
        elif dia_total == -3:
            win = True
            result = True
            break
        t_sum = 0
        if sum(play_list[r]) == 3:
            result = True
            break
        elif sum(play_list[r]) == -3:
            win = True
            result = True
            break
        for j in range(3):
            t_sum = t_sum + play_list[j][r]
            if t_sum == 3:
                result = True
                break
            elif t_sum == -3:
                win = True
                result = True
                break
    if (play_list[0][2] + play_list[1][1] + play_list[2][0]) == 3:
        result = True
    elif (play_list[0][2] + play_list[1][1] + play_list[2][0]) == -3:
        win = True
        result = True
    if result is False:
        duplicate = True
        while duplicate is True:
            computer_opt = random.randint(1, 9)
            com_x, com_y = convert_xy(computer_opt)
            if play_list[com_y][com_x] != 1 and play_list[com_y][com_x] != -1:
                play_list[com_y][com_x] = 1
                duplicate = False

for y in range(3):
    print('\n-------')
    print('|', end='')
    for x in range(3):
        convert = convert_dict[play_list[y][x]]
        print(convert + '|', end='')
print('\n-------')

if peace is False:
    if win is True:
        print('You win')
    else:
        print('You lose')
else:
    print('Peace')
