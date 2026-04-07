# --- DAY 2: ROBOT LOGIC ---

print("--- Radar System Online ---")

# 1. Ask for sensor data
distance = int(input("Obstacle distance (cm): "))

# 2. The Decision Maker (If-Else)
if distance < 20:
    print("🛑 ALERT: Object too close! Applying BRAKES.")
elif distance < 50:
    print("⚠️ WARNING: Object detected. Reducing SPEED.")
else:
    print("✅ PATH CLEAR: Full speed ahead.")

# 3. Final Status
print("Scan complete.")