# Python Udemy Project Learnings (single-reference revision sheet)

- **Environment & setup**
  - PEP8 basics (4 spaces, meaningful names) and Zen of Python (`import this`); Python is portable, readable, and “batteries included”.
  - Create/activate a virtual environment with `python3 -m venv .venv && source .venv/bin/activate`; `uv` is an alternative. Requirements: `requests==2.31.0`, `flask==3.0.0`.
  - Quick interpreter check:
    ```python
    import sys
    print(sys.version)
    # -> 3.11.x (main, ...)  [your local version]
    ```

- **Objects & classes**
  - A simple `Chai` class holds state (`sweetness`, `milk_level`) and behaviors (`sip`, `add_sugar`). Example call sequence prints:
    ```python
    class Chai:
        def __init__(self, sweetness, milk_level):
            self.sweetness = sweetness
            self.milk_level = milk_level
        def sip(self): print("Sipping Chai")
        def add_sugar(self): print("Added the sugar")
    Chai(3, 2).add_sugar(); Chai(3, 2).sip()
    # -> Added the sugar
    # -> Sipping Chai
    ```

- **Chai shop package skeleton**
  - Empty placeholders for future modules (core file, runner, utils, processing directories) ready to be filled.

- **Data types & mutability**
  - Everything is an object with identity, type, and value. Mutability: numbers are immutable; containers like sets are mutable. Reassigning an int changes `id`; mutating a set keeps its `id` while elements grow (e.g., `{'Cardamom', 'Ginger'}`).
  - Arithmetic and truthiness: sums, floor division, modulus, exponentiation, and bool coercion. Sample outputs: `Total grams of base tea is 17`, `Milk per serving is 1.75`, `While tea bags per pots is 1`, `Leftover cardamon pods 1`, `Scale flavour strength 8`, `Is there milk? False/True/False`, `Can we serve Chai? False`, and float precision details like `Differnce in temp 0.0010000000000047748` plus `sys.float_info`.
    ```python
    grams = 14 + 3; print("Total grams of base tea is", grams)          # 17
    print("Milk per serving is", 7 / 4)                                 # 1.75
    print("While tea bags per pots is", 7 // 4)                         # 1
    print("Leftover cardamon pods", 10 % 3)                             # 1
    print("Scale flavour strength", 2 ** 3)                             # 8
    print("Is there milk?", bool(0), bool(11), bool(None))              # False True False
    ```
  - Strings: slicing and stepping (`desc[:8]`, `desc[::-1]`), reversing, and UTF-8 encode/decode round-trips for labels like `"Chai Spécial"`. Outputs include `First word: Aromatic`, `Last word: Bold`, `First word skipped: Aoai`, `Reversed word: dloB dna citaromA`, and matching decoded text. Remember slicing is non-mutating because strings are immutable.
    ```python
    desc = "Aromatic and Bold"
    print(desc[:8], desc[::-1])  # Aromatic dloB dna citaromA
    label = "Chai Spécial"
    data = label.encode("utf-8"); print(data); print(data.decode("utf-8"))
    ```
  - Tuples: packing/unpacking, swapping, and membership. Outputs show `Main masala spieces: cardamom, cloves, cinnamon`, swapped ratios, and membership checks (`False` for ginger, `True` for cinnamon).
    ```python
    spice1, spice2, spice3 = ("cardamom", "cloves", "cinnamon")
    ginger, cardamom = 2, 1; ginger, cardamom = cardamom, ginger
    print("Is ginger in masala spices?", "ginger" in (spice1, spice2, spice3))
    ```
  - Lists: append/remove/extend/insert/pop/reverse/sort; operator overloading with `+` and `*`; `bytearray` for mutable bytes. Outputs include ingredient lists as they change, popped value `cardamom`, sorted lists, max/min sugar levels, repeated lists, and byte manipulations such as `bytearray(b'CINNAMON')` transforming to `bytearray(b'CARDNAMON')`. `bytearray.replace` returns a new object; reassign if you need the change.
    ```python
    chai = ["water", "milk"]; chai.extend(["ginger", "cardamom"])
    print(chai.pop())                       # cardamom
    print(["black tea"] * 3)                # ['black tea', ...]
    raw = bytearray(b"CINNAMON"); raw = raw.replace(b"CINNA", b"CARD")
    print(raw)                              # bytearray(b'CARDNAMON')
    ```
  - Sets: union, intersection, difference, membership. Outputs: combined spice sets, common elements (`{'ginger'}`), differences (`{'cinnamon', 'cardamom'}`), and membership booleans.
    ```python
    essential = {"cardamom", "ginger", "cinnamon"}
    optional = {"cloves", "ginger", "black pepper"}
    print(essential | optional)  # union
    print(essential & optional)  # {'ginger'}
    print(essential - optional)  # {'cinnamon', 'cardamom'}
    ```
  - Dictionaries: creation, updates, deletion, membership, key/value/item views, `popitem`, `update`, `get` with defaults. Fix nested f-string quotes before running to avoid syntax errors. Intended outputs show order/recipe contents, membership `True/False`, removed items, updated recipes, and default `"No Note"`.
    ```python
    order = {"type": "Masala Chai", "sugar": 2}
    print(order.get("customer_note", "No Note"))  # No Note
    ```
  - Note: choose keys that are hashable; avoid mutating dicts while iterating unless you copy items first.
  - Date/time and collections: quick `arrow.utcnow()` usage with `.shift(hours=2)` and `namedtuple` construction. Outputs include a UTC timestamp, ETA two hours ahead, and the namedtuple type `chaiProfile(flavour, aroma, color)`.

