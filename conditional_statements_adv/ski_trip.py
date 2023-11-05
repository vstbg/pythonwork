# Input
nights = int(input()) - 1
place_type = input()
review = input()

# Logics
price = 0

if place_type == "room for one person":
    price = 18
elif place_type == "apartment":
    price = 25

    if nights < 10:
        price *= 0.70
    elif 10 <= nights <= 15:
        price *= 0.65
    else:
        price *= 0.50

else:
    price = 35

    if nights < 10:
        price *= 0.90
    elif 10 <= nights <= 15:
        price *= 0.85
    else:
        price *= 0.80

if review == "positive":
    price *= 1.25
else:
    price *= 0.90

#Print output
print(f"{price * nights:.2f}")
