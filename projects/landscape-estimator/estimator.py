import math

def calculate_volume(sq_ft, depth_inches):
    cubic_feet = sq_ft * (depth_inches / 12)
    cubic_yards = cubic_feet / 27
    return math.ceil(cubic_yards)

def generate_estimate():
    print("--- JOB ESTIMATOR ---")
    
    try:
        area = float(input("Enter total area in SqFt: "))
        depth = float(input("Enter depth in inches: "))
        material_cost = float(input("Cost per cubic yard: "))
        labor_rate = float(input("Labor rate per hour: "))
        
        yards_needed = calculate_volume(area, depth)
        material_total = yards_needed * material_cost
        

        labor_hours = yards_needed * 0.5 
        labor_total = labor_hours * labor_rate
        
        grand_total = material_total + labor_total

        print("\n" + "="*30)
        print(f"JOB SUMMARY")
        print("="*30)
        print(f"Materials: {yards_needed} Cubic Yards")
        print(f"Material Cost: ${material_total:.2f}")
        print(f"Labor Hours: {labor_hours:.1f}")
        print(f"Labor Cost: ${labor_total:.2f}")
        print("-" * 30)
        print(f"GRAND TOTAL: ${grand_total:.2f}")
        print("="*30)

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    generate_estimate()
