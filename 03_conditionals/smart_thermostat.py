device_status = "active"
temperature = 48

if device_status == "active":
    # pass
    if temperature > 35:
        print(f"High temperature alert!")
    else:
        print(f"Temperature is normal")
else:
    print(f"Device is offline")