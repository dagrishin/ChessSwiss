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
soper = [[[]*turs]*players]
for tur in range(turs):
    j = 1

    for i in range(len(players)):
        for j in range(i+1, len(players)):
            if players[i] != players[j] and players[j] not in soper[i][tur]:
                soper[i][tur].append(players[j])
                break
    print(soper)