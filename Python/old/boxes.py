import math

items = int(input("How many manufactured items are there? "))
boxes = int(input("How many items can fit in a box? "))

boxes_needed = math.ceil(items/boxes)
print(f"Boxes needed: {boxes_needed}")