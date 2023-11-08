balance = 0

while True:
    user_input = input()
    if user_input == "NoMoreMoney":
        break
    money = float(user_input)
    if money < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {money:.2f}")
    balance += money

print(f"Total: {balance:.2f}")
