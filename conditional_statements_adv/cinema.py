# Input
type_movie = input()
rows = int(input())
columns = int(input())

# Logics
income = 0
cinema_capacity = rows * columns

if type_movie == "Premiere":
    income = cinema_capacity * 12
elif type_movie == "Normal":
    income = cinema_capacity * 7.50
elif type_movie == "Discount":
    income = cinema_capacity * 5

# Output
print(f"{income:.2f} leva")
