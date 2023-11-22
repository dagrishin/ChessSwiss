import random
from pprint import pprint
from typing import Dict, List, Tuple

Player = str
Result = Tuple[float, str]
Match = Tuple[Player, Result]


def initialize_tournament(players: List[Player], rounds: int) -> Dict[Player, Dict[int, List[Result]]]:
    tournament = {}
    for player in players:
        tournament[player] = {round_num: [] for round_num in range(1, rounds + 1)}
    return tournament


def generate_initial_matches(players: List[Player]) -> List[Match]:
    matches = []
    random.shuffle(players)  # Перемешиваем порядок игроков
    for i in range(0, len(players) // 2):
        result = random.choice([1, 2, 3, 4])
        if result == 1:
            p1_result = (1, "w")
        elif result == 2:
            p1_result = (0, "b")
        else:
            p1_result = (0.5, "")

        match = (players[i], p1_result)
        matches.append(match)

    return matches


def play_round(tournament: Dict[Player, Dict[int, List[Result]]], round_num: int, matches: List[Match]) -> None:
    for player, match_info in matches:
        if match_info:
            p1_bal, p1_color = match_info
            tournament[player][round_num].extend([p1_bal, p1_color, "", 0, p1_bal])
        else:
            # Обработка случая, когда информации о матче нет (игрок не играет)
            tournament[player][round_num].extend([0, "", "", 0, 0])


def can_play(player1: Player, player2: Player, round_num: int, tournament: Dict[Player, Dict[int, List[Result]]]) -> \
Tuple[bool, str]:
    color_player1 = tournament[player1][round_num - 1][1] if len(tournament[player1][round_num - 1]) > 1 else ""
    color_player2 = tournament[player2][round_num - 1][1] if len(tournament[player2][round_num - 1]) > 1 else ""

    if color_player1 and color_player2:
        if color_player1[-1] != color_player2[-1]:
            color1 = color_player2[-1]
            return True, color1

    color1 = None
    if color_player1 and color_player1[-1:-3:-1] == "ww" and color_player2 and color_player2[-1:-3:-1] == "ww":
        return False, ""
    if color_player2 and color_player2[-1:-3:-1] == "bb" and color_player1 and color_player1[-1:-3:-1] == "bb":
        return False, ""
    if color_player1 and color_player1[-1:-3:-1] == "ww":
        color1 = "b"
    if color_player1 and color_player1[-1:-3:-1] == "bb":
        color1 = "w"
    if color_player2 and color_player2[-1:-4:-1] == "ww":
        color1 = "b"
    if color_player2 and color_player2[-1:-3:-1] == "bb":
        color1 = "w"
    if color1 and not color_player2:
        color_player2 = "b" if color1 == "w" else "w"

    if color1 and color_player2:
        if color1 != color_player2:
            return True, color1

    return False, ""


def add_results(tournament: Dict[Player, Dict[int, List[Result]]], matches: List[Match], round_num: int) -> None:
    for player, match_info in matches:
        if match_info:
            result = random.choice([1, 2, 3, 4])
            if result == 1:
                p1_result = (1, match_info[1])
            elif result == 2:
                p1_result = (0, match_info[1])
            else:
                p1_result = (0.5, "")

            color1 = match_info[1] + p1_result[1]
            result1 = match_info[0] + p1_result[0]

            tournament[player][round_num].extend([result1, color1, "", 0, p1_result[0]])
        else:
            # Обработка случая, когда информации о матче нет (игрок не играет)
            tournament[player][round_num].extend([0, "", "", 0, 0])


def pair_players(players: List[Player], round_num: int, tournament: Dict[Player, Dict[int, List[Result]]],
                 depth: int = 0) -> List[Match]:
    paired_players = []

    # Перемешиваем порядок игроков перед каждым раундом
    shuffled_players = random.sample(players, len(players))

    for i in range(0, len(shuffled_players) // 2, 2):
        player1 = shuffled_players[i]
        player2 = shuffled_players[i + 1]

        can_play_flag, color = can_play(player1, player2, round_num, tournament)

        if can_play_flag:
            paired_players.append((player1, (0, color)))
            paired_players.append((player2, (0, color)))
        else:
            # Если не удалось найти подходящего оппонента, вернемся на шаг 1 и перемешаем игроков заново
            if depth < 10:  # Ограничим глубину рекурсии
                return pair_players(players, round_num, tournament, depth + 1)
            else:
                print("Maximum recursion depth exceeded. Resetting pair_players.")
                return pair_players(players, round_num, tournament, depth=0)

    return paired_players


def main():
    players = [
        "player1", "player2", "player3", "player4", "player5",
        "player6", "player7", "player8", "player9", "player10",
    ]
    num_rounds = 9
    tournament_data = initialize_tournament(players, num_rounds)

    for round_num in range(1, num_rounds + 1):
        current_matches = pair_players(players, round_num, tournament_data)
        play_round(tournament_data, round_num, current_matches)

    pprint(tournament_data)


if __name__ == "__main__":
    main()
