import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print(f"\nThe distance between the two points is: {distance:.2f}")

"""
REFLECTION:
Using a library is much more practical because it provides pre-tested, highly accurate 
# functions like math.sqrt() and math.pow(), saving me from writing complex square root 
# algorithms from scratch. In this activity, the library simplified my program into a 
# single, readable line of code. Without it, calculating a square root manually would 
# require dozens of extra lines of complex code, making the program harder to write and debug.
"""