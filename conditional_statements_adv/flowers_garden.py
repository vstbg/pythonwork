# Input

type_flowers = input()
flowers_count = int(input())
budget = int(input())

rose_price = 5
dahlia_price = 3.80
tulip_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

total_price = 0

# Logic
if type_flowers == "Roses":
    total_price = flowers_count * rose_price

    if flowers_count > 80:
        total_price *= 0.90

elif type_flowers == "Dahlias":
    total_price = flowers_count * dahlia_price

    if flowers_count > 90:
        total_price *= 0.85

elif type_flowers == "Tulips":
    total_price = flowers_count * tulip_price

    if flowers_count > 80:
        total_price *= 0.85

elif type_flowers == "Narcissus":
    total_price = flowers_count * narcissus_price

    if flowers_count < 120:
        total_price *= 1.15

elif type_flowers == "Gladiolus":
    total_price = flowers_count * gladiolus_price

    if flowers_count < 80:
        total_price *= 1.20

# Print Output

if total_price <= budget:
    print(f"Hey, you have a great garden with {flowers_count} {type_flowers} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
