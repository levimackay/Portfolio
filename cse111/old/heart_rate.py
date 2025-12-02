import math

age = int(input("Enter your age: "))
max_heart_rate = 220 - age

min_target = int(max_heart_rate * 0.65)
max_target = int(max_heart_rate * 0.85)

print(f"Your maximum heart rate is: {max_heart_rate} bpm")
print(f"Your target heart rate zone is: {min_target} - {max_target} bpm")
print("To maintain a healthy heart rate, aim to exercise within this zone.")