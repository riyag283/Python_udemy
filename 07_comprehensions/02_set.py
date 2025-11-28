# Set {expression for item in iterable if condition}

favorite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Chai",
    "Green Tea",
    "Elaichi Chai"
]

unique_chai = {chai for chai in favorite_chais if "Chai" in chai}
print(unique_chai)

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["elaichi", "cardamom", "milk"],
    "Masala Chai": ["ginger", "black pepper", "clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)

