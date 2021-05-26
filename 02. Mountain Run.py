record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_for_one_meter = float(input())
delay = (distance_in_meters // 50) * 30
climbing_time = distance_in_meters * seconds_for_one_meter + delay
difference = climbing_time - record_in_seconds
if climbing_time < record_in_seconds:
    print(f"Yes! The new record is {climbing_time:.2f} seconds.")
else:
    print(f"No! He was {difference:.2f} seconds slower.")
