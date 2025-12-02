import math
from datetime import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
    return volume

def get_tire_price(width, aspect_ratio, diameter):
    if width == 185 and aspect_ratio == 50 and diameter == 14:
        return 100.00
    elif width == 205 and aspect_ratio == 60 and diameter == 15:
        return 120.00
    elif width == 225 and aspect_ratio == 55 and diameter == 16:
        return 135.00
    elif width == 245 and aspect_ratio == 45 and diameter == 17:
        return 150.00
    else:
        return 160.00  

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
volume = calculate_tire_volume(width, aspect_ratio, diameter)
print(f"\nThe approximate volume is {volume:.2f} liters")
current_date = datetime.now().strftime("%Y-%m-%d")
price = get_tire_price(width, aspect_ratio, diameter)
print(f"The price for this tire size is: ${price:.2f}")

with open("volumes.txt", "at") as file:
    print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file=file)
buy_choice = input("Do you want to buy tires with these dimensions? (yes/no): ").strip().lower()
if buy_choice == "yes":
    phone = input("Please enter your phone number: ")
    with open("volumes.txt", "at") as file:
        print(f"Customer phone: {phone}", file=file)
