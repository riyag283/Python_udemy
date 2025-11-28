# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing", order)

# prepare_chai(chai)

chai = [1, 2, 3]
def edit_chai(cup):
    cup[1] = 42

edit_chai(chai) 
print(chai) # list is mutable

# args -> position agruments
# *kwargs -> keyword args

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") # positional
make_chai(tea="Green", sugar="Medium", milk="No") # keyword-based

def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients) # tuple of all values we have
    print("Extras", extras) # dictionary of keyword-based

special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam=True)

# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

# # Default traps
# chai_order()
# chai_order()

def chai_order(order=None):
    if order is None:
        order = []
    order.append("Ginger")
    print(order)
chai_order()
chai_order()