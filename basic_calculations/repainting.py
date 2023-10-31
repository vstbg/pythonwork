# Read user input
nylon = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())

nylon_price = 1.50
paint_price = 14.50
thinner_price = 5
bags_price = 0.40

nylon += 2
paint += paint * 0.10

# Logics
materials_price = (nylon * nylon_price) + (paint * paint_price) + (thinner * thinner_price) + (bags_price * 1)
price_for_one_hour_of_work = materials_price * 0.30
total_price = materials_price + (price_for_one_hour_of_work * work_hours)

# Print output
print(total_price)