- **Conditionals**
  - Basic if/else: print `"Kettle Done! Time to make Chai!"` when a flag is true.
    ```python
    kettle_boiled = True
    if kettle_boiled:
        print("Kettle Done! Time to make Chai!")
    # -> Kettle Done! Time to make Chai!
    ```
  - Nested checks: smart thermostat prints `"High temperature alert!"` when active and hot; otherwise `"Temperature is normal"` or `"Device is offline"`.
    ```python
    device_status, temperature = "active", 48
    if device_status == "active":
        if temperature > 35: print("High temperature alert!")
        else: print("Temperature is normal")
    else:
        print("Device is offline")
    # -> High temperature alert!
    ```
  - Ternary/inputs: delivery fee calculator returns `0` when amount > 300 else `30`, after casting input to `int`.
    ```python
    order_amount = 280
    delivery_fees = 0 if order_amount > 300 else 30
    print(delivery_fees)  # 30
    ```
  - Multi-branching: cup-size chooser prints `10/15/20 rupees` for small/medium/large or `"Unknown cup size"` otherwise.
    ```python
    cup_size = "medium"
    if cup_size == "small": print("Price is 10 rupees")
    elif cup_size == "medium": print("Price is 15 rupees")
    elif cup_size == "large": print("Price is 20 rupees")
    else: print("Unknown cup size")
    # -> Price is 15 rupees
    ```
  - String normalization: snack suggestion lowers input and only accepts `samosa` or `cookies`.
    ```python
    snack = "Samosa".lower()
    if snack in ("samosa", "cookies"):
        print(f"Great Choice! We'll serve you {snack}")
    else:
        print("Sorry, we only serve cookies or samosa with tea")
    # -> Great Choice! We'll serve you samosa
    ```
  - Pattern matching: train seat selector uses `match/case` for sleeper/AC/general/luxury with a default `"Invalid seat type"`.
    ```python
    seat_type = "ac"
    match seat_type:
        case "sleeper": print("Sleeper - No AC, beds available")
        case "ac": print("AC, comfy beds available")
        case "general": print("General - Cheapest option, no reservation")
        case "luxury": print("Luxury - Premium seats with beds and meals")
        case _: print("Invalid seat type")
    # -> AC, comfy beds available
    ```
  - Note: always normalize user input (e.g., `.lower()`) before comparisons; `match` requires Python 3.10+.

