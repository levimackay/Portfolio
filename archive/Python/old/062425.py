x = 5
y = 0

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    
    
divide(x, y)