# Read user input
pens_packs = int(input())
markers_packs = int(input())
detergent_liters = int(input())
discount = int(input()) / 100

pen_price = 5.80
marker_price = 7.20
detergent_price = 1.20

# Logics
price_before_discount = (pen_price * pens_packs) + (marker_price * markers_packs) + (detergent_price * detergent_liters)
total_price = price_before_discount - price_before_discount * discount

# Print output
print(total_price)
