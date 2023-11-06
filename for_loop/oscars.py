# Input
MAX_POINTS = 1250.5

actor = input()
points = float(input())
judges = int(input())

# Logics

for _ in range(judges):
    judges_name = input()
    judge_points = float(input())

    points += len(judges_name) * judge_points / 2

    if points > MAX_POINTS:
        print(f"Congratulations, {actor} got a nominee for leading role with {points:.1f}!")
        break
else:
    print(f"Sorry, {actor} you need {MAX_POINTS - points:.1f} more!")
