# Python Udemy Project Learnings (single-reference revision sheet)

- **Environment & setup**
  - PEP8 basics (4 spaces, meaningful names) and Zen of Python (`import this`); Python is portable, readable, and “batteries included”.
  - Create/activate a virtual environment with `python3 -m venv .venv && source .venv/bin/activate`; `uv` is an alternative. Requirements: `requests==2.31.0`, `flask==3.0.0`.
  - Quick interpreter check:
    ```python
    import sys; print(sys.version)
    ```
    Output: your local Python version string (e.g., `3.11.x (main, ...)`).

- **Objects & classes**
  - A simple `Chai` class holds state (`sweetness`, `milk_level`) and behaviors (`sip`, `add_sugar`). Example call sequence prints:
    ```
    Added the sugar
    Sipping Chai
    ```

- **Chai shop package skeleton**
  - Empty placeholders for future modules (core file, runner, utils, processing directories) ready to be filled.

- **Data types & mutability**
  - Everything is an object with identity, type, and value. Mutability: numbers are immutable; containers like sets are mutable. Reassigning an int changes `id`; mutating a set keeps its `id` while elements grow (e.g., `{'Cardamom', 'Ginger'}`).
  - Arithmetic and truthiness: sums, floor division, modulus, exponentiation, and bool coercion. Sample outputs: `Total grams of base tea is 17`, `Milk per serving is 1.75`, `While tea bags per pots is 1`, `Leftover cardamon pods 1`, `Scale flavour strength 8`, `Is there milk? False/True/False`, `Can we serve Chai? False`, and float precision details like `Differnce in temp 0.0010000000000047748` plus `sys.float_info`.
  - Strings: slicing and stepping (`desc[:8]`, `desc[::-1]`), reversing, and UTF-8 encode/decode round-trips for labels like `"Chai Spécial"`. Outputs include `First word: Aromatic`, `Last word: Bold`, `First word skipped: Aoai`, `Reversed word: dloB dna citaromA`, and matching decoded text.
  - Tuples: packing/unpacking, swapping, and membership. Outputs show `Main masala spieces: cardamom, cloves, cinnamon`, swapped ratios, and membership checks (`False` for ginger, `True` for cinnamon).
  - Lists: append/remove/extend/insert/pop/reverse/sort; operator overloading with `+` and `*`; `bytearray` for mutable bytes. Outputs include ingredient lists as they change, popped value `cardamom`, sorted lists, max/min sugar levels, repeated lists, and byte manipulations such as `bytearray(b'CINNAMON')` transforming to `bytearray(b'CARDNAMON')`.
  - Sets: union, intersection, difference, membership. Outputs: combined spice sets, common elements (`{'ginger'}`), differences (`{'cinnamon', 'cardamom'}`), and membership booleans.
  - Dictionaries: creation, updates, deletion, membership, key/value/item views, `popitem`, `update`, `get` with defaults. Fix nested f-string quotes before running to avoid syntax errors. Intended outputs show order/recipe contents, membership `True/False`, removed items, updated recipes, and default `"No Note"`.
  - Date/time and collections: quick `arrow.utcnow()` usage with `.shift(hours=2)` and `namedtuple` construction. Outputs include a UTC timestamp, ETA two hours ahead, and the namedtuple type `chaiProfile(flavour, aroma, color)`.

- **Conditionals**
  - Basic if/else: print `"Kettle Done! Time to make Chai!"` when a flag is true.
  - Nested checks: smart thermostat prints `"High temperature alert!"` when active and hot; otherwise `"Temperature is normal"` or `"Device is offline"`.
  - Ternary/inputs: delivery fee calculator returns `0` when amount > 300 else `30`, after casting input to `int`.
  - Multi-branching: cup-size chooser prints `10/15/20 rupees` for small/medium/large or `"Unknown cup size"` otherwise.
  - String normalization: snack suggestion lowers input and only accepts `samosa` or `cookies`.
  - Pattern matching: train seat selector uses `match/case` for sleeper/AC/general/luxury with a default `"Invalid seat type"`.

