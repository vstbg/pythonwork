# Input
day = input()
price = 0

# Logics
if day == "Monday" or day == "Tuesday" or day == "Friday":
    price = 12
elif day == "Wednesday" or day == "Thursday":
    price = 14
elif day == "Saturday" or day == "Sunday":
    price = 16

# Print output
print(price)
