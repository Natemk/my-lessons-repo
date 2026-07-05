def create_car():
    # Prompt the user to build a car dictionary
    print("\nCreate a car dictionary")
    car = {
        "make": "",
        "model": "",
        "year": 0
    }

    # Get the make and model from the user
    car["make"] = input("Enter the car make: ").strip() or "Unknown"
    car["model"] = input("Enter the car model: ").strip() or "Unknown"
    year_input = input("Enter the car year: ").strip()

    if year_input.isdigit() :
        car["year"] = int(year_input)
    else:
        car["year"] = 0

    return car


def print_car(car):
    # Display the saved car details
    print("\nCar details")
    print("--------------------")
    for key, value in car.items():
        print(f"{key}: {value}")
    print("--------------------")


def main():
    # Main program flow: create a car and then print it
    car = create_car()
    print_car(car)


if __name__ == "__main__":
    main()