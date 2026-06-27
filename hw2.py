def create_car():
    print("\nCreate a car dictionary")
    car = {
        "make": "",
        "model": "",
        "year": 0
    }

    car["make"] = input("Enter the car make: ").strip() or "Unknown"
    car["model"] = input("Enter the car model: ").strip() or "Unknown"
    year_input = input("Enter the car year: ").strip()

    if year_input.isdigit():
        car["year"] = int(year_input)
    else:
        car["year"] = 0

    return car


def print_car(car):
    print("\nCar details")
    print("--------------------")
    for key, value in car.items():
        print(f"{key}: {value}")
    print("--------------------")


def main():
    car = create_car()
    print_car(car)


if __name__ == "__main__":
    main()