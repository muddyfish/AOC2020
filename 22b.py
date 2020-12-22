from typing import Tuple, Set

with open("22.txt") as f:
    player_1, player_2 = [tuple(int(j) for j in i.split("\n")[1:]) for i in f.read().split("\n\n")]


def make_move(deck_1: Tuple[int], deck_2: Tuple[int]) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
    move_1 = deck_1[0]
    move_2 = deck_2[0]

    if move_1 > len(deck_1) - 1 or move_2 > len(deck_2) - 1:
        deck_1_winner = move_1 > move_2
    else:
        deck_1_winner = bool(play_game(deck_1[1:1+move_1], deck_2[1:1+move_2])[0])
    if deck_1_winner:
        return (
            deck_1[1:] + (move_1, move_2),
            deck_2[1:]
        )
    else:
        return (
            deck_1[1:],
            deck_2[1:] + (move_2, move_1)
        )


def is_recursive(prev_moves: Set, deck_1: Tuple[int, ...], deck_2: Tuple[int, ...]) -> bool:
    rtn = (deck_1, deck_2) in prev_moves
    prev_moves.add((deck_1, deck_2))
    return rtn


def play_game(deck_1: Tuple[int, ...], deck_2: Tuple[int, ...]) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
    prev_moves = set()
    while deck_1 and deck_2:
        if is_recursive(prev_moves, deck_1, deck_2):
            return deck_1, ()
        deck_1, deck_2 = make_move(deck_1, deck_2)
    return deck_1, deck_2


player_1, player_2 = play_game(player_1, player_2)
winner_deck = player_1 or player_2

print("Score:", sum(map(lambda i: i[0]*i[1], enumerate(reversed(winner_deck), 1))))
