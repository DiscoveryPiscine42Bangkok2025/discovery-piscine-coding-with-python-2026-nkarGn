#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
    
new = []
for value in array:
    if value > 5:
        new.append(value + 2)
    
print(array)
print(new)
