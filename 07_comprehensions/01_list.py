# List [expression for item in iterable if condition]

menu = [
    "Masala",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Tea"
]

iced_tea = ["My " + tea for tea in menu if "Iced" in tea]
print(iced_tea)

