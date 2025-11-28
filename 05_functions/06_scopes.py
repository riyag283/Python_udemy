# Scopes and Name Resolution
# local - insode a function
# Enclosing from outer function if nested
# global - top-level script
# Built-in

# Order of scope resolution: local -> enclosing -> global -> built-in

def serve_chai():
    chai_type = "Masala" # local scope
    print(f"Inside function: {chai_type}")

chai_type = "Lemon" # global scope
serve_chai()
print(f"Outside function: {chai_type}")

def chai_counter():
    chai_order = "Lemon" # Enclosing scope
    def print_order():
        chai_order = "Ginger" 
        print("Inner:", chai_order)
    print_order()
    print("Outer:", chai_order)

chai_order = "Tulsi" # global scope
print("Global:", chai_order)

