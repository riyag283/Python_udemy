chai_type = "Ginger"

def update_order():
    chai_type = "Elaichi"
    def kitchen():
        # nonlocal (just above the fn) -> from inside to inside function - just targetting outside the function
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update:", chai_type)

update_order()
print("Global chai type:", chai_type)