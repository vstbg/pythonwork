# Read user input
destination = input()
dates = input()
overnights = int(input())

total = 0
# Logic

if destination == 'France':
    if dates == '21-23':
        total = 30 * overnights
    elif dates == '24-27':
        total = 35 * overnights
    elif dates == '28-31':
        total = 40 * overnights
elif destination == 'Italy':
    if dates == '21-23':
        total = 28 * overnights
    elif dates == '24-27':
        total = 32 * overnights
    elif dates == '28-31':
        total = 39 * overnights
elif destination == 'Germany':
    if dates == '21-23':
        total = 32 * overnights
    elif dates == '24-27':
        total = 37 * overnights
    elif dates == '28-31':
        total = 43 * overnights


# Print output
print(f"Easter trip to {destination} : {total:.2f} leva.")
