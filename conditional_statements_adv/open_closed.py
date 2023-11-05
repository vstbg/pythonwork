# Input
hour = int(input())
day = input()

# Logics + print output
if hour >=10 and hour <= 18:
    if day == "Monday" \
            or day == "Tuesday" \
            or day == "Wednesday" \
            or day == "Thursday" \
            or day == "Friday" \
            or day == "Saturday":
        print("open")
    else:
        print("closed")
else:
    print("closed")
