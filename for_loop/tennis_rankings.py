# Input
from math import floor

tournaments = int(input())
starting_points = int(input())

win_tournaments = 0
gained_points = 0

# Logics
for _ in range(tournaments):
    tournament = input()

    if tournament == "W":
        gained_points += 2000
        win_tournaments += 1
    elif tournament == "F":
        gained_points += 1200
    elif tournament == "SF":
        gained_points += 720

# Print output
print(f"Final points: {starting_points + gained_points}")
print(f"Average points: {floor(gained_points / tournaments)}")
print(f"{win_tournaments / tournaments * 100:.2f}%")
