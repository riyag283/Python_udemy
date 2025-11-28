sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")


# numbers 2 and 12 are immutable
# what changed was the reference
# variable sugar_amoount was first pointing to 2;
# now it is pointing to 12
sugar_amount = 12
print(f"Second init sugar: {sugar_amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")
print(f"ID of sugar_amount: {id(sugar_amount)}")