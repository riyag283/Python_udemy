import sys
from fractions import Fraction
from decimal import Decimal as D

ideal_temp = 95.5
current_temp = 95.499

print(f"Ideal temp {ideal_temp}")
print(f"Current temp {current_temp}")
print(f"Differnce in temp {ideal_temp - current_temp}")

print(sys.float_info)

