import math
total_passangers = 0
airlines_number = int(input())
max_passangers = 0
max_passangers_airline = ""
average_passangers_of_max_airline = 0
for flights in range(airlines_number):
    airline_name = input()
    command = input()
    passangers_per_airline = 0
    flights_counter = 0
    while command != "Finish":
        passangers_per_flight = int(command)
        flights_counter += 1
        passangers_per_airline += passangers_per_flight
        total_passangers += passangers_per_flight

        command = input()
    average_pass = math.floor(passangers_per_airline / flights_counter)
    if average_pass > max_passangers:
        max_passangers = average_pass
        max_passangers_airline = airline_name
    print(f"{airline_name}: {average_pass} passengers.")
print(f"{max_passangers_airline} has most passengers per flight: {max_passangers}")