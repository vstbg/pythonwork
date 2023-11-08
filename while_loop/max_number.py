# Input
bigger_num = int(input())

# Logics
while True:
    user_input = input()
    if user_input == "Stop":
        break
    num = int(user_input)
    if num > bigger_num:
        bigger_num = num

# Print output
print(bigger_num)
