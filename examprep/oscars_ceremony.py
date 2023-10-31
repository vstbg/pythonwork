# Input
rent = int(input())

# Logics
prizes = rent - rent * 0.3
catering = prizes - prizes * 0.15
sound = catering / 2
total = rent + prizes + catering + sound

# Print Output
print(f'{total:.2f}')
