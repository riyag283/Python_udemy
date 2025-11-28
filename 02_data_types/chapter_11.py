import arrow

brewing_time = arrow.utcnow()
brewing_time.to("local")

print(f"Brewing time: {brewing_time}")

future = brewing_time.shift(hours=2)
future.humanize(brewing_time)
print(f"ETA: {future}")

from collections import namedtuple

chaiProfile = namedtuple("chaiProfile", ["flavour", "aroma", "color"])
print(f"Chai Profile: {chaiProfile}")