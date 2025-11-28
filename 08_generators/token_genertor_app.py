def token_generator(start = 1):
    print(f"Dispenser started with start token - {start}...")
    token = start
    try:
        while True:
            print(f"Generated token: #{token}")
            reset_token = yield token
            if reset_token:
                token = reset_token
            else:
                token += 1
    except GeneratorExit:
        print("Dispenser closed.")
    
# creating the generator object
dispenser = token_generator()

# first call 
next(dispenser)
# second call
next(dispenser)

# sending reset value
dispenser.send(10)
for _ in range(5):
    next(dispenser)

# closing the generator
dispenser.close()