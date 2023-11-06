from sys import maxsize

max_diff = -maxsize
last_sum = -maxsize


for index in range(int(input())):
    num1 = int(input())
    num2 = int(input())

    current_pairs_sum = num1 + num2

    if index == 0:
        last_sum = current_pairs_sum
        continue

    if last_sum != current_pairs_sum:
        if abs(current_pairs_sum - last_sum) > max_diff:
            max_diff = abs(current_pairs_sum - last_sum)

        last_sum = current_pairs_sum

if max_diff == -maxsize:
    print(f"Yes, value={last_sum}")
else:
    print(f"No, maxdiff={max_diff}")
