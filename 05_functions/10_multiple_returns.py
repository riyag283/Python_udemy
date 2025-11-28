# def make_chai():
#     print("Here is your Masala Chai") 

# return_value = make_chai()
# print(return_value)

def idle_chaiwala():
    pass

print(idle_chaiwala())

def sold_cups():
    return 120

total = sold_cups()
print(total)

# returning early
def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"

print(chai_status(0))
print(chai_status(5))

# returing multiple values
def chai_report():
    return 100, 20

print(chai_report())

sold, remaining = chai_report()
print("Sold:", sold)
print("Remaining:", remaining)

def chai_report():
    return 100, 20, 1

sold, remaining, not_paid = chai_report()

