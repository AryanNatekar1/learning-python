# --- DAY 1: ROBOT IDENTITY ---

# 1. We create variables to hold information
name = "Alpha-1"
version = 1.0

print("Booting System...")
print("Robot Name: " + name)
print(f"Software Version: {version}")

# 2. We ask the user for data (Input)
battery = int(input("Enter battery level (0-100): "))

# 3. We print a confirmation
print(f"Status: Battery is at {battery}%. Ready for Day 2!")