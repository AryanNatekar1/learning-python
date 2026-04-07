# Aryan's First Python Script
print("--- 🤖 Robot Controller v1.0 ---")

name = input("Enter your name, Engineer: ")
print(f"Welcome, {name}! Let's test the logic.")

num1 = float(input("Enter distance to obstacle (cm): "))

if num1 < 20:
    print("⚠️ ALERT: Object too close! Stop the motor.")
else:
    print("✅ Path clear. Continue moving.")