#!/usr/bin/env python3
x = int(input("first number : "))
y = int(input("second number : "))
if  x * y == 0 :
    print("This number is both positive and negative")
elif x * y>0:
    print("This number is positive")
else :
     print("This number is negative")