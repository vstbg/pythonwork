# Input
years = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_given = 10
money_from_gifts = 0
toys_count = 0

# Logics
for age in range(1, years + 1):
    if age % 2 == 0:
        money_from_gifts += money_given - 1
        money_given += 10
    else:
        toys_count += 1

money_from_gifts += toys_count * toy_price

if money_from_gifts >= washing_machine_price:
    print(f"Yes! {money_from_gifts - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - money_from_gifts:.2f}")