- **Loops**
  - `for` over ranges/lists: token dispenser prints `"Serving chai to Token #n"` (1–10); batch prep prints `"Preparing chai for batch #n"`; order list prints `"Order ready for <name>"`; `enumerate` prints numbered menu.
    ```python
    for token in range(1, 4):
        print(f"Serving chai to Token #{token}")
    # -> Serving chai to Token #1 ... #3
    ```
  - `zip`: name/bill pairs like `"Rhea paid 50 rupees"`.
    ```python
    for name, amount in zip(["Rhea", "Meera"], [50, 70]):
        print(f"{name} paid {amount} rupees")
    # -> Rhea paid 50 rupees
    # -> Meera paid 70 rupees
    ```
  - `while`: heat until temperature reaches 100, printing each step and `"Tea is ready to be served"`.
    ```python
    temp = 40
    while temp < 100:
        print("Current temperature:", temp)
        temp += 15
    print("Current temperature:", temp)
    print("Tea is ready to be served")
    ```
  - Flow control: skip `"out of stock"`, break on `"Discontinued"`, and print remaining flavors plus `"outside of loop"`.
    ```python
    for flavor in ["ginger", "out of stock", "lemon", "Discontinued", "tulsi"]:
        if flavor == "out of stock": continue
        if flavor == "Discontinued":
            print("Discontinued item found"); break
        print("flavor:", flavor)
    print("outside of loop")
    ```
  - `for-else`: finds the first eligible staff (age ≥ 17) or prints `"No one is eligible to manage the staff"`.
    ```python
    staff = [("Minty", 16), ("Raj", 17), ("Sam", 15)]
    for name, age in staff:
        if age >= 17:
            print(f"{name} is eligible to manage the staff")
            break
    else:
        print("No one is eligible to manage the staff")
    # -> Raj is eligible to manage the staff
    ```
  - Walrus operator `:=`: reuses computed remainder, validates cup sizes and flavors in input loops until a valid choice.
  - Dictionary iteration: applies percent/fixed discounts per user; fix f-string quotes before running to see outputs like `1 paid 100 and got discount for next visit of rupees 20.0`.
    ```python
    users = [{"id": 1, "total": 100, "coupon": "P20"}]
    discounts = {"P20": (0.2, 0)}
    for user in users:
        percent, fixed = discounts.get(user["coupon"], (0, 0))
        discount = user["total"] * percent + fixed
    print(f"{user['id']} paid {user['total']} and got discount for next visit of rupees {discount}")
    # -> 1 paid 100 and got discount for next visit of rupees 20.0
    ```
  - Note: `for-else` is useful to detect “not found” cases without flags; the walrus operator reduces repetition when capturing input or calculations inline (Python 3.8+).

- **Functions**
  - DRY and decomposition: reusable order printer; report generator split into fetch/filter/summarize steps ending with `"Report is ready"`.
  - Hiding complexity: registration flow splits input, validation, persistence, ending with `"User registeration complete"`.
  - Readability: simple calculator returns cups × price; prints `My bill: 45` and `Order for table 2: 100`.
  - Traceability: VAT helper applied to a list shows original and final amounts (e.g., `Original value: 100, final with VAT: 110.0`).
  - Scope rules: local vs global vs enclosing; prints inside/outside values and demonstrates `nonlocal` (changes enclosing `chai_type` to `Kesar`) and `global` (changes global `chai_type` to `"Irani"`).
  - Parameters: positional vs keyword, `*args/**kwargs`, mutating list arguments, and safe mutable defaults. Outputs include `[1, 42, 3]`, ingredient/extras tuples/dicts, and order lists accumulating `"Ginger"`.
    ```python
    def chai_order(order=None):
        if order is None: order = []
        order.append("Ginger"); return order
    print(chai_order()); print(chai_order())  # ['Ginger'] then ['Ginger']
    ```
  - Note: default arguments are evaluated once; use `None` sentinels for mutable defaults as shown.
  - Returns: `pass` gives `None`; fixed returns; early returns; tuple packing/unpacking with sold/remaining counts; final reassignment adds a third return value.
  - Function styles: pure vs impure counters, recursion for pouring chai (counts down then returns `"All cups poured"`), and lambda with `filter` returning `['kadak', 'kadak']`.
    ```python
    def pour_chai(n):
        if n == 0: return "All cups poured"
        print("Pouring chai", n); return pour_chai(n-1)
    print(pour_chai(3))
    ```
  - Docstrings/dunders: access `__doc__` and `__name__`; `generate_bill` returns `(355, 'Thank you for visiting chaicode.com')` for `(1, 23)`.
  - Imports: notes on module/function imports and aliasing; reminder that package imports work as shown in the chai business example.

- **Chai business package demo**
  - Importing a flavor function from the package and printing its return string shows package structure works (`"Ginger chai is ready"`; another variant returns `"Elaichi chai is ready"`). Package init is empty, ready for exports.

- **Comprehensions**
  - Concept: concise creation of lists, sets, dicts, and generator expressions for filtering, transforming, or flattening data; more readable and often faster.
  - List comprehension: filter iced drinks and prefix with `"My "`; output `['My Iced Lemon Tea', 'My Iced Peach Tea']`.
  - Set comprehension: deduplicate chai names and gather unique spices; outputs sets without duplicates (order arbitrary).
  - Dict comprehension: convert prices from INR to USD-like values via division (e.g., `{'Masala Tea': 0.5, 'Green Tea': 0.625, 'Lemon Tea': 2.5}` with a divisor of 80).
  - Generator expression: sum only sales above a threshold; output `61`.
    ```python
    menu = ["Masala", "Iced Lemon Tea", "Iced Peach Tea"]
    iced = ["My " + tea for tea in menu if "Iced" in tea]
    print(iced)  # ['My Iced Lemon Tea', 'My Iced Peach Tea']
    total = sum(s for s in [5, 10, 12, 7, 3, 8, 9, 15] if s > 5)
    print(total) # 61
    ```
  - Note: prefer comprehensions for readability when the intent is a simple transform/filter; use generator expressions for large or infinite streams to save memory and avoid list materialization.

