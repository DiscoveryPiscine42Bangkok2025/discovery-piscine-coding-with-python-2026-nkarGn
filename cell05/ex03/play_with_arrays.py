#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
    
new = set()
    
for i in array:
    if i > 5:
        new.add(i + 2)
            
new_array = list(new)
    
print(array)
print(new_array)