# Input

target = int(input())
sum_earnings = 0

# Logics

while target > sum_earnings:
    service = input()
    if service == "closed":
        break
    else:
        type_person = input()
    if service == "haircut":
        if type_person == "mens":
            sum_earnings += 15
        elif type_person == "ladies":
            sum_earnings += 20
        elif type_person == "kids":
            sum_earnings += 10

    elif service == "color":
        if type_person == "touch up":
            sum_earnings += 20
        elif type_person == "full color":
            sum_earnings += 30

# Print output

if sum_earnings >= target:
    print("You have reached your target for the day!")
else:
    print(f"Target not reached! You need {target - sum_earnings}lv. more.")

print(f"Earned money: {sum_earnings}lv.")
