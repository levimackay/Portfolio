from datetime import datetime

def user_input():
    gender = input("Enter your gender (M/F): ").strip().upper()
    while gender not in ['M', 'F']:
        print("Invalid input. Please enter 'M' or 'F'.")
        gender = input("Enter your gender (M/F): ").strip().upper()

    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    height_unit = input("Enter height unit (in or ft/in): ").strip().lower()
    if height_unit == "ft/in":
        feet = int(input("Enter feet: "))
        inches = int(input("Enter inches: "))
        height_in = inches_from_feet_and_inches(feet, inches)
    else:
        height_in = float(input("Enter your height in inches: "))
    weight_lbs = float(input("Enter your weight in pounds: "))
    return gender, birthdate, weight_lbs, height_in

def inches_from_feet_and_inches(feet, inches):
    return feet * 12 + inches

def compute_age(birth_str):
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year
    if birthdate.month > today.month or (birthdate.month == today.month and birthdate.day > today.day):
        years -= 1
    return years

def kg_from_lb(pounds):
    return pounds * 0.45359237

def cm_from_in(inches):
    return inches * 2.54

def meters_from_cm(cm):
    return cm / 100

def body_mass_index(weight, height):
    bmi = (weight * 10000) / (height ** 2)
    return round(bmi, 1)

def bmi_category(bmi):
    if bmi < 18.5:
        return "You're skinny"
    elif bmi < 25:
        return "You're aight"
    elif bmi < 30:
        return "You're fat"
    else:
        return "Obese"

def basal_metabolic_rate(gender, weight, height, age):
    if gender == 'M':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return round(bmr, 1)

def main():
    gender, birthdate, weight_lbs, height_in = user_input()
    age = compute_age(birthdate)
    weight_kg = kg_from_lb(weight_lbs)
    height_cm = cm_from_in(height_in)
    height_m = meters_from_cm(height_cm)
    bmi = body_mass_index(weight_kg, height_cm)
    bmr = basal_metabolic_rate(gender, weight_kg, height_cm, age)

    print(f"\nAge (years): {age}")
    print(f"Weight (kg): {weight_kg:.2f}")
    print(f"Height (cm): {height_cm:.2f}")
    print(f"Height (m): {height_m:.2f}")
    print(f"Body mass index: {bmi:.1f} ({bmi_category(bmi)})")
    print(f"Basal metabolic rate (kcal/day): {bmr:.1f}")

main()