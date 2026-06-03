# =============================================================================
# FOREMAN'S FRIEND: LANDSCAPE JOB ESTIMATOR
#
# So, before I was grinding code, I was a landscape foreman.
# One of the most annoying parts of the job was trying to estimate 
# materials (mulch, sod, rock) on the fly while standing in a client's yard.
#
# This is a quick CLI tool I built to handle the math. It calculates
# volume based on square footage and depth, adds labor rates, and 
# spits out a clean quote. 
#
# No more "guesstimating" and losing money on mulch.
# =============================================================================

import math

def calculate_volume(sq_ft, depth_inches):
    """ 
    Calculates cubic yards needed. 
    Formula: (SqFt * (Depth/12)) / 27 
    """
    cubic_feet = sq_ft * (depth_inches / 12)
    cubic_yards = cubic_feet / 27
    return math.ceil(cubic_yards) # Always round up, better to have extra than be short.

def generate_estimate():
    print("--- FOREMAN'S FRIEND: JOB ESTIMATOR ---")
    print("Let's get this quote sorted.\n")

    try:
        # Get the basics
        area = float(input("Enter total area in Square Feet: "))
        depth = float(input("Enter desired depth in inches (e.g., 3 for mulch): "))
        material_cost = float(input("Cost of material per cubic yard ($): "))
        labor_rate = float(input("Labor rate per hour ($): "))
        
        # Estimation logic
        yards_needed = calculate_volume(area, depth)
        material_total = yards_needed * material_cost
        
        # Assuming a standard pace (e.g., 1 hour per 2 yards for spreading)
        labor_hours = yards_needed * 0.5 
        labor_total = labor_hours * labor_rate
        
        grand_total = material_total + labor_total

        # Spitting out the results
        print("\n" + "="*30)
        print(f"JOB SUMMARY")
        print("="*30)
        print(f"Materials Needed: {yards_needed} Cubic Yards")
        print(f"Material Cost:   ${material_total:.2f}")
        print(f"Estimated Labor: {labor_hours:.1f} Hours")
        print(f"Labor Cost:      ${labor_total:.2f}")
        print("-" * 30)
        print(f"GRAND TOTAL:     ${grand_total:.2f}")
        print("="*30)
        
        print("\nSend it. Good luck with the client.")

    except ValueError:
        print("My man, you gotta enter actual numbers.")

if __name__ == "__main__":
    generate_estimate()
