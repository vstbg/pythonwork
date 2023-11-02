# Input
tourists = int(input())
season = input()
price = 0

# Logics
if season == 'spring':
    if tourists <= 5:
        price = 50
    else:
        price = 48
elif season == 'summer':
    if tourists <= 5:
        price = 48.50
    else:
        price = 45

elif season == 'autumn':
    if tourists <= 5:
        price = 60
    else:
        price = 49.50

elif season == 'winter':
    if tourists <= 5:
        price = 86
    else:
        price = 85

if season == 'summer':
    price *= 0.85
elif season == 'winter':
    price *= 1.08

sums = price * tourists

# Print Output
print(f'{sums:.2f} leva.')
