# Input
budget = float(input())
season = input()

price = 0
destination = None
place = None

# Logics
if budget <= 100:
    destination = "Bulgaria"

    if season == "summer":
        place = "Camp"
        price = budget * 0.30
    else:
        place = "Hotel"
        price = budget * 0.70

elif budget <= 1000:
    destination = "Balkans"

    if season == "summer":
        place = "Camp"
        price = budget * 0.40
    else:
        place = "Hotel"
        price = budget * 0.80

else:
    destination = "Europe"
    place = "Hotel"
    price = budget * 0.90

# Print output
print(f"Somewhere in {destination}")
print(f"{place} - {price:.2f}")
