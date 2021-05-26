cars_number = int(input())
cars = {}
for _ in range(cars_number):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = {"mileage": mileage, "fuel": fuel}

command = input()

while not command == "Stop":
    if command.startswith("Drive"):
        car, distance, fuel = command.split(" : ")[1:]
        distance = int(distance)
        fuel = int(fuel)
        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["fuel"] -= fuel
            cars[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]["mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            cars.pop(car)
    elif command.startswith("Refuel"):
        car, fuel = command.split(" : ")[1:]
        fuel = int(fuel)
        cars[car]["fuel"] += fuel
        total_refill = 0
        if cars[car]["fuel"] > 75:
            total_refill = fuel - (cars[car]["fuel"] - 75)
            cars[car]["fuel"] = 75
        else:
            total_refill = fuel
        print(f"{car} refueled with {total_refill} liters")
    elif command.startswith("Revert"):
        car, km = command.split(" : ")[1:]
        km = int(km)
        cars[car]["mileage"] -= km
        if cars[car]["mileage"] >= 10000:
            print(f"{car} mileage decreased by {km} kilometers")
        else:
            cars[car]["mileage"] = 10000

    command = input()

sorted_cars = dict(sorted(cars.items(), key=lambda kvp: (-kvp[1]["mileage"], kvp[0])))

for car in sorted_cars:
    print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")
