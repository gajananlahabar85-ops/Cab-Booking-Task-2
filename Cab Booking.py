import random

cab_rates = {
    1: ("Mini Cab", 10),
    2: ("Comfort Cab", 16),
    3: ("Premium Cab", 24)
}

routes = {
    1: ("Nagpur Railway Station", "Sitabuldi", 4),
    2: ("Zero Mile", "Dharampeth", 6),
    3: ("Airport", "Medical Square", 12)
}


def book_ride():
    print("\n--- SELECT YOUR CAB ---")
    for key, value in cab_rates.items():
        print(f"{key}. {value[0]} - Rs.{value[1]}/km")

    try:
        cab_choice = int(input("Choose cab: "))
        if cab_choice not in cab_rates:
            print("Invalid cab selection.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print("\n--- AVAILABLE ROUTES ---")
    for key, value in routes.items():
        print(f"{key}. {value[0]} to {value[1]} - {value[2]} km")

    try:
        route_choice = int(input("Choose route: "))
        if route_choice not in routes:
            print("Invalid route selection.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    cab_name, rate = cab_rates[cab_choice]
    source, destination, distance = routes[route_choice]
    fare = rate * distance

    print("\n====== RIDE SUMMARY ======")
    print("Cab:", cab_name)
    print("From:", source)
    print("To:", destination)
    print("Distance:", distance, "km")
    print("Rate per km: Rs.", rate)
    print("Total fare: Rs.", fare)

    print("\n1. Confirm booking")
    print("2. Cancel booking")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid choice. Booking not confirmed.")
        return

    if choice == 2:
        print("Your ride has been cancelled.")
    elif choice == 1:
        otp = random.randint(1000, 9999)
        print("\nYour booking OTP is:", otp)
        print("Ride booking successful!")
        print("Cancellation is not allowed after OTP sharing.")
    else:
        print("Invalid choice. Booking not confirmed.")


while True:
    print("\n====== CAB BOOKING CHATBOT ======")
    print("1. Book a Ride")
    print("2. Exit")

    try:
        menu = int(input("Select an option: "))
    except ValueError:
        print("Please enter 1 or 2.")
        continue

    if menu == 1:
        book_ride()
    elif menu == 2:
        print("Thank you for using our Cab Booking Chatbot!")
        break
    else:
        print("Invalid option. Please try again.")