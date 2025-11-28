staff = [
    ("Minty", 16),
    ("Raj", 17),
    ("Sam", 15)
]

for name, age in staff:
    if age >= 17:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff")