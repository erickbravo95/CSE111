'''A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. 
Write a Python program named boxes.py that asks the user for two integers:

the number of manufactured items
the number of items that the user will pack per box

Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number. 
Note that the last box may be packed with fewer items than the other boxes.'''

import math

number_items = int(input("Enter the number of items: "))
number_item_box = int(input("Enter the number of items per box: "))

boxes = number_items / number_item_box

print(f"For {number_items} items, packing {number_item_box} items in each box, you will need {math.ceil(boxes)} boxes.")