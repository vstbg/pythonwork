# Read user input
product = input()
city = input()
quantity = float(input())
total = 0

# Logics
if city == "Sofia":
    if product == "coffee":
        total = quantity * 0.50
    elif product == "water":
        total = quantity * 0.80
    elif product == "beer":
        total = quantity * 1.20
    elif product == "sweets":
        total = quantity * 1.45
    else:
        total = quantity * 1.60
elif city == "Plovdiv":
    if product == "coffee":
        total = quantity * 0.40
    elif product == "water":
        total = quantity * 0.70
    elif product == "beer":
        total = quantity * 1.15
    elif product == "sweets":
        total = quantity * 1.30
    else:
        total = quantity * 1.50
else:
    if product == "coffee":
        total = quantity * 0.45
    elif product == "water":
        total = quantity * 0.70
    elif product == "beer":
        total = quantity * 1.10
    elif product == "sweets":
        total = quantity * 1.35
    else:
        total = quantity * 1.55

# Print output
print(total)
