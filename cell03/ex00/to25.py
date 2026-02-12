#!/usr/bin/env python3

print("Enter a number less than 25")
num = int(input())
if num > 25:
        print("Error")
else:
    current = num
    while current <= 25:
        print(f"Inside the loop, my variable is {current}")
        current += 1