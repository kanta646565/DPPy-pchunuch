#!/usr/bin/env python3
user_input = input("your number\n")
if user_input.isnumeric():
    x = int(user_input)
    if x<=25 :
        while x<= 25 :
            print("Inside the loop, my variable is" ,x)
            x = x+1
    else :
        print("error")
   