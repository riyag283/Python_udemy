# Python Udemy Project Learnings

- **Setup basics** (`00_python/pep8_and_zen`, `00_python/virtual_environment`, `01_1_virtual/requirements.txt`): noted PEP8 conventions, Zen of Python, and using virtual environments (`python3 -m venv .venv && source .venv/bin/activate`) to isolate dependencies like `requests` and `flask`.
- **Objects & classes** (`00_python/non_python_shop.py`): defined a simple `Chai` class with methods (`sip`, `add_sugar`) to illustrate object state (`sweetness`, `milk_level`) and behavior.
  ```python
  my_chai = Chai(sweetness=3, milk_level=2)
  my_chai.add_sugar()  # -> Added the sugar
  ```
- **Data types & mutability**
  - Integers are immutable references (`02_data_types/chapter_1.py`), while containers like sets are mutable (`chapter_2.py`).
    ```python
    sugar_amount = 2; print(id(sugar_amount))
    sugar_amount = 12; print(id(sugar_amount))  # new id shows immutability
    ```
  - Arithmetic ops and formatting for ints/floats (`chapter_3.py`, `chapter_5.py`); boolean truthiness and logical operators (`chapter_4.py`).
    ```python
    milk_per_serving = 7 / 4     # 1.75
    bool(0), bool(11), bool(None)  # False, True, False
    ```
  - Strings: slicing, steps, reversing, UTF-8 encode/decode round-trip (`chapter_6.py`).
    ```python
    desc = "Aromatic and Bold"
    desc[:8], desc[::-1]  # 'Aromatic', 'dloB dna citaromA'
    ```
  - Tuples for packing/unpacking and swapping, membership checks (`chapter_7.py`).
    ```python
    spice1, spice2, spice3 = ("cardamom", "cloves", "cinnamon")
    ginger, cardamom = 2, 1; ginger, cardamom = cardamom, ginger
    "ginger" in spice1  # False
    ```
  - Lists: append/remove/extend/insert/pop/reverse/sort, operator overloading with `+` and `*`, working with `bytearray` for mutable bytes (`chapter_8.py`).
    ```python
    chai = ["water", "milk"]; chai.extend(["ginger", "cardamom"]); chai.pop()
    ["black tea"] * 3  # ['black tea', 'black tea', 'black tea']
    ```
  - Sets: union, intersection, difference, membership testing (`chapter_9.py`).
    ```python
    essential | optional  # union; &, - for intersection/difference
    ```
  - Dicts: literal creation, key access, deletion, membership checks, `keys`/`values`/`items`, `popitem`, `update`, `get` with defaults (`chapter_10.py`).
    ```python
    order = dict(type="Masala", sugar=2)
    order.get("note", "No Note")  # default fallback
    ```
  - Date/time and collections: quick look at `arrow` for time math and `namedtuple` for structured data (`chapter_11.py`); notes on `datetime`, `timedelta`, etc. in `02_data_types/advanced_data_types`.
    ```python
    future = arrow.utcnow().shift(hours=2)
    chaiProfile = namedtuple("chaiProfile", ["flavour", "aroma", "color"])
    ```
- **Conditionals** (`03_conditionals/*`): standard `if/elif/else` branching for chai pricing and snack suggestions, ternary expressions for delivery fees, nested conditions for device checks, and `match/case` pattern matching for train seat types.
  ```python
  delivery_fees = 0 if amount > 300 else 30
  match seat_type:
      case "sleeper": ...
  ```
- **Loops** (`04_loops/*`):
  - `for` over ranges, lists, and with `enumerate` or `zip` for paired iteration.
  - `while` loops with increment logic and exit messages.
  - Control flow with `continue`/`break`, plus `for-else` to detect missing matches.
  - Walrus operator `:=` for inline assignment in conditions and input validation.
  - Iterating dictionaries and calculating discounts from coupon data.
  ```python
  for idx, item in enumerate(menu, 1): print(idx, item)
  while temp < 100: temp += 15
  if (size := input()) in sizes: ...
  ```
- **Functions** (`05_functions/*`):
  - Encapsulating behavior to reduce duplication and split complex tasks (`01_duplication.py`, `02_complex.py`, `03_hiding.py`).
  - Readability via clear parameters and return values (`04_readability.py`, `05_traceability.py`).
  - Scope rules (local/enclosing/global/built-in), `nonlocal` and `global` updates (`06_scopes.py`, `07_non_local.py`, `08_global_scope.py`).
  - Parameter handling: positional vs keyword args, `*args`/`**kwargs`, mutable default pitfalls avoided with `None` sentinel (`09_input_params.py`).
  - Return patterns: `None`, single/multiple returns, early returns, and tuple unpacking (`10_multiple_returns.py`).
  - Function styles: pure vs impure, recursion, lambdas with `filter` (`11_types_of_functions.py`).
  - Docstrings and dunder metadata (`__doc__`, `__name__`), plus doc-style notes in `generate_bill` (`12_built_in.py`).
  - Import patterns and aliasing reminders (`13_imports.py`); simple package imports via `06_chai_business/main.py` using `recipes/flavors.py`.
  ```python
  def chai_order(order=None):
      if order is None: order = []
      order.append("Ginger"); return order
  pure_chai = lambda cups: cups * 10
  from recipes.flavors import ginger_chai
  ```
- **Comprehensions** (`07_comprehensions/*`): list, set, and dict comprehensions to filter/transform menus and prices, and generator expressions for memory-efficient summation.
  ```python
  iced = ["My " + tea for tea in menu if "Iced" in tea]
  prices_usd = {t.replace("Chai", "Tea"): p/80 for t, p in prices.items()}
  total = sum(s for s in daily_sales if s > 5)
  ```
- **Generators** (`08_generators/*`): basic `yield`/`next` usage, infinite generators for refill tokens, `send` to pass values in, `yield from` to chain generators, and graceful shutdown with `close`/`GeneratorExit`; includes a token dispenser example with reset support.
  ```python
  def infinite_chai():
      count = 1
      while True: yield f"Refil #{count}"; count += 1
  refill = infinite_chai(); next(refill)
  stall = chai_customer(); next(stall); stall.send("Masala Chai")
  ```
- **Decorators** (`09_decorators/*`): wrapper pattern with `functools.wraps` to preserve metadata, logging decorator that accepts `*args/**kwargs`, and an auth gate decorator to restrict access based on user roles.
  ```python
  @log_activity
  def brew_chai(kind, milk): ...
  @require_admin
  def access_tea_inventory(role): ...
  ```

Use this as a quick reference to revisit topics and locate runnable examples across the repo.
