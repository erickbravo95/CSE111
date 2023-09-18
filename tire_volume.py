"""The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a tire can 
be approximated with this formula:

v =     π w2 a(W a + 2,540 d)
        10,000,000,000

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches."""

from datetime import datetime
import math

current_date = datetime.now()
w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))
r = math.pi

v1 =  r*(w**2)*a
v2 =  (w*a)+(2540*d)
vt =  v1*v2/10000000000

print()
print (f"The approximate volume is {vt:.2f} liters")
print()
q=input("Would you like to buy tires with the entered dimensions(Y/N): ")

if q == "Y":
        phone = input("Enter your phone number: ")
        with open("volumes.txt","at") as volumes_file:
               print(f"{current_date:%Y-%m-%d}, {w}, {a}, {d}, {vt:.2f}, {phone}", file=volumes_file)  
else:
        with open("volumes.txt","at") as volumes_file:
               print(f"{current_date:%Y-%m-%d}, {w}, {a}, {d}, {vt:.2f}", file=volumes_file)  






