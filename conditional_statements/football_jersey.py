# Input
shirt_price = float(input())
sums = float(input())

# Logics
shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.20
sneakers_price = (shirt_price + shorts_price) * 2
price = (shirt_price + shorts_price + socks_price + sneakers_price) * 0.85

# Print output
if sums > price:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {sums - price:.2f} lv. more.")
else:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {price:.2f} lv.")
