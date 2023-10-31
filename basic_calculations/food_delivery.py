# Read user input
chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

chicken_menus_price = 10.35
fish_menus_price = 12.40
vegetarian_menus_price = 8.15
delivery = 2.50

# Logics
menus_price = \
    (chicken_menus * chicken_menus_price) + \
    (fish_menus * fish_menus_price) + \
    (vegetarian_menus * vegetarian_menus_price)
dessert_price = menus_price * 0.20

total_price = menus_price + dessert_price + delivery

# Print output
print(total_price)
