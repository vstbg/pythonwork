# User Input
deposit = float(input())
deposit_deadline = int(input())
yearly_percent = float(input()) / 100

# Logic
sum_deposit = deposit + deposit_deadline * ((deposit * yearly_percent) / 12)

# Print Output
print(sum_deposit)
