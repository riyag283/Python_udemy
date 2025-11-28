# List [expression for item in iterable if condition] - make an entire list in memory
# Generator (expression for item in iterable if condition) - like a stream

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
# _list = [x for x in daily_sales]
# _generator = (x for x in daily_sales)

# memory efficient
total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)

