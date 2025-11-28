is_boiling = True
# True -> 1
# False -> 0

stir_count = 5

total_actions = stir_count + is_boiling # upcasting
print(f"Total actions: {total_actions}")

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}")

milk_present = 11 # milk
print(f"Is there milk? {bool(milk_present)}")

milk_present = None # no milk
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
tea_added = False
can_serve = water_hot and tea_added
print(f"Can we serve Chai? {can_serve}")

