# Input
steps_walked = 0
goal = 10000

# Logics
while steps_walked < goal:
    steps = input()

    if steps != "Going home":
        steps_walked += int(steps)
    else:
        steps_walked += int(input())
        break

if steps_walked >= goal:
    print("Goal reached! Good job!")
    print(f"{steps_walked - goal} steps over the goal!")
else:
    print(f"{goal - steps_walked} more steps to reach goal.")
