'''
import math

def convert_celsius_to_fahrenheit(celsius): # 5
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def get_average_temperature(readings): # 4
    """Calculate the average of a list of temperatures."""
    return sum(readings) / len(readings)

def display_temperature_report(readings): # 3
    """Display temperature report with converted values."""
    avg_celsius = get_average_temperature(readings)
    avg_fahrenheit = convert_celsius_to_fahrenheit(avg_celsius)
    print("Average Celsius Temperature:", round(avg_celsius, 2))
    print("Average Fahrenheit Temperature:", round(avg_fahrenheit, 2))

temps = [18.5, 20.0, 19.6, 21.11] # 2

display_temperature_report(temps) # 1
'''

'''
import time

def start_timer(): # 1
    """Return the start time."""
    return time.time()

def stop_timer(): # 3
    """Return the stop time."""
    return time.time()

def display_elapsed_time(start, stop): # 4
    """Display the elapsed time between two timestamps."""
    elapsed = stop - start
    print(f"Elapsed time: {round(elapsed, 2)} seconds")

start = start_timer()
time.sleep(1.5) # 2
stop = stop_timer()
display_elapsed_time(start, stop) 
'''

'''
import random

def generate_random_numbers(count, lower, upper): # 3
    """Generate a list of random integers."""
    return [random.randint(lower, upper) for _ in range(count)]

def find_maximum(numbers): # 4
    """Find the maximum number in a list."""
    return max(numbers)

def analyze_numbers(): # 2
    """Generate numbers, find the max, and print results."""
    nums = generate_random_numbers(5, 1, 100)
    max_num = find_maximum(nums)
    print("Numbers:", nums)
    print("Maximum number:", max_num)

analyze_numbers() # 1
'''