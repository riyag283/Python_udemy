flavors = ["ginger", "out of stock", "lemon", "Discontinued", "tulsi"]

for flavor in flavors:
    if flavor == "out of stock":
        continue
    if flavor == "Discontinued":
        print("Discontinued item found")
        break
    print(f"flavor: {flavor}")

print(f"outside of loop")