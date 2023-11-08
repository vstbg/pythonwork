# Input
name = input()
fails = 0
average = 0
grade = 1

# Logics
while True:
    current_input = float(input())
    if current_input < 4:
        fails += 1
        if fails >= 2:
            break
        continue
    average += current_input
    grade += 1
    if grade > 12:
        break

# Output
if fails >= 2:
    print(f'{name} has been excluded at {grade} grade')
else:
    print(f'{name} graduated. Average grade: {average / 12:.2f}')
