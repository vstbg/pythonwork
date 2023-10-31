# Input

x = int(input())
y = int(input())
z = int(input())

# Logic + Print Output

for i in range(2, x + 1):
    if i == 2 or i == 4 or i == 6 or i == 8:
        for j in range(2, y + 1):
            if j == 2 or j == 3 or j == 5 or j == 7:
                for k in range(2, z + 1):
                    if k == 2 or k == 4 or k == 6 or k == 8:
                        print(f'{i} {j} {k}')
