from datetime import datetime

sales_tax_rate = 0.06
discount_rate = 0.10

def discount():
    subtotal = float(input("Enter the subtotal: "))
    weekday = datetime.now().weekday()
    discount_amount = 0

    if subtotal > 50 or (subtotal < 50 and weekday in [1, 2]): 
        discount_amount = subtotal * discount_rate

    discounted_subtotal = subtotal - discount_amount
    sales_tax = discounted_subtotal * sales_tax_rate
    total = discounted_subtotal + sales_tax

    print(f"Subtotal: {subtotal:.2f}")
    if discount_amount > 0:
        print(f"Discount: {discount_amount:.2f}")
    print(f"Sales tax: {sales_tax:.2f}");
    print(f"Total: {total:.2f}")

    return total

discount()