- **Loops**
  - `for` over ranges/lists: token dispenser prints `"Serving chai to Token #n"` (1–10); batch prep prints `"Preparing chai for batch #n"`; order list prints `"Order ready for <name>"`; `enumerate` prints numbered menu.
  - `zip`: name/bill pairs like `"Rhea paid 50 rupees"`.
  - `while`: heat until temperature reaches 100, printing each step and `"Tea is ready to be served"`.
  - Flow control: skip `"out of stock"`, break on `"Discontinued"`, and print remaining flavors plus `"outside of loop"`.
  - `for-else`: finds the first eligible staff (age ≥ 17) or prints `"No one is eligible to manage the staff"`.
  - Walrus operator `:=`: reuses computed remainder, validates cup sizes and flavors in input loops until a valid choice.
  - Dictionary iteration: applies percent/fixed discounts per user; fix f-string quotes before running to see outputs like `1 paid 100 and got discount for next visit of rupees 20.0`.

- **Functions**
  - DRY and decomposition: reusable order printer; report generator split into fetch/filter/summarize steps ending with `"Report is ready"`.
  - Hiding complexity: registration flow splits input, validation, persistence, ending with `"User registeration complete"`.
  - Readability: simple calculator returns cups × price; prints `My bill: 45` and `Order for table 2: 100`.
  - Traceability: VAT helper applied to a list shows original and final amounts (e.g., `Original value: 100, final with VAT: 110.0`).
  - Scope rules: local vs global vs enclosing; prints inside/outside values and demonstrates `nonlocal` (changes enclosing `chai_type` to `Kesar`) and `global` (changes global `chai_type` to `"Irani"`).
  - Parameters: positional vs keyword, `*args/**kwargs`, mutating list arguments, and safe mutable defaults. Outputs include `[1, 42, 3]`, ingredient/extras tuples/dicts, and order lists accumulating `"Ginger"`.
  - Returns: `pass` gives `None`; fixed returns; early returns; tuple packing/unpacking with sold/remaining counts; final reassignment adds a third return value.
  - Function styles: pure vs impure counters, recursion for pouring chai (counts down then returns `"All cups poured"`), and lambda with `filter` returning `['kadak', 'kadak']`.
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

- **Generators**
  - Motivation: lazy, memory-saving iteration; key verbs are `yield`, `next`, `send`, `yield from`, `close`.
  - Basics: generator object shows as `<generator ...>`; successive `next` calls yield `"Cup 1"`, `"Cup 2"`, `"Cup 3"`, then a `StopIteration` on an extra call.
  - Infinite patterns: token-like refills produce `"Refil #1"`, `"Refil #2"`, `"Refil #3"` (and more for another consumer).
  - `send`: prime the generator with `next`, then `send` orders to see `"Preparing Masala Chai"` and `"Preparing Lemon Chai"`.
  - `yield from`: combine multiple menus into one stream, printing local then imported teas; `close()` triggers cleanup message `"Stall closed, no more chai"` after `"Waiting for chai order"`.
  - Token dispenser app: prints start message, emits tokens, supports resets (e.g., jump to token 10), and prints `"Dispenser closed."` on shutdown.

- **Decorators**
  - Basics: wrapper adds before/after behavior while `functools.wraps` keeps metadata (`__name__` stays `greet`). Output sequence: `"Before function runs"`, greeting, `"After function runs"`, then prints `greet`.
  - Logging decorator: wraps any function to show start/end messages. Fix nested f-string quotes inside the sample before running. Intended output: `Calling: brew_chai`, `Brewing Masala chai, without milk`, `Finished: brew_chai`.
  - Auth decorator: role gate that prints `"Access denied: Admins only"` for non-admin and `"Access granted to tea inventory"` for admin.
  - Placeholder YAML exists for decorator notes.

- **Placeholders**
  - Empty/topic stubs are present for namespace notes, advanced data types, a walrus directory, chai shop processing, and utils—ready to be populated later.

Use this single document to revise: concepts, behaviors, and expected outputs are all summarized here. Fix the noted f-string quote issues before executing those samples to avoid syntax errors.
