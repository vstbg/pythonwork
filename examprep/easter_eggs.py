# Read user input
egg_count = int(input())

# Logic
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

for i in range(egg_count):
    color = input()
    if color == 'red':
        red_eggs += 1
    elif color == 'orange':
        orange_eggs += 1
    elif color == 'blue':
        blue_eggs += 1
    elif color == 'green':
        green_eggs += 1

# Print output

print(f'Red eggs: {red_eggs}')
print(f'Orange eggs: {orange_eggs}')
print(f'Blue eggs: {blue_eggs}')
print(f'Green eggs: {green_eggs}')

if red_eggs > orange_eggs and red_eggs > blue_eggs and red_eggs > green_eggs:
    print(f'Max eggs: {red_eggs} -> red')
elif orange_eggs > red_eggs and orange_eggs > blue_eggs and orange_eggs > green_eggs:
    print(f'Max eggs: {orange_eggs} -> orange')
elif blue_eggs > red_eggs and blue_eggs > orange_eggs and blue_eggs > green_eggs:
    print(f'Max eggs: {blue_eggs} -> blue')
else:
    print(f'Max eggs: {green_eggs} -> green')
