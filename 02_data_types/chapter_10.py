chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(f"Recipe: {chai_recipe}")
print(f"Recipe base: {chai_recipe["base"]}")

del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

# Membership test
print(f"Is sugar in the order? {"sugar" in chai_order}")

chai_order = dict(type="Masala Chai", size="Medium", sugar=1)
print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {
    "cardamom": "crushed",
    "ginger": "sliced"
}

chai_recipe.update(extra_spices)
print(f"Updated chai recipe: {chai_recipe}")

chai_size = chai_order["size"]
print(f"Chai size is: {chai_size}")

customer_note = chai_order.get("customer_note", "No Note")
print(f"Chai customer note is: {customer_note}")

