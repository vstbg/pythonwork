# Input
degrees = int(input())
time_of_day = input()

outfit = None
shoes = None

# Logics
if 10 <= degrees <= 18:
    if time_of_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_day == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"

elif 18 < degrees <= 24:
    if time_of_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_of_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"

else:
    if time_of_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_of_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"

# Print output
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
