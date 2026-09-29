# ==================================================
# SPACE MISSION COMPUTER
# Version 1 - Modules 1-2
# ==================================================

print("=" * 50)
print("PYTHON SPACE COMMAND")
print("=" * 50)
print()

# Mission input
commander = input("Commander: ")
spacecraft = input("Spacecraft: ")
destination = input("Destination: ")

distance = float(input("Distance in millions of miles: "))
speed = float(input("Speed in thousands of miles per hour: "))

fuel_capacity = float(input("Fuel capacity: "))
fuel_used = float(input("Fuel used: "))

# Calculations
# Both distance and speed use thousands/millions,
# so convert the distance to thousands of miles.
travel_hours = (distance * 1000) / speed
travel_days = travel_hours / 24

fuel_remaining = fuel_capacity - fuel_used
fuel_percent = (fuel_remaining / fuel_capacity) * 100

# Mission report
print()
print("=" * 50)
print("MISSION REPORT")
print("=" * 50)

print(f"Commander:   {commander}")
print(f"Spacecraft:  {spacecraft}")
print(f"Destination: {destination}")

print()
print("TRAVEL")
print("-" * 50)
print(f"Distance:     {distance:.2f} million miles")
print(f"Speed:        {speed:.2f} thousand mph")
print(f"Travel Hours: {travel_hours:.2f}")
print(f"Travel Days:  {travel_days:.2f}")

print()
print("FUEL")
print("-" * 50)
print(f"Capacity:       {fuel_capacity:.2f}")
print(f"Used:           {fuel_used:.2f}")
print(f"Remaining:      {fuel_remaining:.2f}")
print(f"Fuel Remaining: {fuel_percent:.2f}%")

print("=" * 50)