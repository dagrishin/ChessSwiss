from pprint import pprint
players = ["player1",
"player2",
"player3",
"player4",
"player5",
"player6",
"player7",
"player8",
"player9",
"player10",
]
turs = 9
# import random
# tournament = dict()
# if len(players) % 2 == 0:
#     for i in range(len(players)//2):
#         rez = random.choice([1,2,3])
#
#         tournament.setdefault('1', ).append({players[i]: players[len(players)//2+i], random.choice([1,2,3]))})
# else:
#     for i in range((len(players)-1)//2):
#         print(players[i], players[len(players)//2+i])
#
# print(tournament)
# """
# player_result={
# 1:(bal, dop_bal, color)
# tournament = {
# 1:[(pla1,pla2,rez)
# }
# """
# for j in range(2, tur):
#     pass
turnir = dict()

for player in players:
    for i in range(turs):
        turnir.setdefault(player, {})
        turnir[player].setdefault(i+1, [])

import random
number_tur = 1
if len(players) % 2 == 0:
    for i in range(len(players)//2):
        rez = random.choice([1, 2, 3, 4])
        if rez == 1:
            p1 = 1
            p2 = 0
        elif rez == 2:
            p1 = 0
            p2 = 1
        else:
            p1 = 0.5
            p2 = 0.5
        turnir[players[i]][1].extend([players[len(players)//2 + i], p1, 'w', '', 0, p1])
        turnir[players[len(players)//2 + i]][1].extend([players[i], p2, 'b', '', 0, p2])
    number_tur += 1

else:
    for i in range((len(players)-1)//2):
        rez = random.choice([1, 2, 3, 4])
        if rez == 1:
            p1 = 1
            p2 = 0
        elif rez == 2:
            p1 = 0
            p2 = 1
        else:
            p1 = 0.5
            p2 = 0.5
        turnir[players[i]][1].extend([players[len(players) // 2 + i], p1, 'w', '', 0])
        turnir[players[len(players) // 2 + i]][1].extend([players[i], p2, 'b', '', 0])
    turnir[players[len(players)-1]][1].extend([players[len(players)-1], 1, '', '', 1])
    number_tur += 1

# while number_tur <= tur:
#     for player in players:
#         if
# pprint(turnir)
# for pl in turnir.values():
#     print(pl[number_tur-1][1])

def can_play(player1, player2, tur, turnir):
    # print('---------------------------------------------------------')
    # pprint(turnir)
    # print(turnir[player2][tur - 1])
    # print(turnir[player2][tur - 1][2])
    color_player1 = turnir[player1][tur-1][2]
    color_player2 = turnir[player2][tur-1][2]

    # print(tur)
    for i in range(1, tur):
        # print(player1, turnir[player2][i][0], i)
        if player1 == turnir[player2][i][0]:
            # print(player1, turnir[player2][i][0], i)
            return False, '', ''

    # return True, 'w', 'b'

    if color_player1[-1] != color_player2[-1]:
        color1, color2 = color_player2[-1], color_player1[-1]
        return True, color1, color2

    color1 = None
    color2 = None
    print(color_player1[-1:-3:-1], color_player2[-1:-3:-1])
    if color_player1[-1:-3:-1] == 'ww' and color_player2[-1:-3:-1] == 'ww':
        return False, '', ''
    if color_player2[-1:-3:-1] == 'bb' and color_player1[-1:-3:-1] == 'bb':
        return False, '', ''
    if color_player1[-1:-3:-1] == 'ww':
        color1 = 'b'
    if color_player1[-1:-3:-1] == 'bb':
        color1 = 'w'
    if color_player2[-1:-4:-1] == 'ww':
        color2 = 'b'
    if color_player2[-1:-3:-1] == 'bb':
        color2 = 'w'
    if color1 and not color2:
        if color1 == 'w':
            color2 = 'b'
        else:
            color2 = 'w'

    if color2 and not color1:
        if color2 == 'w':
            color1 = 'b'
        else:
            color1 = 'w'

    if not color1 and not color2:
        color1 = 'b'
        color2 = 'w'
    # print(player1, color_player1[-1:-3:-1], player2, color_player2[-1:-3:-1], color1, color2)

    if color1 != color2:
        return True, color1, color2
    else:
        return False, '', ''



def add_pars(turnir1, pars, tur):

    for para in pars:
        rez = random.choice([1, 2, 3, 4])
        if rez == 1:
            p1 = 1
            p2 = 0
        elif rez == 2:
            p1 = 0
            p2 = 1
        else:
            p1 = 0.5
            p2 = 0.5
        color1 = turnir1[para[0][0]][tur-1][2] + para[0][1]
        color2 = turnir1[para[1][0]][tur-1][2] + para[1][1]
        rez = turnir1[para[0][0]][tur-1][1] + p1
        rez2 = turnir1[para[1][0]][tur-1][1] + p2
        turnir1[para[0][0]][tur].extend([para[1][0], rez, color1, '', 0, p1])
        turnir1[para[1][0]][tur].extend([para[0][0], rez2, color2, '', 0, p2])
    return turnir1



pars = []
# pprint(sorted(turnir.items(), key=lambda el: el[1][number_tur-1][1], reverse=True))
turnir = sorted(turnir.items(), key=lambda el: el[1][number_tur-1][1], reverse=True)
turnir1 = dict(turnir)
i = 0
j = 1
shag = 1
add_player = []
pprint(turnir)
step =1
for tur in range(2, turs+1):
    # print(tur)
    while len(pars) != len(players)//2:
        if j == len(players) or i == len(players):
            # if i == 10:
            #     step = 1
            print('----------'*10)
            print(add_player, step)
            # print('pars=', pars)
            add_j = add_player[len(add_player) - 2:len(add_player)]
            add_player = add_player[0:len(add_player) - 2]

            pars = pars[0:len(pars)-1]

            # print(pars, tur, shag)
            i = len(pars)

            # while turnir[i][0] in add_player:
            #     i += 1
            shag += 1

            if i == 0:
                shag = 1
                step += 1
                j = i + step
            else:
                player_name = add_j[1]
                for k, el in enumerate(turnir):
                    if player_name == el[0]:
                        j = k + 1
                        break

            # else:
            #
            #     j = i + 1
            # while turnir[j][0] in add_j or turnir[j][0] in add_player:
            #     j += 1
            # print('------------', add_j)
            # print(i, j, pars)

        if turnir[i][0] in add_player:
            i += 1
        # print(i, j)
        # if i != j:
        #     flag, color1, color2 = can_play(turnir[i][0], turnir[j][0], tur, turnir1)
        # try:
        #     if i != j:
        #         flag, color1, color2 = can_play(turnir[i][0], turnir[j][0], tur, turnir1)
        # except:
        #     # print(i,j)
        #     # print(pars, add_player)
        # print(i, j)
        if j < len(players):
            flag, color1, color2 = can_play(turnir[i][0], turnir[j][0], tur, turnir1)
            if i != j and flag and turnir[i][0] not in add_player and turnir[j][0] not in add_player:
                # print('+++++++++++++++')
                # print(turnir[i][0], turnir[j][0], add_player)
                add_player.append(turnir[i][0])
                add_player.append(turnir[j][0])
                pars.append(((turnir[i][0], color1), (turnir[j][0], color2)))
                # print(add_player, i, j, shag, tur)
                # shag = 2
                i += 1
                j = i + 1
                if i == 2:
                    shag = 1
                # shag = 1

            else:
                j += 1
        print(i, j)
        if j > len(players):
            pars = []
            # pprint(sorted(turnir.items(), key=lambda el: el[1][number_tur-1][1], reverse=True))
            turnir = sorted(turnir1.items(), key=lambda el: el[1][number_tur - 1][1])
            i = 0
            j = 1
            shag = 1
            add_player = []
            step = 1


    turnir1 = add_pars(turnir1, pars, tur)
    # pprint(turnir1)
    # print(pars)
    pars = []
    i = 0
    j = 1
    step = 1
    shag = 1
    add_player = []
    print(tur)
    turnir = sorted(turnir1.items(), key=lambda el: el[1][tur-1][1], reverse=True)
    # pprint(turnir)
    rezult = []
    for ii in turnir:
       rezult.append((ii[0],ii[1][tur-1][1]))
    pprint(sorted(rezult, key=lambda el: el[1], reverse=True))
    pprint(turnir)
    print('--'*50)

print('*'*100)
pprint(sorted(turnir1.items(), key=lambda el: el[1][tur][1], reverse=True))