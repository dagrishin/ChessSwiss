from typing import List, Dict, Tuple
import random

PLAYERS = List[int]
PAIRED_PLAYERS = Tuple[int, int]
PLAYER_DATA = List[Tuple[int, str, int]]
STANDINGS = Dict[int, PLAYER_DATA]
PAIRINGS = List[PAIRED_PLAYERS]


def group_by_points(standings: STANDINGS) -> Dict[int, PLAYERS]:
    groups: Dict[int, PLAYERS] = dict()

    for player, games in standings.items():
        score = len(games)
        if score not in groups:
            groups[score] = []
        groups[score].append(player)

    return groups


def generate_pairings(players: PLAYERS, standings: STANDINGS, prev_pairings: PAIRINGS) -> PAIRINGS:
    point_groups = group_by_points(standings)

    pairings: PAIRINGS = []

    for score in point_groups:
        group = point_groups[score]
        random.shuffle(group)

        for i in range(0, len(group), 2):
            white = group[i]
            black = group[i + 1]

            if (white, black) in prev_pairings:
                raise ValueError("Повторная пара")

            pairings.append((white, black))

    return pairings


def play_round(standings: STANDINGS, pairings: PAIRINGS, colors: List[str], round_num: int) -> None:
    white_idx = 0
    for white, black in pairings:
        result = random.choice([(1, 0), (0, 1), (0.5, 0.5)])

        standings[white].append((round_num, colors[white_idx], result[0]))
        standings[black].append((round_num, colors[1 - white_idx], result[1]))

        white_idx = 1 - white_idx


def print_standings(standings: STANDINGS) -> None:
    for player in players:
        score = sum(game[2] for game in standings[player])
        print(f"{player}: {score} очков")


if __name__ == "__main__":

    NUM_ROUNDS = 5
    NUM_PLAYERS = 8
    players = list(range(1, NUM_PLAYERS + 1))
    colors = ["white", "black"]

    standings: STANDINGS = {player: [] for player in players}
    prev_pairings: PAIRINGS = []

    for round_num in range(1, NUM_ROUNDS + 1):
        pairings = generate_pairings(players, standings, prev_pairings)
        play_round(standings, pairings, colors, round_num)
        prev_pairings = pairings

    print_standings(standings)