- **Generators**
  - Motivation: lazy, memory-saving iteration; key verbs are `yield`, `next`, `send`, `yield from`, `close`.
  - Basics: generator object shows as `<generator ...>`; successive `next` calls yield `"Cup 1"`, `"Cup 2"`, `"Cup 3"`, then a `StopIteration` on an extra call.
  - Infinite patterns: token-like refills produce `"Refil #1"`, `"Refil #2"`, `"Refil #3"` (and more for another consumer).
  - `send`: prime the generator with `next`, then `send` orders to see `"Preparing Masala Chai"` and `"Preparing Lemon Chai"`.
    ```python
    def chai_customer():
        print("Welcome! What chai would you like?")
        order = yield
        while True:
            print(f"Preparing {order}")
            order = yield
    stall = chai_customer(); next(stall)
    stall.send("Masala Chai"); stall.send("Lemon Chai")
    # -> Welcome!... Preparing Masala Chai ... Preparing Lemon Chai
    ```
  - `yield from`: combine multiple menus into one stream, printing local then imported teas; `close()` triggers cleanup message `"Stall closed, no more chai"` after `"Waiting for chai order"`.
  - Token dispenser app: prints start message, emits tokens, supports resets (e.g., jump to token 10), and prints `"Dispenser closed."` on shutdown.
    ```python
    def infinite_chai():
        count = 1
        while True:
            yield f"Refil #{count}"
            count += 1
    refill = infinite_chai()
    print(next(refill)); print(next(refill)); print(next(refill))  # #1 #2 #3
    ```
  - Note: always `next()` once before `send()` to reach the first `yield`; remember to `close()` long-running generators to trigger cleanup; handle `StopIteration` if you may exhaust a finite generator.

- **Decorators**
  - Basics: wrapper adds before/after behavior while `functools.wraps` keeps metadata (`__name__` stays `greet`). Output sequence: `"Before function runs"`, greeting, `"After function runs"`, then prints `greet`.
    ```python
    from functools import wraps
    def my_decorator(func):
        @wraps(func)
        def wrapper():
            print("Before function runs")
            func()
            print("After function runs")
        return wrapper
    @my_decorator
    def greet(): print("Hello from decorators class from chaicode")
    greet(); print(greet.__name__)  # greet
    ```
  - Logging decorator: wraps any function to show start/end messages. Fix nested f-string quotes inside the sample before running. Intended output: `Calling: brew_chai`, `Brewing Masala chai, without milk`, `Finished: brew_chai`.
    ```python
    from functools import wraps
    def log_activity(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Calling: {func.__name__}")
            result = func(*args, **kwargs)
            print(f"Finished: {func.__name__}")
            return result
        return wrapper
    @log_activity
    def brew_chai(chai_type, milk):
        print(f"Brewing {chai_type} chai, {'with' if milk else 'without'} milk")
    brew_chai("Masala", milk=False)
    ```
  - Auth decorator: role gate that prints `"Access denied: Admins only"` for non-admin and `"Access granted to tea inventory"` for admin.
    ```python
    from functools import wraps
    def require_admin(func):
        @wraps(func)
        def wrapper(user_role):
            if user_role != "admin":
                print("Access denied: Admins only"); return None
            return func(user_role)
        return wrapper
    @require_admin
    def access_tea_inventory(role): print("Access granted to tea inventory")
    access_tea_inventory("user"); access_tea_inventory("admin")
    ```
  - Placeholder YAML exists for decorator notes.
  - Note: `functools.wraps` is essential to preserve function metadata (name, docstring); decorators can accept `*args/**kwargs` to stay generic; prefer alternating quotes inside f-strings to avoid syntax errors.

- **Placeholders**
  - Empty/topic stubs are present for namespace notes, advanced data types, a walrus directory, chai shop processing, and utils—ready to be populated later.

Use this single document to revise: concepts, behaviors, and expected outputs are all summarized here. Fix the noted f-string quote issues before executing those samples to avoid syntax errors.
