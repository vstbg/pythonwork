excursion_price = float(input())

puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_toys_count = puzzles_count + talking_dolls_count + teddy_bears_count + \
                   minions_count + trucks_count
total_toys_price = (puzzles_count * puzzle_price) + \
                   (talking_dolls_count * talking_doll_price) + \
                   (teddy_bears_count * teddy_bear_price) + \
                   (minions_count * minion_price) + \
                   (trucks_count * truck_price)

if total_toys_count >= 50:
    total_toys_price *= 0.75

total_toys_price *= 0.90

if total_toys_price >= excursion_price:
    print(f"Yes! {total_toys_price - excursion_price:.2f} lv left.")
else:
    print(f"Not enough money! {excursion_price - total_toys_price:.2f} lv needed.")
