best_player = None
best_score = -1

while best_score < 10:
    player_name = input()

    if player_name == "END":
        break

    player_score = int(input())

    if player_score > best_score:
        best_player = player_name
        best_score = player_score

print(f"{best_player} is the best player!")
print(f"He has scored {best_score} goals{' and made a hat-trick !!!' if best_score >= 3 else '.'}")
