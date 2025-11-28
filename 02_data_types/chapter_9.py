essential_spices = {"cardamom", "ginger", "cinnamon"}
optionl_spices = {"cloves", "ginger", "black pepper"}

# union
all_spices = essential_spices | optionl_spices
print(f"All spices: {all_spices}")

# intersection
common_spices = essential_spices & optionl_spices
print(f"Common spices: {common_spices}")

# differences
only_essentials = essential_spices - optionl_spices
print(f"Only in essentials: {only_essentials}")

# Membership test
print(f"Is 'cloves' in essential spices? {'cloves' in essential_spices}")
print(f"Is 'cloves' in optional spices? {'cloves' in optionl_spices}")
