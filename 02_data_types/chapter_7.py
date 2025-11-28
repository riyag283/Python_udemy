masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spieces: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2, 1
print(f"Ratio is G: {ginger_ratio} and C: {cardamom_ratio}")

# swapping
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ratio is G: {ginger_ratio} and C: {cardamom_ratio}")

# membership testing
print(f"Is ginger in masala spices? {'ginger' in masala_spices}")
print(f"Is cinnamon in masala spices? {'cinnamon' in masala_spices}")