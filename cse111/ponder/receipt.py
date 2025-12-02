from datetime import datetime, timedelta
import random

SALES_TAX_RATE = 0.06
DISCOUNT_RATE = 0.10

def read_dictionary(filename, key_column_index):
    products_dictionary = {}
    with open(filename, "r") as file:
        next(file) 
        for line in file:
            line = line.strip().split(',')
            key = line[key_column_index]
            products_dictionary[key] = line
    return products_dictionary

def should_apply_discount(current_datetime):
    weekday = current_datetime.weekday()  
    hour = current_datetime.hour
    return weekday in [1, 2] or hour < 11

def main():
    try:
        current_datetime = datetime.now()
        discount_applies = should_apply_discount(current_datetime)
        products_dict = read_dictionary("products.csv", 0)
        print('-' * 40)
        print("Inkom Emporium")
        print('-' * 40)
        total_items = 0
        subtotal = 0
        purchased_products = []
        with open("request.csv", "r") as file:
            next(file)  
            for line in file:
                parts = line.strip().split(",")
                prod_num = parts[0]
                quantity = int(parts[1])
                try:
                    product = products_dict[prod_num]
                    name = product[1]
                    price = float(product[2])
                    if discount_applies:
                        price *= (1 - DISCOUNT_RATE)
                    print(f"{name}: {quantity} @ {price:.2f}")
                    total_items += quantity
                    subtotal += quantity * price
                    purchased_products.append(name)
                except KeyError as e:
                    print("Error: unknown product ID in the request.csv file")
                    print(f"{e}")
                    return
        sales_tax = round(subtotal * SALES_TAX_RATE, 2)
        total = round(subtotal + sales_tax, 2)
        print('-' * 40)
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print("\nThank you for shopping at the Inkom Emporium.")
        print(f"{current_datetime:%a %b %d %H:%M:%S %Y}")
        print("\n🎯 We'd love your feedback! Complete our 2-minute survey at:")
        print("https://www.inkomemporium.com/survey")
        print('-' * 40)
        if purchased_products:
            coupon_item = random.choice(purchased_products)
            print(f"\n🎁 Coupon: Get 20% off your next purchase of {coupon_item}!")
        return_date = current_datetime + timedelta(days=7)
        print(f"🔁 Returns accepted through: {return_date:%A, %B %d, %Y}")
        new_year = datetime(current_datetime.year + 1, 1, 1)
        days_until_new_year = (new_year - current_datetime).days
        print(f"🎉 Only {days_until_new_year} days until our New Year's Sale!")
        if discount_applies:
            print("\n✅ You received a 10% discount for shopping early or midweek!")
        print('-' * 40)
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)

if __name__ == "__main__":
    main()
