snack = input("Enter your preferred snack: ").lower()

print(f"User said: {snack}")

# if snack in ["samosa", "cookies"]:
if snack == "samosa" or snack == "cookies":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print(f"Sorry, we only serve cookies or samosa with tea")