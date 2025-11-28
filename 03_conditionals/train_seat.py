seat_type = input("Enter seat type (sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC, comfy beds available")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with beds and meals")
    case _:
        print("Invalid seat type")