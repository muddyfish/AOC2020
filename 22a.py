def make_move(deck_1, deck_2):
    move_1 = deck_1.pop(0)
    move_2 = deck_2.pop(0)
    if move_1 > move_2:
        deck_1.append(move_1)
        deck_1.append(move_2)
    else:
        deck_2.append(move_2)
        deck_2.append(move_1)


with open("22.txt") as f:
    player_1, player_2 = [[int(j) for j in i.split("\n")[1:]] for i in f.read().split("\n\n")]


while player_1 and player_2:
    make_move(player_1, player_2)

winner = player_1 or player_2

print("Score:", sum(map(lambda i: i[0]*i[1], enumerate(reversed(winner), 1))))
