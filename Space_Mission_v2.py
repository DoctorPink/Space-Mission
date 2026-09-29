# ==================================================
# SPACE MISSION COMPUTER
# Version 2 - Communication Monitoring
# ==================================================

print("=" * 50)
print("PYTHON SPACE COMMAND")
print("=" * 50)
print()

# --------------------------------------------------
# MISSION INPUT
# --------------------------------------------------

commander = input("Commander: ")
spacecraft = input("Spacecraft: ")
destination = input("Destination: ")

distance = float(input("Distance in millions of miles: "))
speed = float(input("Speed in thousands of miles per hour: "))

fuel_capacity = float(input("Fuel capacity: "))
fuel_used = float(input("Fuel used: "))

# New in Version 2
signal_quality = int(input("Signal quality (0-100): "))


# --------------------------------------------------
# ORIGINAL CALCULATIONS
# --------------------------------------------------

travel_hours = (distance * 1000) / speed
travel_days = travel_hours / 24

fuel_remaining = fuel_capacity - fuel_used
fuel_percent = (fuel_remaining / fuel_capacity) * 100


# --------------------------------------------------
# COMMUNICATION MONITORING - VERSION 2
# --------------------------------------------------

if signal_quality < 0 or signal_quality > 100:
    signal_status = "INVALID READING"
elif signal_quality >= 80:
    signal_status = "STRONG"
elif signal_quality >= 50:
    signal_status = "STABLE"
elif signal_quality >= 1:
    signal_status = "WEAK"
else:
    signal_status = "SIGNAL LOST"


# --------------------------------------------------
# MISSION REPORT
# --------------------------------------------------

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

print()
print("COMMUNICATIONS")
print("-" * 50)
print(f"Signal Quality: {signal_quality}")
print(f"Signal Status:  {signal_status}")

print("=" * 50)