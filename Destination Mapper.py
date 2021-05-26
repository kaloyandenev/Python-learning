import re
destinations = input()
pattern = r"(?<=(=|/))[A-Z][a-zA-Z]{2,}(?=\1)"
matched = [match.group() for match in re.finditer(pattern, destinations)]
travel_points = 0
for destination in matched:
    travel_points += len(destination)
print(f"Destinations: {', '.join(matched)}")
print(f"Travel Points: {travel_points}")

