# streams, real-time systems
# be cautious: can drain memory

def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()

for _ in range(3):
    print(next(refill))

user2 = infinite_chai()
for _ in range(6):
    print(next(user2))

