# Input

paper = float(input()) * 5.8
cloth = float(input()) * 7.2
glue = float(input()) * 1.2
discount = float(input())

# Logics

total = (paper + cloth + glue) * (100 - discount) / 100

# Print output

print(f'{total:.3f}')
