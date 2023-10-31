# Read user input
yearly_fee = int(input())

# Logics
shoes = yearly_fee - yearly_fee * 0.40
clothes = shoes - shoes * 0.20
ball = clothes / 4
accessories = ball / 5

total_sum = yearly_fee + shoes + clothes + ball + accessories

# Print output
print(total_sum)
