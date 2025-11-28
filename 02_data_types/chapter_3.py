# Integer

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pots is {bags_per_pot}")

total_cardamon_pots = 10
pods_per_cup = 3
leftover_pods = total_cardamon_pots % pods_per_cup
print(f"Leftover cardamon pods {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor
print(f"Scale flavour strength {powerful_flavor}")


total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves: {total_tea_leaves_harvested}")