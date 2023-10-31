import math

days = int(input())
kilometers = float(input())
total_kilometers = kilometers

for i in range(days):
    percentage = float(input())
    kilometers *= (100 + percentage) / 100
    total_kilometers += kilometers

if total_kilometers < 1000:
    print(f"Sorry Mrs. Ivanova, you need to run {1000 - math.floor(total_kilometers)} more kilometers")
else:
    print(f"You've done a great job running {math.ceil(total_kilometers) - 1000} more kilometers!")
