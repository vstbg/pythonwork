# Input
min_num = int(input())

# Logics
while True:
    user_input = input()
    if user_input == "Stop":
        break
    current_num = int(user_input)
    if current_num < min_num:
        min_num = current_num

# Output
print(min_num)
