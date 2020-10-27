﻿def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

a = float(input("Enter the first side's length: "))
b = float(input("Enter the second side's length: "))
c = float(input("Enter the third side's length: "))

if isItATriangle(a, b, c):
    print("Congratulations - it can be a triangle.")
else:
    print("Sorry, it won't be a triangle.")